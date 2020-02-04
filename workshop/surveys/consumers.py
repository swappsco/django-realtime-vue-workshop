# MyApp/consumers.py
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from workshop.surveys.models import Channel, Message


class SurveyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.channel_object, created = Channel.objects.get_or_create(
            name=self.room_name
        )

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(text_data)
        if text_data_json["type"] == "add_vote":
            message_object, created = Message.objects.get_or_create(
                content=message, channel=self.channel_object
            )

            if not created:
                message_object.count = message_object.count + 1
                message_object.save()

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {"type": "add_vote", "message": message}
            )
        if text_data_json["type"] == "get_survey_data":
            channel_messages = list(
                Message.objects.filter(channel=self.channel_object).values(
                    "content", "count"
                )
            )
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {"type": "populate_data", "data": channel_messages},
            )

    # Receive message from room group
    def add_vote(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "type": "add_vote"}))

    def populate_data(self, event):
        data = event["data"]
        print(data)
        self.send(text_data=json.dumps({"data": data, "type": "populate_data"}))

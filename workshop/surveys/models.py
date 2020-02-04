from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=255)


class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    count = models.IntegerField(default=1)

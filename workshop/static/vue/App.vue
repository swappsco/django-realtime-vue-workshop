<template>
  <div>
    <lobby v-if="!survey_started" @roomNameChange="createRoom($event)" />
    <div class="row" v-if="survey_started">
      <div class="col">
        <data-input :room_name="room_name" :results="results" :survey_title="survey_title" />
      </div>
      <div class="col">
        <chart :results="results" ref="chart" />
      </div>
    </div>
  </div>
</template>
<script>
import { eventBus } from "./main";
import Chart from "./components/Chart.vue";
import Lobby from "./components/Lobby.vue";
import DataInput from "./components/DataInput.vue";

export default {
  components: { lobby: Lobby, "data-input": DataInput, chart: Chart },
  props: { app_name: String, default: "" },
  data() {
    return {
      room_name: "",
      survey_title: "",
      socket: null,
      survey_started: false,
      datacollection: {},
      results: {}
    };
  },
  methods: {
    createRoom: function(room_name) {
      this.survey_title = room_name;
      this.room_name = room_name
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/\s+/g, "-")
        .toLowerCase();
      this.channel = this.room_name;
      this.socket = new WebSocket(
        "ws://" + window.location.host + "/ws/surveys/" + this.room_name + "/"
      );
      this.socket.addEventListener("open", this.opening);
      this.socket.addEventListener("message", this.handlerData);
      this.socket.addEventListener("close", this.close);
      this.survey_started = true;
      //   eventBus.goUrl("/" + this.room_name);
    },
    opening: function(e) {
      console.log("opening");
    },
    handlerData: function(e) {
      var data = JSON.parse(e.data);
      console.log(data);
    },
    close: function(e) {
      console.error("Socket closed unexpectedly");
    }
  }
};
</script>

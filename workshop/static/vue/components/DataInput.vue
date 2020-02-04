<template>
  <div class="chat">
    <h2>Survey: {{ survey_title }}</h2>
    <input
      id="chat-message-input"
      type="text"
      size="100"
      class="form-control"
      @keyup.enter="emitMessage"
      ref="input_message"
      v-model="message"
    />
    <br />
    <button id="chat-message-submit" class="btn btn-primary" @click="emitMessage">Vote</button>
    <br />
    <a href="/">Back to Lobby</a>
  </div>
</template>

<script>
import { eventBus } from "../main";
export default {
  props: {
    room_name: String,
    input_message: String,
    survey_title: String
  },
  data() {
    return { message: "" };
  },
  mounted() {
    this.$refs["input_message"].focus();
  },
  methods: {
    emitMessage: function() {
      this.$emit("voteSent", this.message);
      this.message = "";
    }
  }
};
</script>

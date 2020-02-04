<template>
  <div>
    <h2>Survey: {{ survey_title }}</h2>
    <input id="chat-message-input" type="text" size="100" class="form-control" v-model="message" />
    <br />
    <button id="chat-message-submit" class="btn btn-primary">Vote</button>
    <br />
    <a href="/">Back to Lobby</a>
  </div>
</template>

<script>
export default {
  props: {
    room_name: String,
    input_message: String,
    survey_title: String
  },
  data() {
    return { message: "" };
  }
};
</script>

<template>
  <div class="welcome">
    <div class="form-group">
      <label for="room-name-input">Please provide the name of the survey</label>
      <input
        id="room-name-input"
        type="text"
        size="100"
        v-model="room_name"
        placeholder="Name of the survey e.g. Mayor of the City"
        class="form-control"
        ref="input_room"
      />
    </div>
    <br />
    <button id="room-name-submit" class="btn btn-primary" @click="changeRoomName">Start Survey</button>
  </div>
</template>

<script>
export default {
  data() {
    return { room_name: "" };
  },
  mounted() {
    this.$refs["input_room"].focus();
  },
  methods: {
    changeRoomName: function() {
      this.$emit("roomNameChange", this.room_name);
    }
  }
};
</script>

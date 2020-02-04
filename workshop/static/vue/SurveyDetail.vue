<template>
  <div>
    <app :app_name="room_name" />
  </div>
</template>
<script>
import App from "./App.vue";

export default {
  components: { app: App },
  data() {
    return { room_name: roomName };
  },
  methods: {}
};
</script>

<template>
  <div class="message">
    {{ text }}
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    text: String,
    fromUser: Boolean
  }
}
</script>

<style scoped>
.message {
  width: 30vw;
  border: 1px solid #000;
}
</style>

<template>
  <div class="message">
    {{ msg }}
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.message {
  width: 30vw;
  border: 1px solid #000;
}
</style>

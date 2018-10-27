<template>
  <div class="messageContainer">
    <div class="message" v-bind:class="leftOrRight">
      {{ text }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    text: String,
    fromUser: Boolean
  },
  computed: {
    leftOrRight: function () {
      if (this.fromUser) return "msgRight"; else return "msgLeft"
    }
  }
}
</script>

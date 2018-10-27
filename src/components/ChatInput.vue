<template>
  <form @submit.prevent="sendMsg">
    <div class="chatinput input-group">
      <input v-model="currentMsg" type="text" class="form-control" placeholder="Message" aria-describedby="button-addon2" autofocus>
      <div class="input-group-append">
        <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Send</button>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: 'ChatInput',
  methods: {
    sendMsg: function () {
      this.$emit('msg', this.currentMsg)
      this.currentMsg=""
    }
  },
  data() {
    return {
      currentMsg: ""
    }
  }
}
</script>

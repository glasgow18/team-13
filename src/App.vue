<template>
  <div id="app">
    <template v-for="msg in messages">
      <message :text="msg.text" :fromUser="msg.fromUser"/>
    </template>
    <chat-input @msg="createMsg"/>
  </div>
</template>

<script>
import Message from './components/Message.vue'
import ChatInput from './components/ChatInput.vue'

export default {
  name: 'app',
  components: {
    Message,
    ChatInput
  },
  data () {
    return {
      messages: [{"text": "Hi there! How can I help you?", "fromUser": false}],
      msgCount: 1
    }
  },
  methods: {
    createMsg: function (text) {
      console.log('hi')
      this.$set(this.messages, this.msgCount++, {"text": text, "fromUser": true})
    }
  }
}
</script>

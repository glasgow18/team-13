<template>
  <div id="app">
    <chat-nav></chat-nav>
    <template v-for="msg in messages">
      <message :text="msg.text" :fromUser="msg.fromUser"/>
    </template>
    <chat-input @msg="createMsg"/>
  </div>
</template>

<script>
import Message from './components/Message.vue'
import ChatInput from './components/ChatInput.vue'
import ChatNav from './components/ChatNav.vue'

export default {
  name: 'app',
  components: {
    Message,
    ChatInput,
    ChatNav
  },
  data () {
    return {
      messages: [{"text": "Hi there! How can I help you?", "fromUser": false}],
      msgCount: 1
    }
  },
  methods: {
    createMsg: function (text, fromUser) {
      this.$set(this.messages, this.msgCount++, {"text": text, "fromUser": fromUser})
    }
  }
}
</script>

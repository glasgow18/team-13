<template>
  <div id="app">
    <message msg="hi"/>

    <chat-input/>
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
  }
}
</script>

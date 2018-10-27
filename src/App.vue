<template>
  <div id="app">
    <message msg="hi"/>
  </div>
</template>

<script>
import Message from './components/Message.vue'

export default {
  name: 'app',
  components: {
    Message
  }
}
</script>

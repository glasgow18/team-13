<template>
  <form @submit.prevent="sendMsg">
    {{response}}
    <div class="chatinput input-group">
      <input v-model="currentMsg" type="text" class="form-control" placeholder="Message" aria-describedby="button-addon2" autofocus>
      <div class="input-group-append">
        <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Send</button>
      </div>
    </div>
  </form>
</template>

<script>
  import axios from 'axios'
export default {
  name: 'ChatInput',
  methods: {
    sendMsg: function () {
      if (this.currentMsg.length>0) {
        this.$emit('msg', this.currentMsg, true)

      axios.post('/sendMessage', {
        text: this.currentMsg
      })
      .then((response) => {
        this.$emit('msg', response.data.text, false)
      })
      .catch(function (error) {
        console.log(error)
      });

        this.currentMsg = ""

      }
    }
  },
  data() {
    return {
      currentMsg: '',
    }
  }
}
</script>

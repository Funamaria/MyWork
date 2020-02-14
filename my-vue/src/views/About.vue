<template>
  <div id="about">
    <b-alert show variant="primary"><h2 class="subtitle">このサイトについて</h2></b-alert>

    <h4>1からポートフォリオとして作りました。</h4><br>
    <h4>時間がなく、中途半端に終わっています。</h4><br>
    <h4>よろしくお願いします。</h4>

  </div>
</template>

<script>
import axios from "axios";
export default {
  data(){
    return {
      name: "",
      comment: "",
      private: ""
    }
  },
  methods: {
    getContent() {
      axios.post('url', {
        fields: {
          name: {
            stringValue:this.name
          },
          comment: {
            stringValue: this.comment
          },
          private: {
            boolean: this.private
          }
        }
      })
    }
  }
}
</script>

<style scoped>

</style>

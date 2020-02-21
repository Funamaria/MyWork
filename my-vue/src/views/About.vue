<template>
  <div id="about">
    <b-alert show variant="primary"><h2 class="subtitle">このサイトについて</h2></b-alert>

    <h4>1からポートフォリオとして作りました。</h4><br>
    <h4>サイトの構成はメニューの環境に書いています。</h4><br>
    <h4>詳細は各項目をご覧ください。</h4>

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

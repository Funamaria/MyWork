<template>
  <div id="left">
    <div id="left-block">
      <form id="move-form">
        <h4>訪問コメント</h4>
        <div class="form-group">
          <label for="name">名前</label>
          <input
            class="form-control"
            id="name"
            v-model="name"
            type="text"
            placeholder="名前を入力してください"
          />
          <small id="nameHelp" class="form-text text-muted">残り文字数: {{ 18 - name.length }}</small>
        </div>
        <div class="form-group">
          <label for="input-comment">コメント</label>
          <textarea
            class="form-control"
            id="input-comment"
            v-model="comment"
            type="text"
            placeholder="コメントを入力してください"
          ></textarea>
          <small id="commnetHelp" class="form-text text-muted">残り文字数: {{ 140 - comment.length }}</small>
        </div>
        <button type="button" @click="sendContent" class="btn btn-primary">送信</button>
        <button type="button" @click="resetIn" class="btn btn-danger">リセット</button>
      </form>
    </div>
  </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js"></script>

<script>
import axios from "axios";
// const Cookie = require('js-cookie')
export default {
  data() {
    return {
      name: "",
      comment: "",
    }
  },
  methods: {
    sendContent() {
      var csrftoken = Cookies.get('csrftoken');
      var headers = {'X-CSRFToken': csrftoken};

      axios.post("api/content/", {
        name: this.name,
        comment: this.comment, 
      }, {headers: headers});
      this.name = "";
      this.comment = "";
      location.reload();
    },
    resetIn() {
      this.name = "";
      this.comment = "";
    }
  }
};
</script>

<style scoped>
#left {
  height: 2000px;
}
#left-block {
  width: 90%;
  height: 70%;
  margin: 0 auto;
}
#move-form {
  position: sticky;
  top: 95px;
}
</style>
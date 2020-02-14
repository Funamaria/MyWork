<template>
  <div>
    <div id="right-block">
      <h3>投稿一覧</h3>
      <div v-for="getpost in getposts" :key="getpost.name">
        <div id="nameandcomment">
          <div>名前:{{ getpost.name }}</div>
          <div>コメント:{{ getpost.comment }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      getname: "",
      getcomment: "",
      getposts: []
    };
  },
  created() {
    axios.get("http://127.0.0.1:8000/content/api/").then(response => {
      this.getposts = response.data;
    });
  },
  methods: {}
};
</script>

<style scoped>
#everycontent {
}
</style>
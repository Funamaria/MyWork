<template>
  <div>
    <div id="right-block">
      <h3>コメント一覧</h3>
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
    axios.get("api/content/").then(response => {
      this.getposts = response.data;
    });
  },
  methods: {}
};
</script>

<style scoped>

</style>
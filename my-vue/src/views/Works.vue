<template>
    <div id="works">
        <b-alert show variant="primary"><h2 class="subtitle">制作物</h2></b-alert>
        <h3>商品一覧</h3>

        <div v-for="getpost in getposts" :key="getpost.name">
            <div id="goods">
                <b-card
                    :title= "getpost.goodsname"
                    :img-src= "getpost.goodsimage"
                    img-alt="Image"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2">
                    <b-card-text>{{getpost.goodsdescription}}</b-card-text>
                    <b-button :href= "getpost.goodsurl" variant="primary">商品を見る</b-button>
                </b-card>
            </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            goodsname: "",
            goodsdescription: "",
            goodsprice:"",
            goodscategory:"",
            getposts: [],
        };
    },
  created() {
    axios.get("http://mynfportfolio.com/content/api/").then(response => {
      this.getposts = response.data;
    });
  },
}
</script>

<style>

</style>
<template>
    <div id="works">
        <div class="alert alert-primary" role="alert">一言日記</div>
        <div class="row">
            <div v-for="getpost in getposts" :key="getpost.name">
            <div class="col-sm-4">
                <div class="card" style="width: 16rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{ getpost.name }}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{ getpost.date }}</h6>
                            <p class="card-text">{{ getpost.description }}</p>
                    </div>
                </div>
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
      getposts: [],
      imageSrc: [
          '@/assets/camera.jpg',
          '@assets/caramel.jpg',
          '@assets/cat.jpg',
      ]
    };
  },
  created() {
    axios.get("api/goods/").then(response => {
      this.getposts = response.data;
    });
  },
  methods: {}
};
</script>

<style>

</style>
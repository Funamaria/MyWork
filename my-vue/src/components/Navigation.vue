<template>
    <div id="navigation">
        <b-navbar toggleable="lg" type="dark" variant="dark" class="p-4" fixed="top" id="nav-all">
        <b-navbar-brand href='/'>求職中</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item @click='toContent' to='About'>サイトについて</b-nav-item>
            <b-nav-item @click='toContent' to='MySelf'>自己紹介</b-nav-item>
            <b-nav-item @click='toContent' to="Works">制作物</b-nav-item>
            <b-nav-item @click='toContent' to="Contact">連絡先</b-nav-item>
            <b-nav-item @click='toContent' to="Environment">環境</b-nav-item>
            <!-- <div class="dropdown"> -->
          </b-navbar-nav>

        </b-collapse>
      </b-navbar>
    </div>
</template>

<script>
export default {
  methods: {
    toContent() {
      var el = document.getElementById('center-main');
      el.clientHeight - 95;
      el.scrollIntoView({
        behavior: "smooth",
      });
    }
  }

}
</script>

<style scoped>

#navigation {
  font-size:130%;
  margin-bottom: 95px;
}
</style>
<template>
  <div id="app">
    <div id="gloabal-nav">
      <Navigation />
    </div>
    <div id="header-parts">
      <HeaderParts></HeaderParts>
    </div>
    <div class="allcontent">
    <b-container fluid id="container">
      <b-row>
        <b-col cols="3" id="left-menu">
            <LeftMenu />
        </b-col>
        <b-col cols="6" id="center-main">
          <transition name="slide"
          enter-active-class="animated fadeInRight"
          leave-active-class="animated fadeOutLeft"
          mode="out-in">
            <router-view></router-view>
            </transition>
        </b-col>
        <b-col cols="3">
            <div id="right-menu">
            <RightMenu />
          </div>
        </b-col>
      </b-row>
    </b-container>
    </div>
  </div>
</template>

<script>
import HeaderParts from "./components/HeaderParts.vue";
import LeftMenu from "./components/LeftMenu.vue";
import RightMenu from "./components/RightMenu.vue";
import Navigation from "./components/Navigation.vue";



export default {
  name: "app",
  components: {
    HeaderParts,
    LeftMenu,
    RightMenu,
    Navigation
  },
  data(){
    return {
 
    }
  },
  methods: {
  }


};
</script>

<style>
html {
  scroll-padding-top:95.2px;
}
#header-parts {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#allcontent {
  height: 2000px;
}
#center-main {
  height: 2000px;
}
.slide-move {
  transition: transform 1s;
}
.subtitle {
  text-align: center;
}
.slide-enter {
  opacity: 1;
}

.slide-enter-to {
  opacity: 0;
}
.slide-leave {
  opacity: 1;
}
.slide-leave-to {
  opacity: 0;
}
.animate {
  transition:animated feedOutLeft delay-1s;
}


</style>

<template>
  <div id="app-wrapper">
    <AppHeader/>
    <section>
      <div class = "menuContent">
        <MainMenu/>
      </div>

      <div class = "mainContent">
        <RouterView />
      </div>
    </section>
    <AppFooter/>
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
import AppHeader from "./components/AppHeader.vue";
import MainMenu from "./components/MainMenu.vue";
import AppFooter from "./components/AppFooter.vue";
</script>

<style>
.menuContent {  
  width: 20%;
}

.mainContent{
  width: 80%;
}
section{
  display: flex;
  flex-direction: row;
  
}
</style>
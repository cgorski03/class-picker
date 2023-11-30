<template>
  <div id="app-wrapper">
    <AppHeader/>
    <RouterView/>
    <AppFooter/>
  </div>
</template>

<script setup>
  import { RouterView } from "vue-router";
  import AppHeader from "./components/AppHeader.vue";
  import AppFooter from "./components/AppFooter.vue";
</script>

<style>
#app-wrapper{
  height: 100vh;
  width: 100%;
}
</style>
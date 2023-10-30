<template>
  <nav>
    <ul class="menu">
      <li class="titleItem">Main Menu</li>
      <li v-for="option in menuOptions">
        <MainMenuSelection :name = option.option :path = option.path></MainMenuSelection>
      </li>
    </ul>
  </nav>  
</template>

<script setup>
import MainMenuSelection from "./MainMenuSelection.vue";
import versionState from '../state/version';
import { ref } from 'vue'

let menuOptions = ref(versionState.getMenuOptions);

</script>


<style>

.menu{
    list-style-type: none;
}

.titleItem{
    color: White;
    padding: 25px;
    font-weight: bold;
    font-size: 1.5rem;
    text-align: center;
    border-bottom: 1px solid Black;
}

.emptySpace {
    background: #B90E0A;
    width: 100%;
    padding: auto;
}
</style>

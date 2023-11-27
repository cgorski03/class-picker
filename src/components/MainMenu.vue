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

//ouputs different menu options based on student or teacher state
let menuOptions = [
        { option: "Tutorial", id: 1, path:"/tutorial" },
        { option: "Add Classes", id: 4, path:"/addclasses" },
        { option: "Drop Classes", id: 5, path:"/dropclasses" },
        { option: "View Schedule", id: 2, path:"/schedule" },
        { option: "Sign Out", id: 3, path:"/" },
      ]

</script>


<style>

nav{
  height: 100%;
}

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

</style>

<template>
    <nav>
    <ul class="menu">
      <li class="titleItem">Main Menu</li>
      <li class="item"><RouterLink  to="/">Tutorial</RouterLink></li>
      <li class="item"><RouterLink  to="/">Add Classes</RouterLink></li>
      <li class="item"><RouterLink  to="/">Drop Classes</RouterLink></li>
      <li class="item"><RouterLink  to="/">View Schedule</RouterLink></li>
      <li class="item"><RouterLink  to="/">Sign Out</RouterLink></li>
      <li class="emptySpace"></li>
    </ul>
    </nav>  
</template>

<script setup>
// import the <RouterLink> component so that we can use it in the template above
import { RouterLink } from "vue-router";
</script>


<style>

.menu{
    list-style-type: none;
}
nav {
    background: #B90E0A;
    padding: 0 0;
    border: 1px solid Black;
}

.titleItem{
    color: White;
    padding: 30px;
    font-weight: bold;
    font-size: 1.5rem;
    text-align: center;
    border-bottom: 1px solid Black;
}
.item {
    border-bottom: 1px solid Black;
    color: White;
    font-weight: bold;
    font-size: 1rem;
    padding: 25px;
}
.emptySpace{
    padding: 30px;
}

section {
  display: block;
}

</style>

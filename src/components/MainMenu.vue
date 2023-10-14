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

<script>
// Using router Link to link to different web pages
import { RouterLink } from "vue-router";

const studentMenuOptions = ["Tutorial", "Add Classes", "Drop Classes", "View Schedule", "Sign Out" ]
const teacherMenuOptions = ["Tutorial", "View Schedule", "Sign Out"]

export default{
    
}

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
    padding: 25px;
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
    padding: 20px;
}
.emptySpace{
    padding: 58px;
}

section {
  display: block;
}

</style>

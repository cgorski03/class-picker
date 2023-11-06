<template>
    <nav>
      <ul class="AddClassTable">
        <li class="titleItem">Classes</li>
        <li v-for="class in classes">
          <ClassData></ClassData>
        </li>
      </ul>
    </nav>  
  </template>
  
  <script setup>
  import ClassData from './ClassData'
  import { ref } from 'vue'
  
  let classes = ref();
  
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
  
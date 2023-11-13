<template>
  <nav>
    <ul class="AddClassTable">
      <li class="titleItem">Classes</li>
      <li v-for="classInstance in props.classes" :key="classInstance.classTitle">
        <ClassData :classData="classInstance"></ClassData>
      </li>
    </ul>
  </nav>
</template>


<script setup>
import ClassData from "../components/ClassData.vue"

const props = defineProps({
  classes: {
    type: Array,
    default: () => [],
  },
})
</script>

<style>
.menu {
  list-style-type: none;
}

.titleItem {
  color: white;
  padding: 25px;
  font-weight: bold;
  font-size: 1.5rem;
  text-align: center;
  border-bottom: 1px solid black;
}

.emptySpace {
  background: #B90E0A;
  width: 100%;
  padding: auto;
}
</style>

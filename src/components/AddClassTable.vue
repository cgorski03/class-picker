<template>
  <nav>
    <ul class="AddClassTable">
      <li id="titleItem">
        <h2>Classes</h2>
      </li>
      <li v-for="classInstance in props.classes" :key="classInstance.classTitle">
        <ClassData :classData="classInstance"></ClassData>
      </li>
    </ul>
  </nav>
</template>


<script setup>
import ClassData from "../components/ClassData.vue"
console.log("props.classes: "+props.classes)
const props = defineProps({
  classes: {
    type: Array,
    default: () => [],
  },
})
</script>

<style>
#titleItem {
  color: white;
  padding: 25px;
  font-weight: bold;
  font-size: 1.5rem;
  text-align: center;
  border-bottom: 1px solid black;
}
</style>

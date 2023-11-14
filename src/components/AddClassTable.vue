<template>
  <div id="tableLayout">
    <div id="classSearch">
      <nav>
        <ul class="AddClassTable">
          <li id="titleItem">
            <h2>Classes</h2>
          </li>
          <li v-for="classInstance in props.classes" :key="classInstance.classTitle">
            <div>
              <ClassData @sendclass="loadYourClasses" :classData="classInstance"></ClassData>
            </div>
          </li>
        </ul>
      </nav>
    </div>
    <div id="yourClasses">
      <nav>
        <ul class="YourClassTable">
          <li id="titleItem">
            <h2>Your Classes</h2>
          </li>
          <li id="yourclassitem" v-for="c in yourclasseslist">
            <p>{{ c }}</p>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script setup>
import ClassData from "../components/ClassData.vue";
import { ref } from 'vue';

let yourclasseslist = ref([]);


const props = defineProps({
  classes: {
    type: Array,
    default: () => [],
  },
});

//const { emit } = defineEmits(['sendclass']);

const loadYourClasses = (yourCurrentClassList) => {
  console.log('loadYourClasses called with:', yourCurrentClassList);
  yourclasseslist.value = yourCurrentClassList;
};
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

#tableLayout{
  display: flex;
  flex-direction: row;
}

#classSearch{
  width: 80%;
}

#yourClasses{
  width: 20%
}

#yourclassitem{
  border: 2px black;
}
</style>

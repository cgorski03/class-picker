<template>
  <div id="tableborder">
    <div id ="tableLayout">
      <div id="classSearch">
        <nav>
          <ul class="AddClassTable">
            <li id="titleItem">
              <h2 id="classtableitemtitle">Available Classes</h2>
            </li>
            <Loading v-if="loading"/>
            <li v-for="classInstance in props.classes" :key="classInstance.classTitle">
              <div>
                <ClassData @sendclass="loadYourClasses" @toggleloader="loadingHandler" @refresh="refreshHandler" :classData="classInstance"></ClassData>
              </div>
            </li>
          </ul>
        </nav>
      </div>
      <div id="yourClasses">
        <nav>
          <ul class="YourClassTable">
            <li id="titleItem">
              <h2 id="classtableitemtitle">Your Classes</h2>
            </li>
            <Loading v-if="yourclassesloader"/>
            <li id="yourclassitem" v-for="c in yourclasseslist">
              <p style="color: black;">{{ c }}</p>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup>
import ClassData from "../components/ClassData.vue";
import { ref } from 'vue';
import Loading from "../components/Loading.vue"

let yourclasseslist = ref([]);
let yourclassesloader =ref(false);
//takes in an array of classes
const props = defineProps({
  classes: {
    type: Array,
    default: () => [],
  },
  loading:Boolean,
});

//this handles the data sent up by the child component
const emit = defineEmits("refresh")

const refreshHandler = () =>{
  emit("refresh")
}
const loadYourClasses = (yourCurrentClassList) => {
  console.log('loadYourClasses called with:', yourCurrentClassList);
  yourclasseslist.value = yourCurrentClassList;
};

const loadingHandler = () => {
  yourclassesloader.value =  !yourclassesloader.value;
}
</script>

<style>
#titleItem {
  padding: 25px;
  font-weight: bold;
  font-size: 1.5rem;
  text-align: center;
  border-bottom: 1px solid black;
}

#tableLayout{
  margin-left: auto;
  margin-right: auto;
  height: 100%;
  width: 94%;
  background-color: #151E3D;
  display: flex;
  flex-direction: row;
}

#tableborder{
  padding-top: 3%;
  padding-bottom: 3%;
  height: 65vh;
  width: 100%;
  background-color: #151E3D;
}

#classSearch{
  width: 67.5%;
  background-color: white;
  margin-right: 2.5%;
  overflow: auto;
}

#yourClasses{
  width: 30%;
  background-color: white;
  overflow: auto;
}

#yourclassitem{
  border-bottom: 1px solid black;
  padding: 10px;
}

.AddClassTable{
  height: auto;
  max-height: auto;
}

#classtableitemtitle{
  color: black;
}

</style>
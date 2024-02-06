<template>
  <div id="tableborder">
    <div id="tableLayout">
      <div id="classSearch">
        <nav>
          <ul class="AddClassTable">
            <li id="titleItem">
              <h2 id="classtableitemtitle">Available Classes</h2>
            </li>
            <Loading v-if="loading" />
            <li
              v-for="classInstance in props.classes"
              :key="classInstance.classTitle"
              style="position: relative">
              <div>
                <ClassData
                  @sendclass="loadYourClasses"
                  @toggleloader="loadingHandler"
                  @refresh="refreshHandler"
                  :classData="classInstance"></ClassData>
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
            <Loading v-if="yourclassesloader" />
            <li id="yourclassitem" v-for="c in yourclasseslist">
              <p style="color: black">{{ c }}</p>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup>
import ClassData from "../components/classdata.vue";
import { ref } from "vue";
import Loading from "../components/Loading.vue";

let yourclasseslist = ref([]);
let yourclassesloader = ref(false);
//takes in an array of classes
const props = defineProps({
  classes: {
    type: Array,
    default: () => [],
  },
  loading: Boolean,
});

//this handles the data sent up by the child component
const emit = defineEmits("refresh");

const refreshHandler = () => {
  emit("refresh");
};
const loadYourClasses = (yourCurrentClassList) => {
  yourclasseslist.value = yourCurrentClassList;
};

const loadingHandler = () => {
  yourclassesloader.value = !yourclassesloader.value;
};
</script>

<style>
#titleItem {
  padding: 25px;
  font-weight: bold;
  font-size: 1.5rem;
  text-align: center;
  border-bottom: 1px solid #e0e0e0; /* Softer border color */
}

#tableLayout {
  margin: auto;
  height: 125%;
  width: 100%;
  background-color: #f7f7f7; /* Lighter background for the entire table area */
  display: flex;
  flex-direction: row;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* subtle shadow for depth */
}

#tableborder {
  padding-top: 3%;
  padding-bottom: 3%;
  height: 75vh;
  width: 100%;
  background-color: #f7f7f7; /* Lighter background for the table border */
}

#classSearch {
  width: 67.5%;
  background-color: white;
  margin-right: 2.5%;
  overflow: auto;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); /* subtle inset shadow for depth */
}

#yourClasses {
  width: 30%;
  background-color: rgb(255, 255, 255);
  overflow: auto;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); /* subtle inset shadow for depth */
}

#yourclassitem {
  border-bottom: 1px solid #e0e0e0; /* Softer border color */
  padding: 10px;
}

.AddClassTable {
  height: auto;
  background-color: #eeeeee; /* Slightly darker background for contrast */
  max-height: auto;
}

#classtableitemtitle {
  color: #333; /* Dark grey color for better readability */
}

#yourClasses #titleItem {
  background-color: #33333314; /* Match the background color with the Available Classes header */
}
/* Global font setting */
body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
}
</style>

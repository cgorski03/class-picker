<template>
  <main>
    <div class="menuContent">
      <MainMenu />
    </div>

    <div class="mainContent">
      <div class="home">
        <div class="formatText">
          <h2>Add Classes</h2>
        </div>
        <div>
          <form class="searchbar">
            <div id="searchfield">
              <input
                type="text"
                placeholder="Search by keyword"
                id="className"
                v-model="className"
              />
            </div>
            <div id="searchbutton">
              <button @click.prevent="search"></button>
            </div>
          </form>
        </div>
        <div id ="tablediv">
          <ClassTable :classes="classList" :loading="loading"></ClassTable>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import MainMenu from "../components/MainMenu.vue";
import ClassTable from "../components/AddClassTable.vue";
import { ref, reactive } from "vue";
import versionState from '../state/version';
import { check_compatibility } from '../classes/check'

let loading = ref(false)
//stores the user input
let className = ref("");

//stores the list of classes to send to the child component
let classList = ref([]);

class Class {
  constructor(classTitle, classCA, classCANum, classSubj, daysMeet, startTime, endTime) {
    this.classTitle = classTitle;
    this.classCA = classCA;
    this.classCANum = classCANum;
    this.classSubj = classSubj;
    this.daysMeet = daysMeet;
    this.startTime = startTime;
    this.endTime = endTime;
    this.isCompatible = ref(false);
    this.conflictingCourse = ref('')
  }
}

//searches for classes in the databased by name
const search = async () => {
  classList.value = [];
  loading.value =true;
  try {
    // Encode the className parameter
    const encodedClassName = encodeURIComponent(className.value);

    // Implement fetch to get a list of classes corresponding to name
    const response = await fetch(
      `https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/search?search=${encodedClassName}`
    );

    // Log the entire response to the console
    const responseText = await response.text();

    // Check if the response is successful (status code 2xx)
    if (response.ok) {
      const responseData = JSON.parse(responseText);

      // Clear existing classList
      
      // Loop through the responseData and create instances of Class
      for (const key in responseData) {
        if (Object.hasOwnProperty.call(responseData, key)) {
          const item = responseData[key];
          const newClass = reactive(
            new Class(
              item.Title,
              item['CA DESCR'],
              item['CAT NBR'],
              item.SUBJ,
              item.days_meet,
              item.start_time,
              item.end_time
            )
          );
          /*const isCompatible = await check_compatibility(item.Title, versionState.getuserID.value);
          newClass.isCompatible = isCompatible;
          */
          classList.value.push(newClass);
        }
      }
      check_compatibility(classList, versionState.getuserID.value);
      
    } else {
      console.log("Error response:", responseText);
    }
  } catch (error) {
    console.error("Error during fetch:", error);
  }
  loading.value =false;
};

</script>

<style scoped>
.home {
  overflow: hidden;
  padding: 0;
  display: flex;
  flex-direction: column;
  height: 100%;
  max-height: 100%;
}

.home h2 {
  text-align: center;
  font-size: 1.5rem;
  background-color: #151e3d;
  color: white;
  padding: 25px;
}

.menuContent {
  height: auto;
  width: 20%;
  background-color: #b90e0a;
  border: 2px black;
}

.mainContent {
  min-height: max-content;
  height: auto;
  width: 80%;
}

main {
  display: flex;
  flex-direction: row;
  height: 100vh;
}

.searchbar {
  background-color: #151e3d;
  margin-top: 30px;
  margin-bottom: 30px;
  margin-left: 60px;
  margin-right: 60px;
  padding: 30px;
  width: 90%;
  display: flex;
  flex-direction: row;
}
.searchbar #searchfield {
  margin-left: 120px;
  width: 75%;
}

.searchbar input {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  font-size: 30px;
  display: block;
}

.searchbar input::placeholder {
  text-align: center;
  color: black;
  font-weight: 500;
}
.searchbar input:hover {
  background-color: lightgray;
}

.searchbar button {
  border-radius: 15%;
  background: url("../assets/images/search.webp") no-repeat scroll 0 0 transparent;
  background-size: 50px;
  color: #000000;
  cursor: pointer;
  padding: 25px 25px;
  border: 1px white;
}

.searchbar button:hover {
  background-color: grey;
}

.searchbar button:active {
  background-color: darkgray;
}

#tablediv{
  align-self: center;
  width: 90%;
  overflow: hidden;
  height: auto;
}
</style>

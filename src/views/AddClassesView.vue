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
        <div id="tablediv">
          <ClassTable @refresh="refreshHandler" :classes="classList" :loading="loading"></ClassTable>
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
import { Class } from '../classes/module'
let loading = ref(false)
//stores the user input
let className = ref("");
//stores the list of classes to send to the child component
let classList = ref([]);

const refreshHandler = () =>{
  search();
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
  background-color: #A9A9A9;
}

.home h2 {
  text-align: center;
  font-size: 1.5rem;
  background-color: #151E3D; /* Blue background color */
  color: white;
  padding: 1rem; /* Adjusted padding */
  margin: 0;
}

.menuContent {
  height: 100%;
  width: 20%;
  background-color: #b90e0a;
  border: 2px solid black;
}

.mainContent {
  min-height: 100%;
  height: 100%;
  width: 80%;
}

main {
  display: flex;
  flex-direction: row;
  height: 100vh;
}

.searchbar {
  background-color: #3A3B3C; /* Light background color */
  margin: 30px auto;
  padding: 1rem; /* Adjusted padding */
  width: 90%;
  display: flex;
  flex-direction: row;
  align-items: center; /* Align items vertically */
}

.searchbar #searchfield {
  flex-grow: 1; /* Allow the input to grow and fill available space */
  margin-right: 1rem; /* Added margin */
}

.searchbar input {
  width: 100%;
  font-size: 1rem; /* Adjusted font size */
  padding: 0.5rem; /* Adjusted padding */
}

.searchbar input::placeholder {
  text-align: center;
  color: #7f8c8d; /* Light text color */
}

.searchbar input:hover {
  background-color: #dfe6e9; /* Light background color on hover */
}

.searchbar button {
  border-radius: 50%;
  background: url("../assets/images/search.webp") no-repeat scroll 0 0 transparent;
  background-size: 30px; /* Adjusted background size */
  color: #000000;
  cursor: pointer;
  padding: 0.75rem; /* Adjusted padding */
  border: 1px solid white; /* Adjusted border color */
}

.searchbar button:hover {
  background-color: #bdc3c7; /* Light background color on hover */
}

#tablediv {
  align-self: center;
  width: 90%;
  overflow: hidden;
  height: 100%;
}
</style>
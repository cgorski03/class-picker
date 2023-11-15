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
                @keyup.enter="search"
              />
            </div>
            <div id="searchbutton">
              <button @click.prevent="search"></button>
            </div>
          </form>
        </div>
        <div>
          <ClassTable :classes="classList"></ClassTable>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import MainMenu from "../components/MainMenu.vue";
import ClassTable from "../components/AddClassTable.vue";
import { ref, reactive } from "vue";

let className = ref("");
let classList = ref([]);

class Class {
  constructor(classTitle, classCA, classCANum, classSubj) {
    this.classTitle = classTitle;
    this.classCA = classCA;
    this.classCANum = classCANum;
    this.classSubj = classSubj;
  }
}

const search = async () => {
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
      classList.value = [];

      // Loop through the responseData and create instances of Class
      for (const key in responseData) {
        if (Object.hasOwnProperty.call(responseData, key)) {
          const item = responseData[key];
          const newClass = reactive(
            new Class(
              item.Title,
              item['CA DESCR'],
              item['CAT NBR'],
              item.SUBJ
            )
          );
          classList.value.push(newClass);
        }
      }

    } else {
      console.log("Error response:", responseText);
    }
  } catch (error) {
    console.error("Error during fetch:", error);
  }
};

</script>

<style scoped>
/* Main layout */
/* Main layout */
main {
  display: flex;
  flex-direction: row;
}

.menuContent {
  width: 20%;
  background-color: #b90e0a;
  border: 2px solid black; /* Ensure border is visible */
}

.mainContent {
  width: 80%;
  padding: 20px; /* Add some padding for spacing */
}

/* Home and heading styles */
.home {
  display: flex;
  flex-direction: column;
}

.home h2 {
  text-align: center;
  font-size: 2rem; /* Slightly larger for emphasis */
  background-color: #151e3d;
  color: white;
  padding: 15px;
  margin-bottom: 20px; /* Space below heading */
}

/* Search bar styles */
.searchbar {
  background-color: #151e3d;
  padding: 20px;
  margin: 0 60px; /* Simplified margin */
  border-radius: 10px; /* Rounded corners */
  display: flex;
  align-items: center; /* Align items vertically */
  justify-content: space-between; /* Space out fields */
}

.searchbar #searchfield {
  flex-grow: 1; /* Allow search field to grow */
  margin-right: 20px; /* Space between field and button */
}

.searchbar input {
  width: 100%;
  font-size: 1rem;
  padding: 10px; /* Padding for better text visibility */
  border-radius: 5px; /* Rounded corners for input */
}

.searchbar input::placeholder {
  color: #aaa; /* Lighter color for placeholder */
}

.searchbar input:hover {
  background-color: #e8e8e8; /* Light hover effect */
}

/* Button styles */
.searchbar button {
  background: url("../assets/images/search.webp") no-repeat center;
  background-size: contain;
  width: 50px; /* Fixed width for button */
  height: 50px; /* Fixed height for button */
  border: none; /* Remove border */
  cursor: pointer;
}

.searchbar button:hover {
  background-color: #ccc; /* Hover effect for button */
}

.searchbar button:active {
  background-color: #bbb; /* Active state effect */
}

</style>

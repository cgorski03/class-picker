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
/* Main content area */
.home {
  overflow: hidden;
  padding: 0;
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: #F5F5F5; /* Updated background color for a cleaner look */
}

/* Header styling */
.home h2 {
  text-align: center;
  font-size: 2rem; /* Keep the font size for emphasis */
  background-color: #151E3D; /* Updated to a more modern navy blue */
  color: white;
  padding: 1rem;
  margin-bottom: 20px; /* Add some space below the heading */
}

/* Side menu styling */
.menuContent {
  height: 95%;
  width: 20%;
  background-color: #B90E0A; /* Updated to a softer shade of blue */
  border-right: 1px solid #000000; /* Light border for separation */
}

/* Main content styling */
.mainContent {
  min-height: 100%;
  height: 100%;
  width: 80%;
  padding: 20px;
}

/* Flexbox layout for main area */
main {
  display: flex;
  flex-direction: row;
  height: 100vh;
}

/* Search bar container */
.searchbar {
  background-color: #FFFFFF; /* Use white for the search bar for a clean look */
  margin: 30px auto;
  padding: 1rem;
  width: 90%;
  display: flex;
  flex-direction: row;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Subtle shadow for depth */
  border-radius: 4px; /* Rounded corners for modern feel */
}

/* Search input field */
.searchbar #searchfield {
  flex-grow: 1;
  margin-right: 1rem;
}

/* Search input styling */
.searchbar input {
  width: 100%;
  font-size: 1rem;
  padding: 0.5rem;
  border: 1px solid #DADFE1; /* Soften the border color */
  border-radius: 4px; /* Rounded corners for the input field */
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.075); /* Inner shadow for depth */
}

/* Placeholder text color */
.searchbar input::placeholder {
  color: #95A5A6; /* Lighten the placeholder text */
}

/* Hover effect for search input */
.searchbar input:hover {
  background-color: #ECF0F1; /* Slightly lighter background on hover */
  border-color: #BDC3C7; /* Border color to match hover bg */
}

/* Search button styling */
.searchbar button {
  border-radius: 50%;
  background: url("../assets/images/search.webp") no-repeat center center / cover; /* Ensure the icon covers the area */
  cursor: pointer;
  padding: 0.75rem;
  border: none; /* Remove border for a cleaner button */
  width: 48px; /* Define a fixed width */
  height: 48px; /* Define a fixed height */
  display: inline-block; /* Use inline-block for proper sizing */
  outline: none; /* Remove the outline to maintain the style on focus */
}

/* Hover effect for the search button */
.searchbar button:hover {
  background-color: #BDC3C7; /* Light background color on hover */
  background-size: 60%; /* Make the icon a bit smaller on hover */
}

/* Table container */
#tablediv {
  align-self: center;
  width: 90%;
  overflow: hidden;
  height: 100%;
  background-color: #FFFFFF; /* White background for the table container */
  border-radius: 4px; /* Rounded corners for the table container */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Shadow for depth */
}
</style>


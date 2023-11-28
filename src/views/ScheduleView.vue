<template>
    <main>
      <div class = "menuContent">
        <MainMenu/>
      </div>
  
      <div class = "mainContent">
        <div class="home">
          <div class = "formatText">
            <h2>Schedule</h2>
          </div>
          <div id="tablediv">
            <div id="droptableborder">
              <div id="droptableLayout">
                  <nav>
                  <ul>
                      <Loading v-if="isLoading" />
                      <li v-for="course in classlist" :key="course">
                      <div id="indivisualCourse">
                          <label class="container">
                          {{ course }}
                          <input type="checkbox" v-model="selectedCourses" :value="course">
                          <span class="checkmark"></span>
                          </label>
                      </div>
                      </li>
                  </ul>
                  </nav>
              </div>
          </div>
        </div>
        </div>
      </div>
  
    </main>
  </template>
  
  <script setup>
  import MainMenu from "../components/MainMenu.vue";
  import Loading from "../components/Loading.vue"
  import versionState from "../state/version";
  import {ref, onMounted} from 'vue';

  let classlist = ref([]);
  let isLoading = ref(false);

  onMounted(() => {
    const username = 'jak19018'; // Replace with the actual username
    fetchData(username);
  });

  const fetchData = async (username) => {
    isLoading.value = true;
    try {
      const response = await fetch(
        `https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class?username=${username}`,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
  
      if (response.ok) {
        const data = await response.json();
        classlist.value = data;
      } else {
        console.error('Error fetching data:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
    isLoading.value = false;
  };
  
  </script>
  <style scoped>
  .home {
    padding: 0;
    display: flex;
    flex-direction: column;
  }
  
  .home h2 {
    text-align: center;
    font-size: 1.5rem;
    background-color: #151E3D;
    color: white;
    padding: 25px;
  }
  
  .menuContent {  
    width: 20%;
    background-color: #B90E0A;
    border: 2px black;
  }
  
  .mainContent{
    width: 80%;
  }
  
  main{
    display: flex;
    flex-direction:row;  
  }
  
  </style>
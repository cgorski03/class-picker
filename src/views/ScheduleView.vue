<template>
  <main>
    <div class="menuContent">
      <MainMenu/>
    </div>

    <div class="mainContent">
      <div class="home">
        <div class="formatText">
          <h2>Schedule</h2>
        </div>
        <div id="tablediv">
          <div id="droptableborder">
            <div id="droptableLayout">
              <nav>
                <ul>
                  <Loading v-if="isLoading" />
                  <li v-for="course in classList" :key="course.classTitle">
                    <dropdown :course="course" :isStudent="versionState.getVersion.value"></dropdown>
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
  import {ref, onMounted, reactive} from 'vue';
  import { Class } from '../classes/module';
  import dropdown from '../components/dropdown.vue';
  import { useAuth0} from '@auth0/auth0-vue';
  const { logout } = useAuth0();


  onMounted(() => {
    const username = versionState.getuserID.value;
    fetchData(username);

  });
  let isLoading = ref(false);
  let classList = ref([]);
  
    const fetchData = async (username) => {
    classList.value = [];
    isLoading.value =true;
    try {
      if(username == ''){
        alert('Your session has expired');
        logout({
            logoutParams: {
                returnTo: window.location.origin
            },
        });
      }
      // Encode the username parameter
      const encodedUsername = encodeURIComponent(versionState.getuserID.value);
      const apiUrl = versionState.getVersion.value
      ? `https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class/detailed?username=${encodedUsername}`
      : `https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class/teacher?username=${encodedUsername}`;

      // Implement fetch to get a list of classes corresponding to name
      const response = await fetch(apiUrl);
      const responseText = await response.text();
      // Check if the response is successful (status code 2xx)
      if (response.ok) {
        console.log(responseText)
        const responseData = JSON.parse((JSON.parse(responseText)).courses);
        console.log(responseData)

        // Loop through the responseData and create instances of Class
        for (const item of responseData) {
            const newClass = reactive(
              new Class(
                item.Title,
                item['CA DESCR'],
                item['CAT NBR'],
                item.SUBJ,
                item.days_meet,
                item.start_time,
                item.end_time,
              )
            );
            if(!versionState.getVersion.value){
              newClass.studentList = item.students;
            }
            classList.value.push(newClass);
        }
      } else {
        console.log("Error response:", response.text);
      }
    } catch (error) {
      console.error("Error during fetch:", error);
    }
    isLoading.value =false;

    }
  
  </script>
  <style scoped>
  /* Main layout */
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
  margin-bottom: -20px; /* Add some space below the heading */
}

  /* Table container */
  #tablediv {
    align-self: center;
    width: 100%;
    overflow: hidden;
    height: calc(100vh - 50px); /* Adjusted for header height */
    background-color: white;
    border-radius: 4px; /* Rounded corners for modern feel */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Subtle shadow for depth */
    margin-top: 20px; /* Space between header and table */
    margin-bottom: 20px; /* Space at the bottom */
  }
  
  /* Table layout for 'Schedule' */
  #droptableLayout {
    margin: auto;
    width: 100%;
    background-color: #F5F5F5; /* Consistent background for both */
    display: flex;
    flex-direction: column;
  }
  
  /* Adjustments for checkboxes and custom checkmarks */
  /* ... (keep your existing styles for checkboxes and checkmarks) ... */
  
  </style>
  
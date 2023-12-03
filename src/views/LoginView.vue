<template>
  <main> 
    <div class = "left">
      <img src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
    </div>

    <div class = "middle">
      <h2 class = "title">{{versionState.getLoginTitle.value}}</h2>
      <form name="login-form">

        <!-- Could add hover to input for clearner look down the road --->

        <div>
          <label for="username" class = "upText">Username</label>
          <input class = "upFormat" type="text" id="username" v-model="username" />
        </div>
        <div>
          <label for="password" class = "upText">Password</label>
          <input class = "upFormat" type="password" id="password" v-model="password" />
        </div>
        <button class="btn" type="submit" v-on:click.prevent="login()">
          Login
        </button>
      </form>
    </div>

   <div class = "right">
     <img src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
   </div>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import versionState from '../state/version';
import { useRouter } from 'vue-router';

const router = useRouter();
const apiURL = 'https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/authenticate';

const username = ref('');
const password = ref('');
let state = '';

//checks if user has a username and password in our database
//Will replace with auth 0
const login = () => {
  // Construct the url of the get request
  state = versionState.getVersion.value ? 'user' : 'teacher';
  const url = `${apiURL}?username=${username.value}&password=${password.value}&state=${state}`;
  
  fetch(url, {
    method: 'GET',
  })
  .then(response => {
    console.log(response.status);

    if (response.ok) {
      console.log('Request was successful');
      router.push('/home');
    } else if (response.status === 400) {
      alert('Please input a username and password');
    } else if (response.status === 401) {
      alert('Username or password are incorrect. Please try again.');
    }
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });
}
</script>


<style>

/* Reset some default styles and apply a full height to the body and main container */
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow-x: hidden; /* Prevent horizontal scroll */
  background-image: url('C:\Users\archi\project2102\Group-Project\src\views\UCONNLOGIN.jpg'); /* Ensure this is the correct relative path */
  background-size: cover;
  background-position: center;
  background-attachment: fixed; /* Keep the background fixed when scrolling */
}

/* If you have an #app div that wraps your entire Vue app, apply styles there too */
#app {
  min-height: 100vh; /* Full viewport height */
  display: flex;
  flex-direction: column;
}

/* Remove the background styles from the main tag */
main {
  flex-grow: 1; /* Take up all available vertical space */
  display: flex;
  flex-direction: column; /* Stack children vertically */
  justify-content: center;
  align-items: center;
  padding-top: 60px; /* Adjust this value to match the height of your header */
  padding-bottom: 60px; /* Adjust this value to match the height of your footer */
  /* No background image here */
}

/* Adjust the .middle class for the login form container */
.middle {
  margin-top: 95px; /* You might not need this if the main tag is centering content */
  width: 30%; /* Adjust width as needed */
  background-color: rgba(255, 255, 255, 0.70); /* Semi-transparent background */
  padding: 40px;
  border-radius: 15px; /* Rounded corners for the form */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

/* ... other styles ... */


.title {
  text-align: center;
  margin-bottom: 25px;
  font-size: 30px;
  color: #151E3D; /* Adjusted the color for contrast against the light background */
}

.upFormat {
  width: 100%; /* Full width of the form */
  font-size: 18px; /* Adjusted for better readability */
  padding: 10px;
  border: 1px solid #ccc; /* Subtle border */
  border-radius: 8px; /* Rounded corners for the input fields */
  margin-bottom: 20px; /* Space between the input fields */
}

.upText {
  font-size: 18px;
  color: #151E3D; /* Matching the title */
  margin-bottom: 5px;
}

.btn {
  width: 100%; /* Full width of the form */
  font-size: 18px;
  padding: 10px;
  border: none;
  border-radius: 8px;
  background-color: #151E3D;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s; /* Smooth transition for hover effect */
}

.btn:hover {
  background-color: #2a346d; /* Slightly darker on hover */
}

/* Hide left and right sections, or repurpose them if needed */
.left, .right {
  display: none;
}

/* Add your additional styles here */


</style>

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
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0; /* Reset default padding */
  overflow-x: hidden; /* Prevent horizontal scroll */
}

main {
  display: flex;
  flex-direction: column; /* Stack children vertically */
  justify-content: center;
  align-items: center;
  padding-top: 60px; /* Height of header */
  padding-bottom: 60px; /* Height of footer */
  flex-grow: 1; /* Allow main content to grow and fill space */
  background-image: url('C:\Users\archi\Downloads\UCONNLOGIN.jpg'); /* Add your local path here */
  background-size: cover;
  background-position: center;
  background-attachment: fixed; /* Background stays fixed during scroll */
}

.middle {
  margin-top: 95px;
  width: 30%; /* Adjust width as needed */
  background-color: rgba(255, 255, 255, 0.70); /* Semi-transparent background */
  padding: 40px;
  border-radius: 15px; /* Rounded corners for the form */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

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

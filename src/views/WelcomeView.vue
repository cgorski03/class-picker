<template>
  <main> 
    <div class = "left">
      <img class = "welcomeImg" src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
    </div>

    <div class = "middle">
      <h2 class = "title">Welcome Huskies</h2>
      
      <h2 class = "title2">Choose an Option Below</h2>
      
      <button class="btn" v-on:click.prevent="toLogin(true)">
        <h4>Student</h4>
      </button>
      <button class="btn" v-on:click.prevent="toLogin(false)">
        <h4>Teacher</h4>
      </button>
    </div>

    <div class = "right">
     <img class = "welcomeImg" src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
    </div>

  </main>
</template>

<script setup>

import versionState from '../state/version';
import { useRouter } from 'vue-router';

const router = useRouter();

let toLogin = (isStudentButtonPressed) => {

  console.log("isStudentButtonPressed: " + isStudentButtonPressed);
  versionState.setup(isStudentButtonPressed);
  console.log("student version cookie: " + versionState.getVersion.value);
  router.push('/login');
}

</script>

<style scoped>

main {
  display: flex;
  flex-direction:row;  
}

.welcomeImg {
  display: block;
  margin-top: 50px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50px;
}

.middle {
  margin-top: 95px;
  width: 34%; /* Adjust width as needed */
  margin-bottom: 35px;
  background-color: rgba(255, 255, 255, 0.70); /* Semi-transparent background */
  padding: 40px;
  border-radius: 15px; /* Rounded corners for the form */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.title, .title2 {
  background-color: transparent; /* Make the title backgrounds transparent */
  color: rgb(0, 0, 0);
  margin-bottom: 30px;
}

.btn {
  background-color: #151E3D;
  color: white;
  padding: 15px 60px; /* Adjust padding to your preference */
  margin-top: 20px;
  margin-bottom: 30px;
}

.btn h4 {
  color: rgb(255, 255, 255);
  text-align: center; /* Center the text in the buttons */
}

/* Additional styles for hover and active states on buttons if needed */
.btn:hover {
  background-color: rgba(211, 211, 211, 0.85); /* Semi-transparent on hover */
}

.btn:active {
  background-color: rgba(169, 169, 169, 0.85); /* Semi-transparent on active */
  transform: translateY(4px);
}

.left {
  width: 33%;
}

.right {
  width: 33%;
}

</style>
<template>
  <main> 
    <div class = "left">
      <img src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
    </div>

    <div class = "middle">
      <h2 class = "title">{{loginTitle}}</h2>
      <form name="login-form">

        <!-- Could add hover to input for clearner look down the road --->

        <div>
          <label for="username" class = "upText">Username</label>
          <input class = "upFormat" type="text" id="username" v-bind="username" />
        </div>
        <div>
          <label for="password" class = "upText">Password</label>
          <input class = "upFormat" type="password" id="password" v-bind="password" />
        </div>
        <button class="btn" type="submit" v-on:click.prevent="login()">
          Login
        </button>
      </form>
    </div>

   <div class = "right">
     <img src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
   </div>
   <!-- <h3>Output: {{ this.output }}</h3> --->
  </main>
</template>

<script setup>
import store from "../store/auth";
import versionState from '../state/version';
import { ref } from 'vue';
import {useRouter} from 'vue-router';

const router = useRouter();

//Can add a forgot password later on
const loginTitle = ref(versionState.getLoginTitle);

const prop = defineProps({
  username:String,
  password:String,
})


  const login = () => {
    //make sure username OR password are not empty
    if (prop.username != "" || prop.username != "") {
      console.log("Authentication complete");
      router.push('/home')
    } 
    else {
      alert("Username and password can not be empty");
    }
  }

</script>

<style>

main {
  display: flex;
  flex-direction:row;  
}

img {
  display: block;
  margin-top: 50px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: auto;
}

.middle {
  margin-top: 35px;
  width: 34%;
  margin-bottom: 35px;
  background-color: #151E3D;
}

.title {
  text-align: center;
  margin-bottom: 25px;
  font-size: 30px;
  font-weight: bold;
  background-color: #151E3D;
  color: white;
  padding: 25px;
}

.upFormat{
  margin-left: auto;
  margin-right: auto;
  font-size: 25px;
  display: block;
}

.upText {
  padding: 10px;
  margin-left: auto;
  margin-right: auto;
  display: block;
  color: White;
  font-weight: semi-bold;
  font-size: 25px;
  text-align: center;
}

.btn{
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 100px;
  display: block;
  color: Black;
  background-color: White;
  border: 2px solid Black;
  font-weight: bold;
  font-size: 20px; 
  padding: 10px 40px;
}

.btn:hover {
  background-color: Gray;
}

.loginButtonWriting {
  font-weight: bold;
  font-size: 20px; 
  padding: 15px 40px;
}

.left {
  width: 33%;
}

.right {
  width: 33%;
}

</style>
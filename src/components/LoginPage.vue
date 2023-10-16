<template>
  <main> 
    <div class = "left">
      <img src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
    </div>

    <div class = "middle">
      <h2 class = "title">{loginTitle}</h2>
      <form name="login-form">
        <div>
          <label for="username" class = "upText">Username</label>
          <input class = "upFormat" type="text" id="username" v-model="input.username" />
        </div>
        <div>
          <label for="password" class = "upText">Password</label>
          <input class = "upFormat" type="password" id="password" v-model="input.password" />
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

<script>
import { SET_AUTHENTICATION, SET_USERNAME } from "../util/storeconstants";
export default {
  name: 'LoginPage',
  props:{
    loginTitle: String
  },
  data() {
    return {
      input: {
        username: "",
        password: ""
      },
      output: "",
    }
  },
  methods: {
    login() {
      //make sure username OR password are not empty
      if (this.input.username != "" || this.input.username != "") {
        this.output = "Authentication complete"
        //stores true to the set_authentication and username to the set_username 
        this.$store.commit(`auth/${SET_AUTHENTICATION}`, true);
        this.$store.commit(`auth/${SET_USERNAME}`, this.input.username);
        this.output = "Authentication complete."
        this.$router.push('/home')
      } 
      else {
        this.$store.commit(`auth/${SET_AUTHENTICATION}`, false);
        this.output = "Username and password can not be empty"
      }
    },
  },
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
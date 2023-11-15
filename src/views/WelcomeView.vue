<template>
  <main> 
    <div class = "left">
      <img class = "welcomeImg" src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
    </div>

    <div class = "middle">
      <h2 class = "title">Welcome Huskies</h2>
      <template v-if="!isAuthenticated">
        <LoginButton />
      </template>
    </div>

    <div class = "right">
     <img class = "welcomeImg" src ="../assets/images/logo5.png" alt="HusckyLogo" width="320" height="400">
    </div>

  </main>
</template>

<script setup>
import LoginButton from '@/components/buttons/login-button.vue'
import { useAuth0} from '@auth0/auth0-vue';
import versionState from '../state/version';
import { useRouter } from 'vue-router';

const { isAuthenticated } = useAuth0();
const router = useRouter();

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
  margin-top: 35px;
  width: 34%;
  margin-bottom: 35px;
  background-color: #151E3D;
}

.title {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  background-color: #151E3D;
  color: white;
  margin-bottom: 30px;
}

.title2 {
  text-align: center;
  font-size: 25px;
  font-weight: semi-bold;
  background-color: #151E3D;
  color: white;
}

.btn{
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  display: block;
  background-color: White;
  border: 2px solid Black;
  padding: 30px 90px;
}

.btn h4{
  text-align: left;  
  font-weight: bold;
  font-size: 20px; 
  color: Black;
}

.btn:hover {
  background-color: #D3D3D3;
}

.btn:active {
  background-color: Gray;
  transform: translateY(4px);
}

.left {
  width: 33%;
}

.right {
  width: 33%;
}

</style>
<template>
  <main>
    <div class = "menuContent">
      <MainMenu/>
    </div>

    <div class = "mainContent">
      <div class="home">
        <div class = "formatText">
          <h2>Welcome, {{user.nickname}}!</h2>
        </div>
        <div class = "formatImage">
          <!-- Need to fix so it resizes and works on different display -->
          <img src ="../assets/images/logo6.jpg" alt="HusckyLogo" width="550" height="366">
        </div>
      </div>
    </div>

  </main>
</template>

<script setup>
import { routerKey } from "vue-router";
import MainMenu from "../components/MainMenu.vue";
import versionState from "../state/version";
import { useRouter } from 'vue-router';
import { useAuth0 } from "@auth0/auth0-vue";

const { user } = useAuth0();
const { isAuthenticated } = useAuth0();
if(!isAuthenticated){
  const router = useRouter();
  router.push('/');
}

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

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
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
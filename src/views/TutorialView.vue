<template>
  <main>
    <div class="menuContent">
      <MainMenu />
    </div>

    <div class="mainContent">
      <div class="home">
        <div style="height: fit-content">
          <h2>Tutorial</h2>
        </div>
        <div id="undertitle">
          <div id="tutorialstart">
            <p style="color: white; font-size: 25px; margin-bottom: 50px">
              Welcome to the {{ versionName }} Tutorial, Lets get started!
            </p>
            <button
              style="padding: 20px 40px; border-radius: 50px; font-weight: 500">
              Continue
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import MainMenu from "../components/MainMenu.vue";
import versionState from "../state/version";
import { ref } from "vue";

let versionName = ref("");

if (versionState.getVersion.value) {
  versionName.value = "student";
} else {
  versionName.value = "teacher";
}
</script>
<style scoped>
#undertitle {
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
#tutorialstart {
  height: 300px;
  width: 600px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 100px;
  background-color: #151e3d;
}
.home {
  height: 100vh;
  width: 100%;
  padding: 0;
  display: flex;
  flex-direction: column;
}

.home h2 {
  text-align: center;
  font-size: 1.5rem;
  background-color: #151e3d;
  color: white;
  padding: 25px;
}

.menuContent {
  width: 20%;
  background-color: #b90e0a;
  border: 2px black;
}

.mainContent {
  width: 80%;
  height: 100%;
}

main {
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: row;
}
</style>

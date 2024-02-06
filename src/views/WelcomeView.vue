<template>
  <main>
    <div class="left">
      <img
        class="welcomeImg"
        src="../assets/images/logo5.png"
        alt="HusckyLogo"
        width="320"
        height="400" />
    </div>

    <div class="middle">
      <h2 class="title">Welcome Huskies</h2>
      <template v-if="!isAuthenticated">
        <LoginButton />
      </template>
      <template v-if="isAuthenticated">
        <ContinueButton />
      </template>
    </div>

    <div class="right">
      <img
        class="welcomeImg"
        src="../assets/images/logo5.png"
        alt="HusckyLogo"
        width="320"
        height="400" />
    </div>
  </main>
</template>

<script setup>
import LoginButton from "@/components/buttons/login-button.vue";
import { useAuth0 } from "@auth0/auth0-vue";
import versionState from "../state/version";
import { useRouter } from "vue-router";
import ContinueButton from "@/components/buttons/continue-button.vue";

const { isAuthenticated } = useAuth0();
const router = useRouter();
</script>

<style scoped>
main {
  display: flex;
  flex-direction: row;
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
  background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent background */
  padding: 40px;
  border-radius: 15px; /* Rounded corners for the form */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.title,
.title2 {
  background-color: transparent; /* Make the title backgrounds transparent */
  color: rgb(0, 0, 0);
  margin-bottom: 30px;
}

.btn {
  background-color: #151e3d;
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

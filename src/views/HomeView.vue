<template>
  <main>
    <div class="menuContent">
      <MainMenu />
    </div>

    <div class="mainContent">
      <div class="home">
        <div class="formatText">
          <h2>Welcome, {{ user.email }}!</h2>
        </div>
        <div class="formatImage">
          <!-- Need to fix so it resizes and works on different display -->
          <img
            src="../assets/images/UCONNHOMEPAGE.png"
            alt="HusckyLogo"
            width="1800"
            height="500" />
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { watch } from "vue";
import MainMenu from "../components/MainMenu.vue";
import { useRouter } from "vue-router";
import { useAuth0 } from "@auth0/auth0-vue";
import versionState from "../state/version";

const { user } = useAuth0();
const { isAuthenticated } = useAuth0();
const router = useRouter();

// Watch for changes in the user object
watch(user, (newUser) => {
  if (newUser && newUser.nickname) {
    // User information is available, perform actions as needed
    let isStudent =
      newUser["dev-qtfdl3mznfynnex6.us.auth0.com/type"] == "s" ? true : false; //setup isStudent
    let email = newUser.email;
    console.log(email);
    versionState.setup(isStudent, email);
  }
});
</script>
<style scoped>
.home {
  overflow: hidden;
  padding: 0;
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: #f5f5f5; /* Updated background color for a cleaner look */
}

/* Header styling */
.home h2 {
  text-align: center;
  font-size: 2rem; /* Keep the font size for emphasis */
  background-color: #151e3d; /* Updated to a more modern navy blue */
  color: white;
  padding: 1rem;
  margin-bottom: 20px; /* Add some space below the heading */
}

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.menuContent {
  height: 95%;
  width: 20%;
  background-color: #b90e0a; /* Updated to a softer shade of blue */
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
.formatText {
  height: auto;
}
.formatImage {
  height: auto;
}
</style>

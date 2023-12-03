<template>
    <main>
      <div class = "menuContent">
        <MainMenu/>
      </div>
  
      <div class = "mainContent">
        <div class="home">
          <div class = "formatText">
            <h2>Drop Classes</h2>
          </div>
          <div id ="tablediv">
            <DropClassTable/>
          </div>
        </div>
      </div>
  
    </main>
  </template>
  
  <script setup>
  import MainMenu from "../components/MainMenu.vue";
  import DropClassTable from "../components/DropClassTable.vue"
  
  </script>
  <style scoped>
  .home {
    overflow: hidden;
    padding: 0;
    display: flex;
    flex-direction: column;
    background-color: #F5F5F5; /* Updated background color for a cleaner look */
;
  }
  
  .home h2 {
  text-align: center;
  font-size: 2rem; /* Keep the font size for emphasis */
  background-color: #151E3D; /* Updated to a more modern navy blue */
  color: white;
  padding: 1rem;
  margin-bottom: -20px; /* Add some space below the heading */
}
  
  img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  
.menuContent {
  height: 95%;
  width: 20%;
  background-color: #B90E0A; /* Updated to a softer shade of blue */
  border-right: 1px solid #EAEAEA; /* Light border for separation */
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

  #tablediv{
  margin-top: 20px;
  margin-bottom: 20px;
  align-self: center;
  width: 90%;
  overflow: hidden;
  height: auto;
}
  
  </style>
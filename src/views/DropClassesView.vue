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

  #tablediv{
  margin-top: 20px;
  margin-bottom: 20px;
  align-self: center;
  width: 90%;
  overflow: hidden;
  height: auto;
}
  
  </style>
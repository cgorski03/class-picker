<template>
    <main>
      <div class = "menuContent">
        <MainMenu/>
      </div>
  
      <div class = "mainContent">
        <div class="home">
          <div class = "formatText">
            <h2>Add Classes</h2>
          </div>
          <div>
            <form class = "searchbar">
              <div id = "searchfield">
                <input type="text" placeholder="Seacrh by class name" id="className" v-model="className" />
              </div>
              <div id = "searchbutton">
                <button v-on:click.prevent="search"></button>
              </div>
            </form>
          </div>
          <div>
            <!--<ClassTable/>-->
          </div>
        </div>
      </div>
  
    </main>
  </template>
  
  <script setup>
  import MainMenu from "../components/MainMenu.vue";
  //import ClassTable from "../components/AddClassTable.vue";
  import { ref } from "vue"

  const className = ref("");

  const search = () => {
    //Implent fetch to get list of classes corresponding to name
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
  

  .searchbar {
    background-color: #151E3D;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-left: 60px;
    margin-right: 60px;
    padding: 30px;
    width: 90%;
    display: flex;
    flex-direction: row;
  }
  .searchbar #searchfield{
    margin-left: 120px;
    width: 75%;
  }

  
  .searchbar input{
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    font-size: 30px;
    display: block;
  }

  .searchbar input::placeholder{
    text-align: center;
    color: black;
    font-weight: 500;
  }
  .searchbar input:hover{
    background-color: lightgray;

  }

  .searchbar button{
    border-radius: 15%;
    background: url("../assets/images/search.webp") no-repeat scroll 0 0 transparent;
    background-size: 50px;
    color: #000000;
    cursor: pointer;
    padding: 25px 25px;
    border: 1px white;
  }

  .searchbar button:hover{
    background-color: grey;
  }

  .searchbar button:active{
    background-color: darkgray;
  }
  </style>
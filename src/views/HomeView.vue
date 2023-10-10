<template>
  <main class="home">
    <h2>{homePageTitle}</h2>
      <img id = "middle" src = "require('.\assets\images\logo2.jpg')" alt="HusckyLogo">
  </main>
</template>

<style>
.home {
  padding: 0rem;
  border: 1px solid Black;
  display: flex;
  flex-direction: column;
}

.home h2 {
  text-align: center;
  font-size: 1.5rem;
  padding: 12.5px;
  background-color: #151E3D;
  color: white;
}

#middle{
  width: 100%;
  height: 470px;      
  object-fit: none;  
  object-position: center; 
}


</style>

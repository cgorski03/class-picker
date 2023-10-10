<template>
  <main class="home">
    <div class = "formatText">
       <h2>{homePageTitle}</h2>
    </div>
    <div class = "formatImage">
      <img src ="../assets/images/logo6.jpg" alt="HusckyLogo" width="550" height="366">
    </div>
  </main>
</template>

<script setup>
  defineProps({
    homePageTitle: String
  })
</script>

<style>
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

</style>
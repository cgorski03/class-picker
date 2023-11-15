<template>
  <header class="app-header">
    <div>
      <h1>University of Connecticut Course Registration</h1>
    </div>
  </header>
</template>

<style>

/* give the header itself a background color, a border, and add some padding to the content */
.app-header {
  position: fixed; /* Make header stay at top */
  top: 0;
  left: 0;
  right: 0;
  background-color: #151E3D; /* Dark blue background */
  color: white !important; /* White text color */
  text-align: center;
  padding: 1rem;
  z-index: 1000; /* Ensure it's above other content */
}

.app-header h1 {
  margin: 0; /* Remove default margin */
  font-size: 1.6rem;
  font-weight: bold;
}

</style>

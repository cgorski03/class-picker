<template>
  <div class = "footer">
    <h3>For help contact techsupport@uconn.edu</h3>
  </div>
</template>
<script>
export default{
  name: "footer"
}
</script>

<style>
<<<<<<< HEAD
.footer {
  position: fixed; /* Make footer stay at bottom */
=======

.footer div{
  position: fixed;
  margin: 0;
>>>>>>> a32ed9be868e813bb6d501923f268c237b2275c1
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #151E3D; /* Dark blue background */
  color: white; /* Ensure text color is white */
  text-align: center;
  padding: 10px 0;
  border-top: 1px solid Black;
  z-index: 1000; /* Ensure it's above other content */
}

.footer h3 {
  margin: 0; /* Remove default margin */
  padding: 10px; /* Adjust padding to your preference */
}

</style>

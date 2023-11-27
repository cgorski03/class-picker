<template>
    <div class="loader">
    </div>
</template>

<style>
.loader {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.75s, visibility 0.75s;
}

.loader::after {
  content: "";
  width: 75px;
  height: 75px;
  border: 15px solid #151e3d;
  border-top-color: #B90E0A;
  border-radius: 50%;
  animation: loading 0.75s ease infinite;
}

@keyframes loading {
  from {
    transform: rotate(0turn);
  }
  to {
    transform: rotate(1turn);
  }
}

</style>
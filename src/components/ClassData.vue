<template>
  <button class="item" @click.prevent="addclass">
    <p>{{ classData.classTitle }} {{ classData.classCA }} {{ classData.classCANum }} {{ classData.classSubj }}</p>
  </button>
</template>

<script setup>

const props = defineProps({
  classData: {
    type: Object, // Assuming classData is an object
    required: true,
  },
});

const addclass = () => {
  // Where you can implement the logic to add the class to the user's classes table
};

</script>

<style scoped>
.item {
  border-bottom: 1px solid black;
  width: 80%;
  margin-right: auto;
  padding: 20px;
}

.item:hover {
  background-color: gray;
}

.item:active {
  background-color: darkgray;
}
</style>

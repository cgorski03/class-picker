<template>
  <button class="item" @click.prevent="addclass">
    <p>{{ classData.classSubj }} {{ classData.classCANum }} {{ classData.classTitle }}</p>
  </button>
</template>

<script setup>
import { ref } from 'vue';

const yourCurrentClassList = ref([])

const props = defineProps({
  classData: {
    type: Object, // Assuming classData is an object
    required: true,
  },
});

const emit = defineEmits("sendclass", yourCurrentClassList)

const addclass = async () => {
  // Where you can implement the logic to add the class to the user's classes table

  const url = "https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class"
  try{
    const response = await fetch(url, {
          method: "POST",
          body:JSON.stringify({
            "username": "jak19018",
            "course": props.classData.classTitle
          }),
          headers: {
          "Content-Type": "application/json"
          }        
    }
    )
    const responseText = await response.text();
    if(response.ok){
        console.log('Success:', result);
        console.log("You added the class");
        
        const responseData = JSON.parse(responseText);

        yourCurrentClassList.value = [];

        for (const key in responseData) {
          if (Object.hasOwnProperty.call(responseData, key)){
            yourCurrentClassList.value.push(item['CAT NBR']);
          }
        }   
        emit("sendclass", yourCurrentClassList.value)
    }
    else {
      console.log("Error response:", responseText);
    }
  }
  catch (error) {
    console.error("Error during fetch:", error);
  }
}
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

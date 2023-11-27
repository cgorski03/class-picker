<template>
  <button class="item" @click.prevent="addclass">
    <p style="color: black;">{{ classData.classTitle }} {{ classData.classCA }} {{ classData.classCANum }} {{ classData.classSubj }}</p>
  </button>
</template>

<script setup>
import { ref } from 'vue';
import { watch } from 'vue';
import { useAuth0 } from "@auth0/auth0-vue";

const yourCurrentClassList = ref([]);
// Watch for changes in the user object

//take in data from Class class
const props = defineProps({
  classData: {
    type: Object, // Assuming classData is an object
    required: true,
  },
});

const emit = defineEmits("sendclass", "toggleloader")

//add a class to user schedule and return the users current schedule
const addclass = async () => {

  yourCurrentClassList.value = [];
  emit("sendclass", yourCurrentClassList.value)
  emit("toggleloader");
  const url = "https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class"
  try{
    
    const response = await fetch(url, {
          method: "POST",
          body:JSON.stringify({
            "username": "cgorski03",
            "course": props.classData.classTitle
          }),
          headers: {
          "Content-Type": "application/json"
          }        
    }
    )
    const responseText = await response.text();
    if(response.ok){
        console.log("You added the class");
        
        //Parsing through the response text to get string list of class names
        const responseData = JSON.parse(responseText);

        //reseting list to empty for the next time you add a class
       
        yourCurrentClassList.value =responseData;
        emit("toggleloader");
        emit("sendclass", yourCurrentClassList.value);
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
  width: 100%;
  padding: 20px;
}

.item:hover {
  background-color: gray;
}

.item:active {
  background-color: darkgray;
}
</style>

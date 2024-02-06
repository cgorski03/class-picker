<template>
  <course_symbol
    :isCompatible="classData.isCompatible"
    :course="classData.conflictingCourse"></course_symbol>
  <dropdown
    @addclass="addclass"
    :course="classData"
    :isStudent="versionState.getVersion.value"
    :addClass="true"
    class="item"
    style="position: relative">
  </dropdown>
</template>

<script setup>
import { ref } from "vue";
import versionState from "../state/version";
import course_symbol from "./addclasses/course_symbol.vue";
import dropdown from "./dropdown.vue";
const yourCurrentClassList = ref([]);
const emit = defineEmits(["sendclass", "toggleloader", "refresh"]);

//take in data from Class class
const props = defineProps({
  classData: {
    type: Object, // Assuming classData is an object
    required: true,
  },
});

//add a class to user schedule and return the users current schedule
const addclass = async () => {
  yourCurrentClassList.value = [];
  emit("sendclass", yourCurrentClassList.value);
  emit("toggleloader");
  const url =
    "https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class";

  try {
    if (!props.classData.isCompatible) {
      throw new Error(
        "This class is not compatible with ",
        props.classData.conflictingCourse
      );
    }
  } catch (error) {
    alert(
      "This class is not compatible with " +
        props.classData.conflictingCourse +
        ". Please edit your schedule and try again."
    );
    emit("toggleloader");
    return;
  }
  try {
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        username: versionState.getuserID.value,
        course: props.classData.classTitle,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const responseText = await response.text();
    if (response.ok) {
      console.log("You added the class");

      //Parsing through the response text to get string list of class names
      const responseData = JSON.parse(responseText);

      //reseting list to empty for the next time you add a class

      yourCurrentClassList.value = responseData;
      emit("toggleloader");
      emit("sendclass", yourCurrentClassList.value);
      emit("refresh");
    } else {
      console.log("Error response:", responseText);
      console.log(versionState.getuserID.value);
    }
  } catch (error) {
    console.error("Error during fetch:", error);
  }
};
</script>

<style scoped>
.item {
  margin: auto;
  padding: 5px;
  width: 90%;
}
</style>

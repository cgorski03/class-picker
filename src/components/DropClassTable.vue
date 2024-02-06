<template>
  <div id="droptableborder">
    <div id="droptableLayout">
      <nav>
        <ul>
          <Loading v-if="isLoading" />
          <li v-for="course in classlist" :key="course">
            <div id="indivisualCourse">
              <label class="container">
                {{ course }}
                <input
                  type="checkbox"
                  v-model="selectedCourses"
                  :value="course" />
                <span class="checkmark"></span>
              </label>
            </div>
          </li>
        </ul>
      </nav>
    </div>
  </div>
  <div id="dropclassdiv">
    <button id="dropclassbutton" @click="dropSelectedClasses">
      <h4 style="color: white">Drop Selected Classes</h4>
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import versionState from "../state/version";
import Loading from "./Loading.vue";

let classlist = ref([]);
let selectedCourses = ref([]);
let isLoading = ref(false);

const fetchData = async (username) => {
  isLoading.value = true;
  try {
    const response = await fetch(
      `https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class?username=${username}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (response.ok) {
      const data = await response.json();
      classlist.value = data;
    } else {
      console.error(
        "Error fetching data:",
        response.status,
        response.statusText
      );
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
  isLoading.value = false;
};

const dropSelectedClasses = async () => {
  isLoading.value = true;
  classlist.value = [];
  const username = versionState.getuserID.value;

  try {
    for (const course of selectedCourses.value) {
      const response = await fetch(
        "https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class",
        {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username,
            course: course,
          }),
        }
      );

      if (!response.ok) {
        console.error(
          "Error dropping class:",
          response.status,
          response.statusText
        );
        const errorData = await response.json();
        console.error("Error message:", errorData);
        throw new Error(
          `Failed to drop class. HTTP status: ${response.status}`
        );
      }

      // Handle successful response for each course, if needed
      console.log(`Class '${course}' dropped successfully`);
    }

    // You might want to refetch data after dropping classes
    await fetchData(username);
  } catch (error) {
    console.error("Error dropping classes:", error.message);
  }
  isLoading.value = false;
};

// Call the Lambda function when the component is mounted
onMounted(() => {
  const username = versionState.getuserID.value;
  fetchData(username);
});
</script>

<style>
#dropclassdiv {
  width: auto;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

#dropclassbutton {
  display: block;
  padding: 20px 40px;
  background-color: #151e3d; /* Button background color */
  color: white; /* Button text color */
  border: none; /* Remove default border */
  cursor: pointer; /* Change cursor to pointer on hover */
  border-radius: 4px; /* Rounded corners */
}

#droptableLayout {
  margin: auto;
  height: 100%;
  width: 94%;
  background-color: #f5f5f5; /* Updated to match Add Classes */
  display: flex;
  flex-direction: column;
  overflow: auto;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

#droptableborder {
  padding-top: 3%;
  padding-bottom: 3%;
  height: 71vh;
  width: 100%;
  background-color: #ffffff; /* Updated to match Add Classes header */
  color: white; /* Text color for header */
}

/* The container */
.container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-top: 10px;
  margin-left: 10px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 22px;
  user-select: none;
}

/* Hide the browser's default checkbox */
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
  background-color: #ccc;
}

/* When the checkbox is checked, add a blue background */
.container input:checked ~ .checkmark {
  background-color: #2196f3;
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.container input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark/indicator */
.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

#indivisualCourse {
  background-color: #151e3d;
  padding: 10px;
  margin-bottom: 5px;
  border-bottom: 1px solid #e0e0e0; /* Consistent border color */
}
</style>

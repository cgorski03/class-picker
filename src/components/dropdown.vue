<template>
  <div class="course-dropdown">
    <div class="course-header" @click="toggleDropdown">
      <span class="arrow">{{ showDropdown ? '▼' : '▶' }} {{ course.classTitle }}</span> 
    </div>

    <div v-if="showDropdown"
      :class="{ addclasses: addClass }"
      class="course-details"
      @click="emitAddClassSignal">
      <p><strong>{{ course.classSubj }} {{ course.classCANum }} {{ course.classTitle }}</strong> {{ course.teacher }}</p>
      <p>Meeting Time: {{ course.startTime }} - {{ course.endTime }} on {{ convertToFullDays(course.daysMeet) }}</p>
      <div v-if="!isStudent">
        <p><strong>Student Roster: </strong></p>
        <p v-for="student in getStudentList(course.studentList)" :key="'student'">
          {{ student }}
        </p>
      </div>
      <div v-else>
      </div>
      <ul>
        <li v-for="student in course.students" :key="student">{{ student }}</li>
      </ul>
    </div>
  </div>
</template>


<script>

import versionState from '../state/version';
import {ref} from 'vue'
export default {
  emits: ['addClass'], // change to PascalCase for consistency
  props: {
    course: {
      type: Object,
      required: true,
    },
    isStudent: {
      type: Boolean,
      required: true,
    },
    addClass: {
      type: Boolean,
      required: false,
      default: false,
    },
  },

  data() {
    return {
      showDropdown: this.addClass,
    };
  },
  methods: {
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    convertToFullDays(abbreviatedDays) {
      if (abbreviatedDays === 'TR') {
        return "Tuesday, Thursday";
      }
      if (abbreviatedDays === 'MW') {
        return "Monday, Wednesday";
      } 
      if (abbreviatedDays === 'MWF') {
        return "Monday, Wednesday, Friday";
      }
    },
    emitAddClassSignal() {
      if (this.addClass) {
        this.$emit('addclass'); // use this.$emit to emit the event
        console.log("Click worked");
      }
    },

    getStudentList(rosterList) {
      return rosterList.filter(name => name !== versionState.getuserID.value);
    },
  },
};

</script>

<style >

.addclasses:hover{
  background-color: #bdc3c7;
  cursor: pointer;
}
.course-dropdown {
  margin-bottom: 15px;
}

.course-header {
  cursor: pointer;
  background-color: #3A3B3C;
  color: white;
  padding: 10px;
  border-radius: 5px 5px 0 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.arrow {
  margin-right: 8px;
}

.course-details {
  background-color: #ecf0f1;
  border: 1px solid #bdc3c7;
  border-top: none;
  padding: 15px;
  border-radius: 0 0 5px 5px;
}

.course-details p {
  margin-bottom: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul li {
  margin-bottom: 5px;
}
</style>

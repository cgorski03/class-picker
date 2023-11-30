<template>
  <div class="course-dropdown">
    <div class="course-header" @click="toggleDropdown">
      <span class="arrow">{{ showDropdown ? '▼' : '▶' }} {{ course.classTitle }}</span> 
    </div>

    <div v-if="showDropdown" class="course-details">
      <p><strong>{{ course.classSubj }} {{ course.classCANum }} {{ course.classTitle }}</strong> {{ course.teacher }}</p>
      <p>Meeting Time: {{ course.startTime }} - {{ course.endTime }} on {{ convertToFullDays(course.days_meet) }}</p>
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

export default {
  props: {
    course: {
      type: Object,
      required: true,
    },
    isStudent: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      showDropdown: false,
    };
  },
  methods: {
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    convertToFullDays(abbreviatedDays) {
      if (abbreviatedDays == 'TR') {
        return "Tuesday, Thursday";
      }
      if (abbreviatedDays == 'MW') {
        return "Monday, Wednesday";
      } else {
        return "Monday, Wednesday, Friday";
      }
    },

    getStudentList(rosterList) {
      return rosterList.filter(name => name !== versionState.getuserID.value);
    },
  },
};
</script>

<style scoped>
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

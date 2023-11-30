import { ref } from "vue";
export class Class {
    constructor(classTitle, classCA, classCANum, classSubj, daysMeet, startTime, endTime) {
      this.classTitle = classTitle;
      this.classCA = classCA;
      this.classCANum = classCANum;
      this.classSubj = classSubj;
      this.daysMeet = daysMeet;
      this.startTime = startTime;
      this.endTime = endTime;
      this.isCompatible = ref(false);
      this.conflictingCourse = ref('');
      this.studentList = ref([])
    }
  }
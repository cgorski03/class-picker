import { reactive, computed } from "vue";

const state = reactive({
  isStudent: false,
  loginTitle: "",
  homePageTitle: "",
});

function toggleVersion() {
  console.log("Changed version");
  state.isStudent = !state.isStudent;
  changeVersionAspects(state);
}

function changeVersionAspects(state){
  if(state.isStudent){
    state.loginTitle = "Student Page";
    state.homePageTitle = "Welcome to the Student Home Page";
  }
  else{
    state.loginTitle = "Teacher Page";
    state.homePageTitle = "Welcome to the Teacher Home Page";
  }
}

const getVersion = computed(() => state.isStudent);
const getLoginTitle = computed(() => state.loginTitle);
const getHomePageTitle = computed(() => state.homePageTitle);

export default {
  state,
  toggleVersion,
  getVersion,
  getLoginTitle,
  getHomePageTitle,
};
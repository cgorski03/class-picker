import { reactive, computed } from "vue";

//Need to implement state staving to local storage, so users can refresh page and the state they were at will be saved
//Could do this using cookies

const state = reactive({
  isStudent: false,
  loginTitle: "",
  homePageTitle: "",
  menuOptions: [{option:"Tutorial", id:1}, {option:"View Schedule", id:2}, {option: "Sign Out", id:3}],
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
    state.menuOptions = [
      {option: "Tutorial", id:1}, 
      {option: "Add Classes", id:4}, 
      {option: "Drop Classes", id:5}, 
      {option: "View Schedule", id:2}, 
      {option: "Sign Out", id:3}
    ];
  }
  else{
    state.loginTitle = "Teacher Page";
    state.homePageTitle = "Welcome to the Teacher Home Page";
    menuOptions=  [
      {option:"Tutorial", id:1}, 
      {option:"View Schedule", id:2}, 
      {option: "Sign Out", id:3}
    ];
  }
}

const getVersion = computed(() => state.isStudent);
const getLoginTitle = computed(() => state.loginTitle);
const getHomePageTitle = computed(() => state.homePageTitle);
const getMenuOptions = computed(() => state.menuOptions);

export default {
  getMenuOptions,
  state,
  toggleVersion,
  getVersion,
  getLoginTitle,
  getHomePageTitle,
};
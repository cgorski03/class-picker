import { ref, computed } from "vue";

const state = ref({
  //did a student or teacher log in
  isStudent: ref(false),

  //Menu options state that is equal to a list of options based on student or teacher state
  menuOptions: JSON.parse(localStorage.getItem("key")) || [],
});

function setup(isStudentButtonPressed) {
  state.value.isStudent = isStudentButtonPressed;
  state.value.menuOptions = isStudentButtonPressed
    ? [
        { option: "Add Classes", id: 4, path:"/addclasses" },
        { option: "Drop Classes", id: 5, path:"/dropclasses" },
        { option: "View Schedule", id: 2, path:"/schedule" },
        { option: "Sign Out", id: 3, path:"/" },
      ]
    : [
        { option: "View Schedule", id: 2, path:"/schedule" },
        { option: "Sign Out", id: 3, path:"/" },
      ];

  let string = JSON.stringify(state.value.menuOptions);
  localStorage.setItem("key", string);

}

function clearLocalStorage() {

  localStorage.removeItem("key");
}

const getVersion = computed(() => state.value.isStudent);
const getMenuOptions = computed(() => state.value.menuOptions);
const getLoginTitle = computed(() => state.value.isStudent ? "Student Login" : "Teacher Login");
const getHomePageTitle = computed(() => state.value.isStudent ? "Welcome to the Student Home Page" : "Welcome to the Teacher Home Page");


export default {
  setup,
  clearLocalStorage,
  getMenuOptions,
  state,
  getVersion,
  getLoginTitle,
  getHomePageTitle,
};

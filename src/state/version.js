import { ref, computed } from "vue";

const state = ref({
  isStudent: ref(false),
  menuOptions: JSON.parse(localStorage.getItem("key")) || [],
});

function setup(isStudentButtonPressed) {
  state.value.isStudent = isStudentButtonPressed;
  state.value.menuOptions = isStudentButtonPressed
    ? [
        { option: "Tutorial", id: 1, path:"/tutorial" },
        { option: "Add Classes", id: 4, path:"/addclasses" },
        { option: "Drop Classes", id: 5, path:"/dropclasses" },
        { option: "View Schedule", id: 2, path:"/schedule" },
        { option: "Sign Out", id: 3, path:"/" },
      ]
    : [
        { option: "Tutorial", id: 1, path:"/tutorial" },
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

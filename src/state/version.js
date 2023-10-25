import { ref, computed } from "vue";

const state = ref({
  isStudent: ref(false),
  menuOptions: JSON.parse(localStorage.getItem("key")) || [],
});

function setup(isStudentButtonPressed) {
  state.value.isStudent = isStudentButtonPressed;
  state.value.menuOptions = isStudentButtonPressed
    ? [
        { option: "Tutorial", id: 1 },
        { option: "Add Classes", id: 4 },
        { option: "Drop Classes", id: 5 },
        { option: "View Schedule", id: 2 },
        { option: "Sign Out", id: 3 },
      ]
    : [
        { option: "Tutorial", id: 1 },
        { option: "View Schedule", id: 2 },
        { option: "Sign Out", id: 3 },
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

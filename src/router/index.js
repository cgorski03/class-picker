// this file creates the router instance that is used by our application

// we start by importing the createRouter and createWebHistory functions, as well as the components describing each of our views
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import FormView from "../views/FormView.vue";
import FetchView from "../views/FetchView.vue";

import LoginView from "../views/LoginView.vue";
import MainMenu from "../components/MainMenu.vue";
import WelcomeView from "../views/WelcomeView.vue";
import AddClasses from "../views/AddClassesView.vue";
import DropClasses from "../views/DropClassesView.vue";
import Schedule from "../views/ScheduleView.vue";
import TutorialView from "../views/TutorialView.vue"; // Use TutorialView if it's the correct component
import { useAuth0 } from "@auth0/auth0-vue"; // Include if Auth0 authentication is required

// ... Rest of your router setup



const router = createRouter({
  // the history mode determines how vue router interacts with the url.
  // createWebHistory() simulates the default browser behavior of changing
  // the path of the url based on the current document.
  // import.meta.env.BASE_URL is a vite feature that you don't need to worry about
  // and can safely use. it refers to the current path to the directory being
  // served by vite, which in this project is always the same directory
  // (and therefore import.meta.env.BASE_URL is '/')
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',

  // each entry to this routes array has a path (what goes in the URL to access
  // this page), a name (check out components/AppHeader.vue for how this is used)
  // and, most importantly, the component that should be rendered for the view
  routes: [
    {
      path: "/",
      name: "welcome",
      component: WelcomeView,
     },
     {
      path: "/addclasses",
      name: "addclasses",
      component: AddClasses,
     },
     {
      path: "/dropclasses",
      name: "dropclasses",
      component: DropClasses,
     },
     {
      path: "/schedule",
      name: "schedule",
      component: Schedule,
     },
    {
      path: "/login",
      name: "login",
      component: LoginView,
     },
    {
      path: "/home",
      name: "home",
      component: HomeView,
    },
    {
      path: "/form",
      name: "form",
      component: FormView,
    },
    {
      path: "/fetch",
      name: "fetch",
      component: FetchView,
    },
    {
      path: "/tutorial",
      name: "tutorial",
      component: TutorialView,
    },
  ],
});

// Navigation guard
router.beforeEach((to, from, next) => {
  const { isAuthenticated } = useAuth0();
  // Check if the route requires authentication
    // Check if the user is authenticated
    if (!isAuthenticated.value && to.path != '/' && to.path != '/home') {
      alert("You are not authorized to access this page. Please log in first.")
      // Redirect to the login page or any other appropriate action
      next('/');
  } else {
    // Continue with the navigation
    next();
  }
});
export default router;

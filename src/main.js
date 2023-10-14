import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import util from "./util";

const app = createApp(App);

app.use(router);
app.use(util);
app.mount("#app");

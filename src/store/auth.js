import { createStore } from 'vuex';

export default createStore({
    namespaced: true,
    state: {
        username: "",
        password: "",
        authenticated: "",
    },
    getters: {
        username: state => state.username,
        password: state => state.password,
        authenticated: state => state.authenticated,
    },
    actions: {

    },
    mutations: {
        login(usernameInput, passwordinput){
            state.authenticated = true;
        },
    }
})
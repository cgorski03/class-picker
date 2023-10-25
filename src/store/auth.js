import { createStore } from 'vuex';
//const AWS = require('aws-sdk@2.1480.0');

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
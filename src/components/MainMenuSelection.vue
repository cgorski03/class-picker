<template>
    <button class = "item" v-on:click.prevent="navigate">
        <h4>{{name}}</h4>
    </button>
</template>

<script setup>
import { useRouter } from 'vue-router'
import versionState from '../state/version'
import { useAuth0} from '@auth0/auth0-vue';
const { logout } = useAuth0();

const router = useRouter();

const props = defineProps({
    name:String,
    path:String,
})

//routes on button click to corresponding path 
const navigate = () => {

  if(props.name === "Sign Out"){
    console.log("registering button ppress");
    logout({
        logoutParams: {
            returnTo: window.location.origin
        },
    });
  }

  router.push(props.path);
}
</script>


<style scoped>
.item {
    border-bottom: 1px solid Black;
    width: 100%;
    margin-right: auto;
    padding: 20px;
    background-color: #B90E0A;
}

h4{
  color: White;
  font-weight: bold;
  font-size: 1rem;
  text-align: left;
}

.item:hover{
  background-color: #BC544B;
}

.item:active{
  background-color: #900603;
}
</style>
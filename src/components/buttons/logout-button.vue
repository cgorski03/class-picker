<template>
    <button class="btn" @click="handleLogout">Log In</button>
</template>

<script setup>
import { useAuth0} from '@auth0/auth0-vue';
const { logout } = useAuth0();

const handleLogout = () => {
    logout({
        logoutParams: {
            returnTo: window.location.origin
        },
    });
};
</script>
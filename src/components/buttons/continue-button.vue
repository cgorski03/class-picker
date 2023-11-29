<template>
    <button class="btn" @click="redirect">Continue</button>
</template>

<script setup>
import {useRouter} from 'vue-router';

const router = useRouter();

const redirect = () => {
    router.push('/home')
};
</script>
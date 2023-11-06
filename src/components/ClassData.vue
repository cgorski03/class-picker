<template>
    <button class = "item" v-on:click.prevent="addclass">
        <p>{{classTitle}}   {{ classCA }}   {{ classCANum }}    {{ classSubj }}</p>
    </button>
</template>

<script setup>

const props = defineProps({
    classTitle:String,
    classCA:String,
    classCANum:String,
    classSubj:String,
})

const addclass = () => {
// where we will actually add class to user classes table

}

</script>


<style scoped>
.item {
    border-bottom: 1px solid Black;
    width: 80%;
    margin-right: auto;
    padding: 20px;
}

.item:hover{
  background-color: gray;
}

.item:active{
  background-color: darkgray;
}
</style>
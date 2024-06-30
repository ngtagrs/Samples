<script setup>
import { ref } from 'vue'

const count=ref(0)
function countUp(){
    count.value++
}
</script>

<template>
    <p>{{ count }}</p>
    <button @click="countUp">button</button>
</template>
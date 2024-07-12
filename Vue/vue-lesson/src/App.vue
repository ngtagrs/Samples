<script setup>
import { ref, computed } from 'vue'
const score = ref(0)
const evaluation = computed(() => {
    return score.value > 3 ? 'Good' : 'Bad'
})
</script>

<template>
    <p>{{ score > 3 ? 'Good' : 'Bad' }}</p>
    <p>{{ evaluation }}</p>
    <p>{{ score }}</p>
    <button @click="score++">+1</button>
</template>
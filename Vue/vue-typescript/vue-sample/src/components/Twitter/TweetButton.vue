<script setup lang="ts">
import { inject } from "vue"

const emits = defineEmits<{
  (e: "submit"): void;
}>();

const onSubmit = () => {
  emits("submit");
};

//const userName = "John Doe";
const userName = inject<string>("username")
</script>

<template>
  <div class="tweet-button">
    <button @click="onSubmit">Tweet</button>
    <span>as</span>
    <span>{{ userName }}</span>
  </div>
</template>

<style scoped>
.tweet-button {
  display: flex;
  gap: 1rem;
  align-items: center;
  border-bottom: 4px solid #ffc0c0;
}

.profile {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}
</style>

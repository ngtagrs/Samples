<script setup lang="ts">
import { Tweet } from "@/types/tweet";

const props = defineProps<{
  tweet: Tweet;
}>();

const emits = defineEmits<{
  (e: "delete", id: string): void;
}>();

const onDelete = (id: string) => {
  emits("delete", id);
};
</script>

<template>
  <div class="tweet">
    <span>{{ props.tweet.description }}</span>
    <button @click="() => onDelete(tweet.id)">Delete</button>
  </div>
</template>

<style scoped>
.tweet {
  background-color: #f5f5f5;
  padding: 1rem;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  button {
    background-color: #ff0000;
    color: #fff;
    border-radius: 4px;
    border: none;
    padding: 0.5rem;
    cursor: pointer;
  }
}
</style>

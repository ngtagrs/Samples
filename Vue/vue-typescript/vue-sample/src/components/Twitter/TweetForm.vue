<script setup lang="ts">
import { ref } from "vue";
import { Tweet } from "@/types/tweet";
import TweetButton from "./TweetButton.vue";
const tweet = ref<Tweet>({
  id: "",
  description: "",
});

const emits = defineEmits<{
  (e: "submit", value: string): void;
}>();

const onSubmit = () => {
  emits("submit", tweet.value.description);
  tweet.value = {
    id: "",
    description: "",
  };
};
</script>

<template>
  <div>
    <form @submit.prevent class="tweet-form">
      <textarea v-model="tweet.description"></textarea>
      <TweetButton @submit="onSubmit" />
    </form>
  </div>
</template>

<style scoped>
.tweet-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  textarea {
    width: 400px;
    height: 100px;
    border-radius: 4px;
  }
  button {
    width: 100px;
    height: 50px;
  }
  justify-content: center;
  align-items: center;
}
</style>

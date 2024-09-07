<script setup lang="ts">
import { ref, provide } from "vue";
import { Tweet } from "@/types/tweet";
import TweetFormComponent from "./TweetForm.vue";
import TweetList from "./TweetList.vue";
import UserModal from "./UserModal.vue";

const tweets = ref<Tweet[]>([
  {
    id: "1",
    description: "Hello!",
  },
  {
    id: "2",
    description: "Example",
  },
]);

const onSubmit = (description: string) => {
  tweets.value = [
    ...tweets.value,
    {
      id: Math.random().toString(),
      description,
    },
  ];
};

const onDelete = (id: string) => {
  tweets.value = tweets.value.filter((tweet) => tweet.id !== id);
};

const isOpenModal = ref<boolean>(false);
const userName = ref<string>("");

const closeUserModal = (username: string) => {
  userName.value = username;
  isOpenModal.value = false;
};

const username =ref("")
provide("username", "Jack")
</script>

<template>
  <div class="setting">
    <button @click="isOpenModal = !isOpenModal">Settings</button>
    {{ userName }}
  </div>
  <Teleport to="body">
    <UserModal :show="isOpenModal" :username="userName" @close="closeUserModal" />
  </Teleport>
  <h1>Twitter</h1>
  <TweetFormComponent @submit="onSubmit" />
  <TweetList :tweets="tweets" @delete="onDelete" />
</template>

<style scoped>
.setting {
  display: flex;
  flex-direction: column;
  font-size: 1.5rem;
  font-weight: bold;
  position: absolute;
  top: 20px;
  right: 20px;
}
</style>

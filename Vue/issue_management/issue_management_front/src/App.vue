
<script lang="ts" setup>
import router from './router';

 
</script>

<template>
  <v-app>
    <v-app-bar color="primary">
      <v-app-bar-title @click="() => router.push('/')">
        <span style="cursor: pointer;">Portal</span>
      </v-app-bar-title>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

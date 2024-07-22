<script setup lang="ts">

import { ref } from "vue";
import draggable from "vuedraggable";
import { useRouter } from "vue-router";
import IssueListMatrix from "../components/IssueListMatrix.vue";
import IssueListKanban from "../components/IssueListKanban.vue";
import Issue from "../assets/ts/Issue"


const router = useRouter();

const issues = ref([]);
const search = ref("");
const display_mode = ref("1");
const newIssueDialog = ref(false);
const newIssue = ref(new Issue());


const addNewIssue = () => {
    newIssueDialog.value = false
    issues.value.push(newIssue.value)
    newIssue.value = new Issue()
};

</script>


<template>
  <v-card flat>
    <v-card-title class="d-flex align-center pe-2">
      <v-icon icon="mdi-format-list-checkbox"></v-icon> &nbsp; Issue

      <v-dialog  v-model="newIssueDialog" max-width="400" persistent>
          <template v-slot:activator="{ props: activatorAddNewIssue }">
            <v-btn class="ml-5" icon="mdi-plus" v-bind="activatorAddNewIssue"></v-btn>
          </template>
          <v-card
            prepend-icon="mdi-map-marker"
            title="New Issue">
            <v-card-text>
                <v-text-field label="タイトル" required v-model="newIssue.title"></v-text-field>
                <v-textarea label="概要" v-model="newIssue.description"></v-textarea>
                <v-select label="分類" :items="['契約書', 'リスク管理']" v-model="newIssue.category"></v-select>
                <v-text-field label="担当者" v-model="newIssue.representative"></v-text-field>
            </v-card-text>

            <v-card-actions>
              <v-btn @click="addNewIssue()"> OK </v-btn>
              <v-btn @click="newIssueDialog = false"> Cancel </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

      <v-spacer></v-spacer>

      <v-radio-group inline v-model="display_mode">
        <v-radio label="Matrix" value="1"></v-radio>
        <v-radio label="Kanban" value="2"></v-radio>
      </v-radio-group>

      <v-spacer></v-spacer>

      <v-text-field
        v-model="search"
        density="compact"
        label="Search"
        prepend-inner-icon="mdi-magnify"
        variant="solo-filled"
        flat
        hide-details
        single-line
      ></v-text-field>
    </v-card-title>

    <v-divider></v-divider>
    <IssueListMatrix :issues="issues" :search="search" v-if="display_mode == '1'"/>
    <IssueListKanban :issues="issues" v-if="display_mode=='2'"/>
  </v-card>
</template>

<style scoped></style>

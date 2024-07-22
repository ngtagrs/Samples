<script setup lang="ts">
import Issue from "../assets/ts/Issue"
import { useRouter } from "vue-router";
import { ref } from "vue";

const router = useRouter();

type Props = {
  issues: Issue[];
  search: string;
};
const props = defineProps<Props>();

const headers = [
  { title: "タイトル", key: "title" },
  { title: "概要", key: "description" },
  { title: "分類", key: "category" },
  { title: "ステータス", key: "status" },
  { title: "担当者", key: "representative" },
  { title: "更新日", key: "last_updated_at" },
  { title: "作成日", key: "created_at" },
  { title: "Actions", key: "actions", sortable: false },
];
const dialog = ref(false);

const detailIssue = (issue: Issue) => {
  router.push({ name: "issue_detail", params: { id: issue.id }});
};
const deleteItem = (issue: Issue) => {
  dialog.value = false;
  const editedIndex = props.issues.indexOf(issue);
  if (editedIndex !== -1) {
    props.issues.splice(editedIndex, 1);
  }
};

</script>

<template>
    <v-data-table :headers="headers" :search="search" :items="issues">
      <template v-slot:item.actions="{ item }">
        <v-icon class="me-2" size="small" @click="detailIssue(item)">
          mdi-pencil
        </v-icon>
        <v-dialog v-model="dialog" max-width="400" persistent>
          <template v-slot:activator="{ props: activatorIsDeleteDialog }">
            <v-icon v-bind="activatorIsDeleteDialog" size="small"> mdi-delete </v-icon>
          </template>
          <v-card
            prepend-icon="mdi-map-marker"
            :text="item.title + 'を削除しますか?'"
            title="Delete"
          >
            <template v-slot:actions>
              <v-spacer></v-spacer>

              <v-btn @click="deleteItem(item)"> OK </v-btn>

              <v-btn @click="dialog = false"> Cancel </v-btn>
            </template>
          </v-card>
        </v-dialog>
      </template>
    </v-data-table>
</template>
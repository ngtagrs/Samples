<script setup lang="ts">
class Issue {
    id: number = 0;
  title: string = "";
  description: string = "";
  category: string = "";
  status: string = "未着手";
  representative: string = "";
  last_updated_at: Date = new Date();
  created_at: Date = new Date();

  work_logs: WorkLog[] = [];
  comments: Comment[] = [];
  files: File[] = [];

}
class WorkLog {
  title: string = "";
  description: string = "";
  files: File[] = [];
  worked_by: string = "";
  worked_at: Date = new Date();
}
class Comment {
  comment: string = "";
  files: File[] = [];
  commented_by: string = "";
  commented_at: Date = new Date();
}
class File {
  name: string = "";
  file_content: ArrayBuffer = new ArrayBuffer(0);
}

const issue = new Issue();
issue.id = 1;
issue.title = "SIMM年次バックテスト"
issue.description = "今のPositionを3年間保持したときのVaRがSIMMの値を超えないかを確認"

</script>

<template>
<v-card>
  <v-card-title>{{ issue.title }}</v-card-title>
  <v-card-text>
    {{ issue.description }}
  </v-card-text>
</v-card>
<v-card>
  <v-card-title>Comment</v-card-title>
</v-card>
<v-card>
  <v-card-title>作業ログ</v-card-title>
</v-card>
<v-card>
  <v-card-title>ファイル</v-card-title>
</v-card>
</template>

<style scoped>
</style>
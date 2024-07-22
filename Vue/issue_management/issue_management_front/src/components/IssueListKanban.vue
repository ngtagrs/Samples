<script setup lang="ts">
import draggable from "vuedraggable";
import Issue from "../assets/ts/Issue"
import { useRouter } from "vue-router";
import { ref, computed } from "vue";

const router = useRouter();

type Props = {
  issues: Issue[];
};
const props = defineProps<Props>();

const unmanaged_issues = computed(() => props.issues.filter(issue => issue.status=="未着手"))
const progressing_issues = computed(() => props.issues.filter(issue => issue.status=="進行中"))
const completed_issues = computed(() => props.issues.filter(issue => issue.status=="完了"))
const pending_issues = computed(() => props.issues.filter(issue => issue.status=="ペンディング"))

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
  <v-container>
    <v-row>
        <v-col>
            <v-card class="outer-card">
                <v-card-title>未着手</v-card-title>
                <v-divider></v-divider>
                <draggable v-model="unmanaged_issues" item-key="id" tag="ul" group="ISSUES">
                    <template #item="{ element }">
                        <v-card class="inner-card" elevated>
                            <v-card-title style="cursor: grab;">{{ element.title }}</v-card-title>
                            <v-divider></v-divider>
                            <v-card-text>{{ element.description }}</v-card-text>
                            <v-card-actions>
                                <v-icon class="me-2" size="small" @click="detailIssue(element)">
                                    mdi-pencil
                                </v-icon>
                                <v-dialog v-model="dialog" max-width="400" persistent>
                                    <template v-slot:activator="{ props: activatorIsDeleteDialog }">
                                        <v-icon v-bind="activatorIsDeleteDialog" size="small"> mdi-delete </v-icon>
                                    </template>
                                    <v-card
                                        prepend-icon="mdi-map-marker"
                                        :text="element.title + 'を削除しますか?'"
                                        title="Delete">
                                        <template v-slot:actions>
                                            <v-spacer></v-spacer>

                                            <v-btn @click="deleteItem(element)"> OK </v-btn>
                                            <v-btn @click="dialog = false"> Cancel </v-btn>
                                        </template>
                                    </v-card>
                                </v-dialog>
                            </v-card-actions>
                        </v-card>
                    </template>
                </draggable>
            </v-card>
        </v-col>

        <v-col>
            <v-card>
                <v-card-title>進行中</v-card-title>
                <v-divider></v-divider>
                <draggable v-model="progressing_issues" item-key="id" tag="ul" group="ISSUES">
                    <template #item="{ element }">
                        <v-card class="inner-card" elevated>
                            <v-card-title style="cursor: grab;">{{ element.title }}</v-card-title>
                            <v-divider></v-divider>
                            <v-card-text>{{ element.description }}</v-card-text>
                            <v-card-actions>
                                <v-icon class="me-2" size="small" @click="detailIssue(element)">
                                    mdi-pencil
                                </v-icon>
                                <v-dialog v-model="dialog" max-width="400" persistent>
                                    <template v-slot:activator="{ props: activatorIsDeleteDialog }">
                                        <v-icon v-bind="activatorIsDeleteDialog" size="small"> mdi-delete </v-icon>
                                    </template>
                                    <v-card
                                        prepend-icon="mdi-map-marker"
                                        :text="element.title + 'を削除しますか?'"
                                        title="Delete">
                                        <template v-slot:actions>
                                            <v-spacer></v-spacer>

                                            <v-btn @click="deleteItem(element)"> OK </v-btn>
                                            <v-btn @click="dialog = false"> Cancel </v-btn>
                                        </template>
                                    </v-card>
                                </v-dialog>
                            </v-card-actions>
                        </v-card>
                    </template>
                </draggable>
            </v-card>
        </v-col>
        <v-col>
            <v-card>
                <v-card-title>完了</v-card-title>
                <v-divider></v-divider>
                <draggable v-model="completed_issues" item-key="id" tag="ul" group="ISSUES">
                    <template #item="{ element }">
                        <v-card class="inner-card" elevated>
                            <v-card-title style="cursor: grab;">{{ element.title }}</v-card-title>
                            <v-divider></v-divider>
                            <v-card-text>{{ element.description }}</v-card-text>
                            <v-card-actions>
                                <v-icon class="me-2" size="small" @click="detailIssue(element)">
                                    mdi-pencil
                                </v-icon>
                                <v-dialog v-model="dialog" max-width="400" persistent>
                                    <template v-slot:activator="{ props: activatorIsDeleteDialog }">
                                        <v-icon v-bind="activatorIsDeleteDialog" size="small"> mdi-delete </v-icon>
                                    </template>
                                    <v-card
                                        prepend-icon="mdi-map-marker"
                                        :text="element.title + 'を削除しますか?'"
                                        title="Delete">
                                        <template v-slot:actions>
                                            <v-spacer></v-spacer>

                                            <v-btn @click="deleteItem(element)"> OK </v-btn>
                                            <v-btn @click="dialog = false"> Cancel </v-btn>
                                        </template>
                                    </v-card>
                                </v-dialog>
                            </v-card-actions>
                        </v-card>
                    </template>
                </draggable>
            </v-card>
        </v-col>
        <v-col>
            <v-card>
                <v-card-title>ペンディング</v-card-title>
                <v-divider></v-divider>
                <draggable v-model="pending_issues" item-key="id" tag="ul" group="ISSUES">
                    <template #item="{ element }">
                        <v-card class="inner-card" elevated>
                            <v-card-title style="cursor: grab;">{{ element.title }}</v-card-title>
                            <v-divider></v-divider>
                            <v-card-text>{{ element.description }}</v-card-text>
                            <v-card-actions>
                                <v-icon class="me-2" size="small" @click="detailIssue(element)">
                                    mdi-pencil
                                </v-icon>
                                <v-dialog v-model="dialog" max-width="400" persistent>
                                    <template v-slot:activator="{ props: activatorIsDeleteDialog }">
                                        <v-icon v-bind="activatorIsDeleteDialog" size="small"> mdi-delete </v-icon>
                                    </template>
                                    <v-card
                                        prepend-icon="mdi-map-marker"
                                        :text="element.title + 'を削除しますか?'"
                                        title="Delete">
                                        <template v-slot:actions>
                                            <v-spacer></v-spacer>

                                            <v-btn @click="deleteItem(element)"> OK </v-btn>
                                            <v-btn @click="dialog = false"> Cancel </v-btn>
                                        </template>
                                    </v-card>
                                </v-dialog>
                            </v-card-actions>
                        </v-card>
                    </template>
                </draggable>
            </v-card>
        </v-col>
    </v-row>
</v-container>
</template>

<style scoped>
v-card-title.title {
    cursor: grab;
}
li.title {
    cursor: pointer;
}
.outer-card {
    margin: 20px;
}
.inner-card {
    margin: 30px; 
}
</style>
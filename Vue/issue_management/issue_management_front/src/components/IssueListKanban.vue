<script setup lang="ts">
import draggable from "vuedraggable";
import Issue from "../assets/ts/Issue"
import { useRouter } from "vue-router";
import { ref, computed, watch } from "vue";

const router = useRouter();

type Props = {
  issues: Issue[];
};
const props = defineProps<Props>();

const isShowDialogs = ref({});
props.issues.forEach((issue: Issue) => { isShowDialogs.value[issue.id] = false})

let unmanaged_issues = ref(props.issues.filter(issue => issue.status=="未着手"))
let progressing_issues = ref(props.issues.filter(issue => issue.status=="進行中"))
let completed_issues = ref(props.issues.filter(issue => issue.status=="完了"))
let pending_issues = ref(props.issues.filter(issue => issue.status=="ペンディング"))
watch(props.issues, () =>{
    unmanaged_issues.value = props.issues.filter(issue => issue.status=="未着手")
    progressing_issues.value = props.issues.filter(issue => issue.status=="進行中")
    completed_issues.value = props.issues.filter(issue => issue.status=="完了")
    pending_issues.value = props.issues.filter(issue => issue.status=="ペンディング")
})

watch(unmanaged_issues, (newIssues, oldIssues) => {
    if (newIssues.length > oldIssues.length){
        const addedIssue: Issue = newIssues.filter(issue => !oldIssues.includes(issue))[0];
        addedIssue.status = "未着手";
    }
})
watch(progressing_issues, (newIssues, oldIssues) => {
    if (newIssues.length > oldIssues.length){
        const addedIssue: Issue = newIssues.filter(issue => !oldIssues.includes(issue))[0];
        addedIssue.status = "進行中";
    }
})
watch(completed_issues, (newIssues, oldIssues) => {
    if (newIssues.length > oldIssues.length){
        const addedIssue: Issue = newIssues.filter(issue => !oldIssues.includes(issue))[0];
        addedIssue.status = "完了";
    }
})
watch(pending_issues, (newIssues, oldIssues) => {
    if (newIssues.length > oldIssues.length){
        const addedIssue: Issue = newIssues.filter(issue => !oldIssues.includes(issue))[0];
        addedIssue.status = "ペンディング";
    }
})


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
            <v-card class="outer-card">
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
            <v-card class="outer-card">
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
            <v-card class="outer-card">
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
    margin-top: 20px;
}
.inner-card {
    margin: 30px; 
}
</style>
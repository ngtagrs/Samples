<script setup lang="ts">
import { Person } from "./Persons.vue"

type Props ={
    persons: Person[]
}
defineProps<Props>()

const emit = defineEmits(["delete"])
const onClickDelete = (id: number, name: string) =>{
    if(confirm("Delete " + name + "?")) {
        emit("delete", id)
    }
}
</script>

<template>
    <li v-for="person in persons" :key="person.id" class="person-list">
        <span>{{ person.name }}</span>
        <span>age:{{ person.age }}</span>
        <button>
            <span @click="onClickDelete(person.id, person.name)">delete</span>
        </button>
    </li>
</template>

<style scoped>

.person-list {
    list-style: none;
    margin-bottom: 12px;
    border-radius: 4px;
    font-size: 20px;
    display: flex;
    justify-content: space-between;
    background-color: rgb(228, 201, 133);
    padding: 8px 20px;
    width: 300px;
}

</style>
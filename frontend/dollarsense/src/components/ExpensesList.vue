<script setup lang="ts">
defineProps<{
  loading: boolean
  allExpenses: any
}>()
</script>

<template>
  <div>
    <!-- <p>ExpensesList</p> -->
    <p v-if="loading">loading...</p>
    <p
      v-else-if="allExpenses"
      class="text-blue-700"
      v-for="expense of allExpenses"
      :key="expense.title"
    >
      {{ expense.title }} {{ expense.amount }}
    </p>
  </div>
</template>

<!-- <style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style> -->

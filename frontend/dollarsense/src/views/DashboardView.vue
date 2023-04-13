<script lang="ts">
import TheWelcome from '../components/TheWelcome.vue'
import ExpensesList from '../components/ExpensesList.vue'
import { useQuery, useMutation } from '@vue/apollo-composable'
import { expenseQueryGql, addExpenseMutationGql } from '../graphql/queries'
import { ref, computed } from 'vue'

export default {
  setup() {
    const { mutate: addExpense, onDone: expenseAdded } = useMutation(addExpenseMutationGql)
    const {
      result,
      loading,
      refetch: refetchExpenses
    } = useQuery(
      expenseQueryGql,
      // variables
      null,
      // options
      () => ({
        fetchPolicy: 'cache-and-network'
      })
    )
    const allExpenses = computed(() => result.value?.allExpenses ?? [])
    console.log('[Home] result: ', allExpenses)
    expenseAdded(() => {
      refetchExpenses()
    })
    return {
      loading,
      allExpenses,
      addExpense
    }
  },
  methods: {
    handleAddExpense() {
      this.addExpense({
        input: {
          spotRate: 20,
          amount: 33.33,
          title: 'Entrance beer',
          category: 'Entertainment',
          currency: 'NTD'
        }
      })
    }
  },
  components: {
    ExpensesList
  }
}
</script>

<template>
  <main class="bg-dark-background w-screen">
    <!-- <TheWelcome /> -->
    <h1>Dashboard</h1>
    <button @click="handleAddExpense" class="bg-lime-500 text-teal-50">Add expense!</button>
    <ExpensesList :loading="loading" :allExpenses="allExpenses" />
  </main>
</template>

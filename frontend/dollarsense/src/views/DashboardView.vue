<script lang="ts">
import { useQuery, useMutation } from '@vue/apollo-composable'
import { expenseQueryGql, addExpenseMutationGql } from '../graphql/queries'
import { computed } from 'vue'
import CategoriesPie from '../components/CategoriesPie.vue'

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

    // const categoryPercentages = [50, 20, 10, 5, 15]
    const categoryPercentages = [30, 28, 15, 10, 27]

    return {
      loading,
      allExpenses,
      addExpense,
      categoryPercentages
    }
  },
  methods: {
    handleAddExpense() {
      this.addExpense({
        input: {
          spotRate: 20,
          amount: 33.33,
          description: 'Entrance beer',
          category: 'Entertainment',
          currency: 'NTD'
        }
      })
    }
  },
  components: {
    // ExpensesList
    CategoriesPie
  }
}
</script>

<template>
  <main class="bg-dark-background w-screen p-14">
    <!-- <TheWelcome /> -->
    <!-- <h1>Dashboard</h1>
    <button @click="handleAddExpense" class="bg-lime-500 text-teal-50">Add expense!</button>
    <ExpensesList :loading="loading" :allExpenses="allExpenses" /> -->
    <div class="flex h-full">
      <div class="w-3/5 rounded-lg bg-grey-bubble"></div>
      <div class="flex flex-col items-center pt-14 ml-14 w-2/5 rounded-lg bg-grey-bubble">
        <CategoriesPie
          :inputPercentages="categoryPercentages"
          label="Total Expenses"
          :value="11050"
          currency="NTD"
        />
      </div>
    </div>
  </main>
</template>

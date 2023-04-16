<script lang="ts">
import Button from '../components/ButtonMain.vue'
import { useQuery, useMutation } from '@vue/apollo-composable'
import { expenseQueryGql, addExpenseMutationGql } from '../graphql/queries'
import { ref, computed, h } from 'vue'
import moment from 'moment'

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

    const columns = [
      {
        title: '',
        key: 'checkbox'
      },
      {
        title: 'DATE',
        key: 'createdAt'
      },
      {
        title: 'DESCRIPTION',
        key: 'title',
        className: 'text-blue-500'
      },
      {
        title: 'CATEGORY',
        key: 'category'
      },
      {
        title: 'CURRENCY',
        key: 'currency'
      },
      {
        title: 'AMOUNT',
        key: 'amount'
      }
    ]

    return {
      loading,
      allExpenses,
      addExpense,
      columns
    }
  },
  methods: {
    handleAddExpense() {
      console.log('[handleAddExpense] adding expense!')
      // this.addExpense({
      //   input: {
      //     spotRate: 20,
      //     amount: 33.33,
      //     title: 'Entrance beer',
      //     category: 'Entertainment',
      //     currency: 'NTD'
      //   }
      // })
    },
    formatDate(value: string) {
      return moment(value).format('lll')
    }
  },
  components: {
    Button
  }
}
</script>

<template>
  <main class="bg-dark-background w-screen p-14">
    <div class="bg-grey-bubble w-full h-full rounded-3xl p-12">
      <div class="flex justify-between">
        <h1 class="font-main font-medium text-2xl text-soft-white">Expenses</h1>
        <Button @click="handleAddExpense" text="New Expense" />
      </div>

      <div class="my-8 overflow-y-scroll h-5/6">
        <table class="w-full">
          <thead class="sticky top-0 z-10 bg-grey-bubble">
            <tr class="">
              <td
                class="font-main font-medium text-base text-soft-gray pb-2"
                v-for="column of columns"
              >
                {{ column.title }}
              </td>
            </tr>
          </thead>

          <tbody class="">
            <tr class="hover:bg-theme-green-hover transition" v-for="expense of allExpenses">
              <td
                class="py-2 mb-1 first:rounded-l-md last:rounded-r-md last:pr-5"
                v-for="column of columns"
              >
                <input
                  v-if="column.key === 'checkbox'"
                  class="ml-5 opacity-0 hover:opacity-100 checked:opacity-100 transition"
                  type="checkbox"
                  :id="expense['id']"
                />
                <p
                  v-else-if="column.title === 'DATE'"
                  class="font-main font-light text-soft-gray text-base"
                >
                  {{ `${formatDate(expense[column.key])}` }}
                </p>
                <p
                  v-else-if="column.title === 'DESCRIPTION' || column.title === 'CURRENCY'"
                  class="font-main font-medium text-soft-white text-base"
                >
                  {{ expense[column.key] }}
                </p>
                <p
                  v-else-if="column.title === 'AMOUNT'"
                  class="font-numeric font-regular text-soft-white text-lg"
                >
                  ${{ expense[column.key] }}
                </p>
                <p v-else>{{ expense[column.key] }}</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<style></style>

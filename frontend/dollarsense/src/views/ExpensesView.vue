<script lang="ts">
import ButtonMain from '../components/ButtonMain.vue'
import Modal from '../components/Modal.vue'
import { useQuery, useMutation } from '@vue/apollo-composable'
import { expenseQueryGql, addExpenseMutationGql } from '../graphql/queries'
import { ref, computed, h } from 'vue'
import moment from 'moment'
import Datepicker from 'vue3-datepicker'
import CalendarIcon from '../components/icons/IconCalendar.vue'
import TimePicker from '../components/TimePicker.vue'

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

    const date = ref(new Date())

    return {
      loading,
      allExpenses,
      addExpense,
      columns,
      date
    }
  },
  data() {
    return {
      isModalOpen: false,
      showModal: false,
      showTimePicker: false,
      currentTime: moment().format('LT')
    }
  },
  computed: {
    getCurrentTime() {
      return moment().format('LT')
    }
  },
  methods: {
    handleOpenExpenseModal() {
      this.showModal = true
    },
    handleAddExpense() {
      console.log('[handleAddExpense] adding expense!')
      console.log('[handleAddExpense] date: ', this.date)
      console.log('[handleAddExpense] currentTime: ', this.currentTime)

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
    ButtonMain,
    Modal,
    Datepicker,
    CalendarIcon,
    TimePicker
  }
}
</script>

<template>
  <main class="bg-dark-background w-screen p-14">
    <div class="bg-grey-bubble w-full h-full rounded-3xl p-12">
      <div class="flex justify-between">
        <h1 class="font-main font-medium text-2xl text-soft-white">Expenses</h1>
        <ButtonMain @click="handleOpenExpenseModal" text="New Expense" />
      </div>

      <div class="my-8 overflow-y-scroll h-5/6">
        <table class="w-full">
          <thead class="sticky top-0 z-[1] bg-grey-bubble">
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

    <Modal
      title="Add Expense"
      :show-modal="showModal"
      @close="() => (showModal = false)"
      :class="`${!showModal ? 'opacity-0 scale-125 duration-300 -z-[1]' : 'z-[2]'}`"
    >
      <hr class="h-0.5 border-none my-4 line-gradient-gray" />
      <div class="flex flex-row">
        <div
          class="flex flex-row bg-grey-pill items-center p-0.5 pl-4 rounded-2xl w-fit text-soft-gray mr-8"
        >
          <CalendarIcon class="mr-2" />
          <Datepicker v-model="date" class="bg-transparent border-0 outline-0 w-[100px]" />
        </div>
        <div class="flex flex-row items-center bg-grey-pill p-1 px-4 rounded-2xl">
          <button @click="() => (showTimePicker = true)">{{ currentTime }}</button>
          <!-- <CalendarIcon class="-ml-5" /> -->
          <TimePicker
            :currentTime="getCurrentTime"
            :is-open="showTimePicker"
            @setTime="(newTime) => (currentTime = newTime)"
            @close="() => (showTimePicker = false)"
            :class="`${!showTimePicker && 'hidden'}`"
          />
        </div>
      </div>

      <div class="flex justify-end items-center">
        <a class="text-soft-white mr-8" @click="() => (showModal = false)">Cancel</a>
        <ButtonMain text="Save" @click="handleAddExpense"></ButtonMain>
      </div>
    </Modal>
  </main>
</template>

<style></style>

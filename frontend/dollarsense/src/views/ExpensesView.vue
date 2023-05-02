<script lang="ts">
import ButtonMain from '../components/ButtonMain.vue'
import Modal from '../components/Modal.vue'
import { useQuery, useMutation } from '@vue/apollo-composable'
import {
  expenseQueryGql,
  addExpenseMutationGql,
  deleteExpenseMutationGql,
  editExpenseMutationGql
} from '../graphql/queries'
import { ref, computed, h } from 'vue'
import { Icon } from '@iconify/vue'
import moment from 'moment'
import currency from 'currency.js'
import Datepicker from 'vue3-datepicker'
import CalendarIcon from '../components/icons/IconCalendar.vue'
import TimePicker from '../components/TimePicker.vue'
import Close from '../components/icons/IconClose.vue'
import DownV from '../components/icons/IconDownV.vue'
import CircleCheck from '../components/icons/IconCircleCheck.vue'
import Dropdown from '../components/Dropdown.vue'
import { countryCodes } from '../data/CountryCodes'
import { defaultCategories } from '../data/DefaultCategories'
import { useNotification } from '@kyvg/vue3-notification'
const { notify } = useNotification()

export default {
  setup() {
    const { mutate: addExpense, onDone: expenseAdded } = useMutation(addExpenseMutationGql)
    const { mutate: editExpense, onDone: expenseEdited } = useMutation(editExpenseMutationGql)
    const { mutate: deleteExpense, onDone: expenseDeleted } = useMutation(deleteExpenseMutationGql)

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
    const allExpenses = computed<any[]>(() => result.value?.allExpenses ?? [])
    console.log('[Home] result: ', allExpenses)

    expenseAdded(() => {
      refetchExpenses()
    })

    expenseEdited(() => {
      refetchExpenses()
    })

    expenseDeleted(() => {
      refetchExpenses()
    })

    const columns = [
      {
        title: '',
        key: 'menu'
      },
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
        key: 'description',
        className: 'text-blue-500'
      },
      {
        title: 'CATEGORY',
        key: 'category'
      },
      {
        title: 'SUBCATEGORY',
        key: 'subCategory'
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
    const amountRef = ref()

    return {
      loading,
      allExpenses,
      addExpense,
      editExpense,
      deleteExpense,
      columns,
      date,
      amountRef,
      countryCodes,
      defaultCategories,
      currency
    }
  },
  data() {
    return {
      isModalOpen: false,
      showModal: false,
      isEdit: false,
      showTimePicker: false,
      showCurrencyPicker: false,
      showCategoryPicker: false,
      showSubCategoryPicker: false,
      showMiniMenu: false,
      miniMenuTop: '',
      miniMenuId: '',
      currentTime: moment().format('LT'),
      amount: '',
      description: '',
      isAmountInputFocused: false,
      currentCurrency: 'NTD',
      currencies: ['NTD', 'AUD', 'USD'],
      currentCategory: 'Category',
      currentSubCategory: 'Subcategory',
      currentId: '',
      currentEditId: '',
      isDescription: true,
      isAmount: true,
      isCategory: true
    }
  },
  computed: {
    getCurrentTime() {
      return moment().format('LT')
    }
  },
  methods: {
    capitalizeFirstLetter(text: string) {
      return text.charAt(0).toUpperCase() + text.slice(1)
    },
    lowerFirstLetter(text: string) {
      return text.charAt(0).toLowerCase() + text.slice(1)
    },
    getSelectedExpense(id: string) {
      return this.allExpenses.filter((expense: any) => expense.id === id)[0]
    },
    handleOpenExpenseModal() {
      this.showModal = true
    },
    sanitizeExpenseInput(input: Ds.Expense) {
      const { description, amount, category } = input

      if (!description || !amount || !category) {
        if (!description) {
          this.isDescription = false
        }
        if (!amount) {
          this.isAmount = false
          return false
        }
        // if (category === 'Category') {
        //   this.isCategory = false
        // }
        return false
      } else {
        return true
      }
    },
    calculateDate() {
      const date = moment(this.date).format('YYYY-MM-DD')
      const time = moment(date + ' ' + this.currentTime).format('H:m:ssZ')
      const dateTime = moment(date + ' ' + time).format()

      return new Date(dateTime)
    },
    handleSaveExpense() {
      console.log('[handleAddExpense] adding expense!')
      console.log('[handleAddExpense] currentCategory: ', this.currentCategory)
      console.log('[handleAddExpense] currentSubCategory: ', this.currentSubCategory)
      console.log('[handleAddExpense] date: ', this.date)
      console.log('[handleAddExpense] currentTime: ', this.currentTime)
      console.log('[handleAddExpense] amount: ', this.amount)
      console.log('[handleAddExpense] currentCurrency: ', this.currentCurrency)
      console.log('[handleAddExpense] description: ', this.description)

      const expenseInput: Ds.Expense = {
        description: this.description,
        amount: currency(this.amount).value,
        currency: this.currentCurrency,
        category:
          this.currentCategory === 'Category'
            ? 'Uncategorized'
            : this.capitalizeFirstLetter(this.currentCategory),
        subCategory: this.currentSubCategory,
        createdAt: this.calculateDate()
      }

      if (this.sanitizeExpenseInput(expenseInput)) {
        if (this.isEdit) {
          this.editExpense({
            input: {
              id: this.currentEditId,
              ...expenseInput
            }
          })

          this.currentEditId = ''

          notify({
            type: 'success',
            text: 'Successfully Edited!'
          })
        } else {
          this.addExpense({
            input: expenseInput
          })

          notify({
            type: 'success',
            text: 'Successfully Added!'
          })
        }

        this.showModal = false
      }
    },
    formatDate(value: string) {
      return moment(value).format('lll')
    },
    formatAmount() {
      if (this.amount && !this.amount.match(/\./)) {
        this.amount = this.amount + '.00'
      }
      this.isAmountInputFocused = false
    },
    blurInput() {
      this.amountRef.blur()
    },
    clearInput() {
      this.amount = ''
      this.amountRef.focus()
    },
    setCurrency(event: any) {
      this.currentCurrency = event.target.value
      this.showCurrencyPicker = false
    },
    getFlagCode(currency: string) {
      return Object.keys(countryCodes).find((key) => countryCodes[key].currency === currency)
    },
    getFlagUrl(currency: string) {
      const flagCode = this.getFlagCode(currency)
      return `https://api.iconify.design/circle-flags:${flagCode}.svg`
    },
    getCategoryIcon(category: string) {
      return `solar:${defaultCategories[category].icon}`
    },
    setCategory(category: string) {
      this.currentCategory = category !== 'uncategorized' ? category : 'Category'
      this.showCategoryPicker = false

      if (
        !defaultCategories[this.currentCategory]?.subCategories.includes(this.currentSubCategory)
      ) {
        this.currentSubCategory = 'Subcategory'
      }
    },
    setSubCategory(subCategory: string) {
      this.currentSubCategory = !subCategory ? 'Subcategory' : subCategory
      this.showSubCategoryPicker = false
    },
    handleSubCategoryClick() {
      if (this.currentCategory !== 'Category') {
        this.showSubCategoryPicker = true
      } else {
        notify({
          type: 'warn',
          text: 'Select a category first!'
        })
      }
    },
    onRowHover(id: string) {
      this.currentId = id
    },
    handleMiniMenuClick(event: any, id: string) {
      this.showMiniMenu = true
      const refName = 'ref:' + id
      const ref: any = this.$refs[refName]
      const refTop = ref[0].getBoundingClientRect().y

      this.miniMenuTop = refTop
      this.miniMenuId = id
      this.currentEditId = id
    },
    async handleDelete(id: string) {
      console.log('[handleDelete] Deleting id: ', id)
      const deleteResult = await this.deleteExpense({
        input: {
          id
        }
      })

      if (deleteResult) {
        notify({
          type: 'success',
          text: 'Successfully Removed!'
        })
      }
    },
    handleEdit() {
      this.showModal = true
      this.isEdit = true
      const currentExpense = this.getSelectedExpense(this.miniMenuId)

      this.setCategory(this.lowerFirstLetter(currentExpense.category))
      this.setSubCategory(currentExpense.subCategory)

      const expenseDateTime = new Date(currentExpense.createdAt)
      this.date = expenseDateTime
      this.currentTime = moment(expenseDateTime).format('LT')

      this.amount = currentExpense.amount
      this.currentCurrency = currentExpense.currency
      this.description = currentExpense.description
    },
    resetInputs() {
      this.setCategory('Category')
      this.setSubCategory('Subcategory')

      this.date = new Date()
      this.currentTime = moment().format('LT')

      this.amount = ''
      this.currentCurrency = 'NTD'
      this.description = ''
    },
    handleCloseModal() {
      this.showModal = false

      if (this.isEdit) {
        this.isEdit = false
        this.resetInputs()
      }
    }
  },
  components: {
    ButtonMain,
    Modal,
    Datepicker,
    CalendarIcon,
    TimePicker,
    Close,
    DownV,
    Dropdown,
    CircleCheck,
    Icon
  }
}
</script>

<template>
  <main class="bg-dark-background w-screen p-14">
    <Dropdown
      :is-open="showMiniMenu"
      @close="
        () => {
          showMiniMenu = false
          miniMenuId = ''
        }
      "
      :style="{ top: miniMenuTop + 'px' }"
      :class="`-ml-[60px] -mt-2 h-max w-max px-2 py-3 duration-300 transition-mini-menu
      ${!showMiniMenu && 'opacity-0 scale-90'}`"
    >
      <template v-slot:activator="{ onClick }">
        <button
          @click="
            () => {
              handleEdit()
              onClick()
            }
          "
          class="flex flex-row items-center px-2 rounded-md hover:bg-theme-green-hover"
        >
          <Icon icon="solar:pen-2-outline" class="mr-2" />
          Edit
        </button>
        <button
          @click="
            () => {
              handleDelete(miniMenuId)
              onClick()
            }
          "
          class="flex flex-row items-center px-2 rounded-md hover:bg-theme-green-hover"
        >
          <Icon icon="solar:trash-bin-trash-outline" class="text-red-500 mr-2" />
          Delete
        </button>
      </template>
    </Dropdown>
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
            <tr
              @mouseover="
                () => {
                  currentId = expense['id']
                }
              "
              @mouseleave="
                () => {
                  currentId = ''
                }
              "
              :class="`transition 
              ${miniMenuId === expense['id'] && 'bg-theme-green-hover'}
              ${miniMenuId === '' && 'hover:bg-theme-green-hover'}`"
              v-for="expense of allExpenses"
            >
              <td
                class="py-2 mb-1 first:rounded-l-md last:rounded-r-md last:pr-5"
                v-for="column of columns"
              >
                <button
                  :ref="'ref:' + expense['id']"
                  v-if="column.key === 'menu'"
                  @click="(e) => handleMiniMenuClick(e, expense['id'])"
                  :class="`ml-5 opacity-0 rounded-md py-1 transition 
                  ${
                    ((currentId === expense['id'] && miniMenuId === '') ||
                      miniMenuId === expense['id']) &&
                    'opacity-100'
                  }
                  `"
                >
                  <Icon icon="ph:dots-three-vertical-bold" class="text-soft-white text-xl" />
                </button>
                <input
                  v-else-if="column.key === 'checkbox'"
                  class="mr-3 opacity-0 hover:opacity-100 checked:opacity-100 checked:accent-theme-green transition"
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
      :title="`${isEdit ? 'Edit Expense' : 'Add Expense'}`"
      :show-modal="showModal"
      @close="handleCloseModal"
      :class="`${!showModal ? 'opacity-0 scale-125 duration-300 -z-[1]' : 'z-[2]'}`"
    >
      <div class="flex flex-row mt-5">
        <div class="mr-6">
          <button
            @click="() => (showCategoryPicker = true)"
            class="items-center bg-grey-pill p-1.5 pl-4 pr-3 rounded-xl flex flex-row hover:bg-grey-pill-highlight transition"
          >
            <p class="text-main text-sm font-light leading-3">
              {{ capitalizeFirstLetter(currentCategory) }}
            </p>
            <DownV class="ml-1" />
          </button>
          <Dropdown
            :is-open="showCategoryPicker"
            @close="() => (showCategoryPicker = false)"
            :class="`ml-4 top-8 h-max w-max pl-[18px] py-[18px] ${!showCategoryPicker && 'hidden'}`"
          >
            <template v-slot:activator="{ onClick }">
              <div
                class="dropdown hover:overflow-y-scroll hover:pr-0 overflow-hidden pr-[18px] h-[220px] w-[300px] flex flex-row flex-wrap"
              >
                <div
                  v-for="category in Object.keys(defaultCategories)"
                  class="flex flex-col items-center w-max px-2 rounded-md mb-1 basis-1/3"
                >
                  <button
                    @click="
                      (e) => {
                        onClick()
                        setCategory(category)
                      }
                    "
                    :class="`bg-[#4D4B55] rounded-lg p-5 hover:bg-theme-green-hover transition
                  ${currentCategory === category && 'bg-theme-green'}`"
                  >
                    <Icon class="text-4xl" :icon="getCategoryIcon(category)" />
                  </button>
                  <p class="my-2 font-main font-light text-xs text-soft-white">
                    {{ capitalizeFirstLetter(category) }}
                  </p>
                </div>
              </div>
            </template>
          </Dropdown>
        </div>
        <div>
          <button
            @click="handleSubCategoryClick"
            class="items-center bg-grey-pill p-1.5 pl-4 pr-3 rounded-2xl flex flex-row hover:bg-grey-pill-highlight transition"
          >
            <p class="text-main text-sm font-light leading-3">{{ currentSubCategory }}</p>
            <DownV class="ml-1" />
          </button>
          <Dropdown
            v-if="currentCategory !== 'Category'"
            :is-open="showSubCategoryPicker"
            @close="() => (showSubCategoryPicker = false)"
            :class="`ml-4 top-8 h-max w-max pl-[18px] pt-[18px] ${
              !showSubCategoryPicker && 'hidden'
            }`"
          >
            <template v-slot:activator="{ onClick }">
              <div
                class="dropdown hover:overflow-y-scroll hover:pr-0 overflow-hidden pr-[18px] min-h-fit max-h-[132px] w-[250px] flex flex-row flex-wrap"
              >
                <div
                  v-for="subCategory in defaultCategories[currentCategory]?.subCategories"
                  class="flex flex-col items-center w-max px-2 rounded-md mb-3"
                >
                  <button
                    @click="
                      (e) => {
                        onClick()
                        setSubCategory(subCategory)
                      }
                    "
                    :class="`bg-[#4D4B55] rounded-xl px-4 hover:bg-theme-green-hover transition
                  ${currentSubCategory === capitalizeFirstLetter(subCategory) && 'bg-theme-green'}`"
                  >
                    <p class="my-2 font-main font-normal text-xs text-soft-white">
                      {{ capitalizeFirstLetter(subCategory) }}
                    </p>
                  </button>
                </div>
              </div>
            </template>
          </Dropdown>
        </div>
      </div>

      <hr class="h-0.5 border-none my-4 line-gradient-gray" />

      <div class="flex flex-row">
        <div
          class="flex flex-row bg-grey-pill items-center p-0.5 pl-4 rounded-2xl w-fit text-soft-gray mr-6 hover:bg-grey-pill-highlight transition"
        >
          <CalendarIcon class="mr-2" />
          <Datepicker
            v-model="date"
            class="bg-transparent border-0 outline-0 w-[100px] text-main text-sm font-light leading-3"
          />
        </div>
        <div class="flex flex-row">
          <button
            @click="() => (showTimePicker = true)"
            class="items-center bg-grey-pill p-1 pl-4 pr-3 rounded-2xl flex flex-row hover:bg-grey-pill-highlight transition"
          >
            <p class="text-main text-sm font-light leading-3">{{ currentTime }}</p>
            <DownV class="ml-1" />
          </button>
          <TimePicker
            :currentTime="currentTime"
            :is-open="showTimePicker"
            @setTime="(newTime) => (currentTime = newTime)"
            @close="() => (showTimePicker = false)"
            :class="`ml-4 ${!showTimePicker && 'hidden'}`"
          />
        </div>
      </div>
      <div class="flex flex-row items-center mt-8">
        <input
          ref="amountRef"
          v-maska
          data-maska="$n.##"
          data-maska-tokens="n:[0-9]:multiple"
          class="bg-grey-pill-darker rounded-xl p-2 px-3 w-1/2 outline-none focus:ring-2 focus:ring-theme-green text-soft-white placeholder:text-soft-gray"
          placeholder="$0.00"
          v-model="amount"
          @blur="formatAmount"
          @focus="() => (isAmountInputFocused = true)"
          @keydown.enter="blurInput"
          @input="
            () => {
              if (!isAmount) isAmount = true
            }
          "
        />
        <div
          v-if="!isAmount"
          class="text-sm text-red-600 absolute top-10 flex flex-row items-center mt-1 ml-1"
        >
          <Icon icon="solar:danger-circle-linear" class="mr-1" />
          Please add an amount!
        </div>
        <button :class="`${amount === '' && 'invisible'}`" @click="clearInput">
          <Close class="-ml-8 text-soft-gray" width="20px" />
        </button>

        <div class="ml-6">
          <button
            @click="() => (showCurrencyPicker = true)"
            class="flex flex-row items-center bg-grey-pill rounded-xl p-2.5 px-3 hover:bg-grey-pill-highlight transition"
          >
            <img :src="getFlagUrl(currentCurrency)" class="mr-2" />
            <p class="text-main text-sm font-normal leading-3">{{ currentCurrency }}</p>
            <DownV class="ml-1" />
          </button>
          <Dropdown
            :is-open="showCurrencyPicker"
            @close="() => (showCurrencyPicker = false)"
            :class="`h-max ml-3 flex flex-col top-11 ${!showCurrencyPicker && 'hidden'}`"
          >
            <template v-slot:activator="{ onClick }">
              <button
                :value="currency"
                v-for="currency in currencies"
                @click="
                  (e) => {
                    onClick()
                    setCurrency(e)
                  }
                "
                :class="`hover:bg-theme-green-hover flex flex-row items-center w-max px-2 rounded-md mb-1
              ${currentCurrency === currency && 'text-theme-green'}`"
              >
                <img :src="getFlagUrl(currency)" class="mr-2" />
                {{ currency }}
              </button>
            </template>
          </Dropdown>
        </div>
      </div>

      <div class="flex flex-col mt-8">
        <input
          class="bg-grey-pill-darker rounded-xl p-2 px-3 w-full outline-none focus:ring-2 focus:ring-theme-green text-soft-white placeholder:text-soft-gray"
          placeholder="Description"
          v-model="description"
          @input="
            () => {
              if (!isDescription) isDescription = true
            }
          "
        />
        <div
          v-if="!isDescription"
          class="text-sm text-red-600 absolute top-10 flex flex-row items-center mt-1 ml-1"
        >
          <Icon icon="solar:danger-circle-linear" class="mr-1" />
          Please add a description!
        </div>
      </div>

      <div class="flex justify-end items-center mt-20">
        <button class="text-soft-white mr-8" @click="() => (showModal = false)">Cancel</button>
        <ButtonMain text="Save" @click="handleSaveExpense"></ButtonMain>
      </div>
    </Modal>
  </main>
  <notifications position="top center" width="250px">
    <template #body="props">
      <div
        class="bg-grey-pill text-soft-white mt-5 p-2 rounded-md flex flex-row items-center justify-center"
      >
        <CircleCheck v-if="props.item.type === 'success'" class="text-theme-green mr-2" />
        <Icon
          v-else-if="props.item.type === 'warn'"
          icon="solar:danger-circle-linear"
          class="mr-2 text-theme-orange"
        />
        <p>{{ props.item.text }}</p>
      </div>
    </template>
  </notifications>
</template>

<style></style>

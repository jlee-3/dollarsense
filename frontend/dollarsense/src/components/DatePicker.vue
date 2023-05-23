<script lang="ts">
import Close from './icons/IconClose.vue'
import moment from 'moment'
import { ref } from 'vue'
import { Icon } from '@iconify/vue'

type Views = 'calendar' | 'month' | 'year'

export default {
  props: {
    inputDate: Date,
    isOpen: Boolean
  },
  setup(props) {
    const header = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    const selectedDate = ref(new Date())

    return {
      header,
      selectedDate
    }
  },
  data() {
    return {
      view: <Views>'calendar',
      nowYear: new Date().getFullYear(),
      nowMonth: new Date().getMonth(),
      nowDay: new Date().getDate(),
      currentDate: this.inputDate ? this.inputDate : new Date()
    }
  },
  computed: {
    getMonth() {
      return moment(this.currentDate).format('MMM')
    },
    getYear() {
      return moment(this.currentDate).format('YYYY')
    },
    getMonthIndex() {
      return this.currentDate.getMonth()
    },
    getYearIndex() {
      return this.currentDate.getFullYear()
    },
    generateDays() {
      const year = this.getYearIndex
      const month = this.getMonthIndex + 1
      const daysOfMonth = new Date(year, month, 0).getDate()
      const startDay = new Date(year, month - 1, 1).getDay()
      const daysGrid: number[][] = []

      let day = 1
      let elementNumber = 0
      for (let row = 0; row < 6; row++) {
        daysGrid.push([])

        for (let dayOfWeek = 0; dayOfWeek < 7; dayOfWeek++) {
          if (elementNumber >= startDay && day <= daysOfMonth) {
            daysGrid[row][dayOfWeek] = day
            day++
          } else if (elementNumber < startDay) {
            daysGrid[row][dayOfWeek] = new Date(
              year,
              month - 1,
              -startDay + elementNumber + 1
            ).getDate()
          } else {
            day = 1
            daysGrid[row][dayOfWeek] = day
            day++
          }

          elementNumber++
        }
      }

      return daysGrid
    }
  },
  methods: {
    handleClick(row: number, day: number) {
      const month = this.getMonthFromGrid(row, day)
      if (month !== this.getMonthIndex) {
        this.selectedDate = new Date(this.currentDate?.setMonth(month))
      }

      this.selectedDate = new Date(this.currentDate?.setDate(day))
      this.$emit('setDate', this.selectedDate)
    },
    getMonthFromGrid(row: number, day: number) {
      let month = this.getMonthIndex
      if (row === 0 && day > 7) {
        month = month - 1
      } else if (row > 3 && day < 14) {
        month = month + 1
      }

      return month
    },
    getMonthFromIndex(index: number) {
      return moment(new Date().setMonth(index)).format('MMM')
    },
    isCurrentDay(row: number, day: number) {
      return (
        day === this.nowDay &&
        this.getMonthFromGrid(row, day) === this.nowMonth &&
        this.getYearIndex === this.nowYear
      )
    },
    isCurrentMonth(row: number, day: number) {
      return this.getMonthFromGrid(row, day) === this.getMonthIndex
    },
    isSelectedDate(row: number, day: number) {
      return (
        day === this.selectedDate.getDate() &&
        this.getMonthFromGrid(row, day) === this.selectedDate.getMonth() &&
        this.getYearIndex === this.selectedDate.getFullYear()
      )
    },
    changeMonth(month: number) {
      let year = this.getYearIndex
      let setMonth = month

      if (month === 12) {
        setMonth = 0
        this.currentDate = new Date(this.currentDate?.setFullYear(year + 1))
      } else if (month === -1) {
        setMonth = 11
        this.currentDate = new Date(this.currentDate?.setFullYear(year - 1))
      } else {
        setMonth = month
      }

      this.currentDate = new Date(this.currentDate?.setMonth(setMonth))
    },
    changeYear(year: number) {
      this.currentDate = new Date(this.currentDate?.setFullYear(year))
    },
    setView(view: Views) {
      this.view = view
      if (view === 'year') {
        this.scrollToElement(this.getYear)
      }
    },
    scrollToElement(year: string) {
      document.getElementById('y' + year)?.scrollIntoView()
    }
  },
  components: {
    Close,
    Icon
  }
}
</script>

<template>
  <div class="bg-grey-pill w-fit z-10 p-1 flex flex-col justify-between">
    <div v-show="view === 'calendar'" class="absolute">
      <div class="flex flex-row justify-between px-1.5 mb-1">
        <button
          @click="() => changeMonth(getMonthIndex - 1)"
          class="hover:bg-theme-green-hover p-1 rounded-md"
        >
          <Icon icon="solar:alt-arrow-left-outline" class="" />
        </button>
        <div>
          <button
            @click="() => setView('month')"
            class="mr-2 hover:bg-theme-green-hover px-3 p-1 rounded-md text-soft-white"
          >
            {{ getMonth }}
          </button>
          <button
            @click="
              () => {
                setView('year')
              }
            "
            class="hover:bg-theme-green-hover px-3 p-1 rounded-md text-soft-white"
          >
            {{ getYear }}
          </button>
        </div>
        <button
          @click="() => changeMonth(getMonthIndex + 1)"
          class="hover:bg-theme-green-hover p-1 rounded-md"
        >
          <Icon icon="solar:alt-arrow-right-outline" class="" />
        </button>
      </div>

      <table>
        <thead>
          <tr>
            <td v-for="day in header">
              <div class="flex flex-row justify-center text-xs font-main font-thin">
                {{ day }}
              </div>
            </td>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(row, index) in generateDays">
            <td v-for="day in row">
              <button
                @click="handleClick(index, day)"
                :class="`hover:bg-theme-green-hover w-full p-1 px-1.5 scroll-px-1.5 flex justify-center rounded-md font-main font-thin text-sm 
              ${isCurrentDay(index, day) && 'border border-theme-green'}
              ${isCurrentMonth(index, day) ? 'text-white' : 'text-soft-gray'}
              ${isSelectedDate(index, day) && 'bg-theme-green'}`"
              >
                {{ day }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div
      :class="`absolute min-w-[218px] p-0.5 duration-200 transition-mini-menu
    ${view !== 'month' && 'opacity-0 invisible -z-10 -translate-y-6'}`"
    >
      <button
        @click="() => setView('calendar')"
        class="hover:bg-theme-green-hover p-1 py-2 rounded-md"
      >
        <Icon icon="solar:alt-arrow-left-outline" class="" />
      </button>
      <div class="w-full flex flex-row flex-wrap">
        <button
          @click="
            () => {
              changeMonth(index)
              view = 'calendar'
            }
          "
          v-for="index in [...Array(12).keys()]"
          :class="`basis-1/3 hover:bg-theme-green-hover rounded-md p-1 text-white
          ${getMonthIndex === index && 'bg-theme-green'}
          `"
        >
          {{ getMonthFromIndex(index) }}
        </button>
      </div>
    </div>

    <div
      :class="`min-w-[218px] h-[260px] p-0.5 duration-200 transition-mini-menu
    ${view !== 'year' && 'opacity-0 invisible -z-10 -translate-y-6'}`"
    >
      <button
        @click="() => setView('calendar')"
        class="hover:bg-theme-green-hover p-1 py-2 rounded-md"
      >
        <Icon icon="solar:alt-arrow-left-outline" class="" />
      </button>
      <div
        class="h-[75%] w-full flex flex-row flex-wrap hide-scroll hover:overflow-y-scroll overflow-hidden"
      >
        <button
          :id="`${'y' + year}`"
          @click="
            () => {
              changeYear(year)
              view = 'calendar'
            }
          "
          v-for="year in Array.from({ length: 200 }, (_, i) => i + getYearIndex - 100)"
          :class="`basis-1/3 hover:bg-theme-green-hover rounded-md p-1 text-white
          ${getYearIndex === year && 'bg-theme-green'}
          `"
        >
          {{ year }}
        </button>
      </div>
    </div>
  </div>
</template>

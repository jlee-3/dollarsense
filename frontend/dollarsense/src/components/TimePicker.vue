<script lang="ts">
import Close from './icons/IconClose.vue'

const clickOutside = {
  beforeMount: (el: any, binding: any) => {
    el.clickOutsideEvent = (event: any) => {
      // check that click occurs outside the el and its children
      // and if it did, call method provided in attribute value
      if (!(el == event.target || el.contains(event.target))) {
        binding.value()
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted: (el: any) => {
    document.removeEventListener('click', el.clickOutsideEvent)
  }
}

export default {
  props: {
    currentTime: String,
    isOpen: Boolean
  },
  directives: {
    clickOutside
  },
  setup(props) {
    const createDebounce = () => {
      let timeout: any
      return function (fn: any, delay: number) {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          fn()
        }, delay || 500)
      }
    }

    const scrollToElement = (timeValue: string) => {
      const [hour, minute, amPm] = timeValue.split(':')
      const hourElement = document.getElementById('h' + hour)?.scrollIntoView()
      const minuteElement = document.getElementById('m' + minute)?.scrollIntoView()
    }

    return {
      scrollToElement,
      debounce: createDebounce()
    }
  },
  created() {
    // window.addEventListener('scroll', this.handleScroll)
  },
  unmounted() {
    // window.removeEventListener('scroll', this.handleScroll)
  },
  data() {
    return {
      openStatus: false,
      lastTopY: 0,
      hours: [...Array.from({ length: 12 }, (_, i) => i + 1), 1, 2, 3],
      minutes: [...Array(60).keys(), 0, 1, 2],
      amPm: this.currentTime?.match('PM') ? ['PM', 'AM'] : ['AM', 'PM'],
      setTime: this.currentTime?.replace(' ', ':') || ''
    }
  },
  methods: {
    handleClose() {
      this.openStatus = false
      this.$emit('close')
    },
    handleClick(event: any, type: string) {
      const [currentHour, currentMinute, currentAmPm] = this.setTime.split(':')
      const hour = type === 'hours' ? event.target.value : currentHour
      const minute = type === 'minutes' ? event.target.value : currentMinute
      const amPm = type === 'amPm' ? event.target.value : currentAmPm

      if (type === 'amPm' && event.target.value !== this.amPm[0]) {
        this.amPm = this.amPm.reverse()
      }

      const newTime = hour + ':' + minute + ':' + amPm
      this.setTime = newTime
      this.scrollToElement(newTime)

      const formattedMinute = minute < 10 ? '0' + minute : minute
      const newFormattedTime = hour + ':' + formattedMinute + ' ' + amPm
      this.$emit('setTime', newFormattedTime)
      this.handleClose()
    },
    // handleScroll(event: any) {
    //   this.debounce(() => {
    //     if (event.target.scrollTop > this.lastTopY) {
    //       console.log('scrolling down!')
    //     } else {
    //       console.log('scrolling up!')
    //     }
    //     this.lastTopY = event.target.scrollTop
    //   }, 50)
    // },
    onScroll(event: any) {
      const scrollTop = event.target.scrollTop
      const clientHeight = event.target.clientHeight
      const scrollHeight = event.target.scrollHeight

      if (scrollTop + clientHeight >= scrollHeight) {
        // set y position to 0.5 to enable continuous scroll to end
        event.target.scrollTo(0, 0.5)
      } else if (scrollTop === 0) {
        // also give a 0.5 buffer to enable continuous scroll to beginning
        event.target.scrollTo(0, scrollHeight - clientHeight - 0.5)
      }
    },
    handleClickOutside() {
      if (this.isOpen && !this.openStatus) {
        if (this.currentTime && this.setTime === this.currentTime?.replace(' ', ':')) {
          this.scrollToElement(this.currentTime.replace(' ', ':'))
        }

        this.openStatus = true
      } else if (this.isOpen && this.openStatus) {
        this.handleClose()
      }
    }
  },
  components: {
    Close
  }
}
</script>

<template>
  <div
    v-click-outside="handleClickOutside"
    class="bg-grey-pill h-[92px] absolute top-9 z-10 p-2 rounded-md flex flex-row justify-between flex-nowrap"
  >
    <div v-on:scroll="onScroll" class="time-picker flex flex-col overflow-y-scroll box-content">
      <button
        :key="hour"
        :id="'h' + hour"
        :value="hour"
        v-for="hour of hours"
        @click="(e) => handleClick(e, 'hours')"
        :class="`hover:bg-theme-green-hover p-0.5 px-1.5 pt-1 mb-1 text-xs mr-1.5 rounded-md ${
          hour.toString() === setTime.split(':')[0] && 'bg-theme-green text-white'
        }`"
      >
        {{ hour }}
      </button>
    </div>
    <div v-on:scroll="onScroll" class="time-picker flex flex-col overflow-y-scroll box-content">
      <button
        :key="minute"
        :id="'m' + minute"
        :value="minute"
        v-for="minute of minutes"
        @click="(e) => handleClick(e, 'minutes')"
        :class="`hover:bg-theme-green-hover p-0.5 px-1.5 pt-1 mb-1 text-xs mr-1.5 rounded-md ${
          minute.toString() === setTime.split(':')[1] && 'bg-theme-green text-white'
        }`"
      >
        {{ minute < 10 ? '0' + minute : minute }}
      </button>
    </div>
    <div class="flex flex-col">
      <button
        :key="value"
        :value="value"
        v-for="value of amPm"
        @click="(e) => handleClick(e, 'amPm')"
        :class="`hover:bg-theme-green-hover p-0.5 px-1.5 pt-1 mb-1 text-xs rounded-md ${
          value === setTime.split(':')[2] && 'bg-theme-green text-white'
        }`"
      >
        {{ value }}
      </button>
    </div>
  </div>
</template>

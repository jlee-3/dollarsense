<script lang="ts">
import Close from './icons/IconClose.vue'

export default {
  props: {
    isOpen: Boolean,
    options: Object
  },
  data() {
    return {
      openStatus: false,
      currencies: ['NTD', 'AUD', 'USD']
    }
  },
  methods: {
    handleClose() {
      this.openStatus = false
      this.$emit('close')
    },
    closeFromOutside(event: any) {
      if (event.target.id === 'outerArea') {
        this.$emit('close')
      }
    },
    handleClickOutside() {
      if (this.isOpen && !this.openStatus) {
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
    class="bg-grey-pill h-[92px] absolute top-11 z-20 p-2 rounded-md flex flex-col"
  >
    <slot></slot>
  </div>
</template>

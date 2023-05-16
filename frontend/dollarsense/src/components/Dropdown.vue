<script lang="ts">
import Close from './icons/IconClose.vue'

export default {
  props: {
    isOpen: Boolean,
    options: Object
  },
  data() {
    return {
      openStatus: false
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
      // sets internal 'isOpen' state for component
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
    class="bg-grey-pill absolute z-10 p-2 rounded-md shadow-lg shadow-dark-background/50"
  >
    <slot name="activator" :onClick="handleClose"></slot>
  </div>
</template>

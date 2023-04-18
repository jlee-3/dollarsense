<script lang="ts">
import Close from './icons/IconClose.vue'

export default {
  props: {
    title: String,
    showModal: Boolean
  },
  methods: {
    handleClose() {
      this.$emit('close')
    }
  },
  components: {
    Close
  }
}
</script>

<template>
  <div class="w-full h-full bg-[rgb(0,0,0,0.4)] fixed left-0 top-0 flex flex-col">
    <div :class="`bg-grey-bubble w-[500px] m-auto p-8 justify-center rounded-2xl`">
      <div class="flex justify-between items-center">
        <p class="text-soft-white font-main font-medium text-2xl">{{ title }}</p>
        <Close @click="handleClose" />
      </div>
      <slot></slot>
    </div>
  </div>
</template>

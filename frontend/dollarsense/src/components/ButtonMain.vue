<script setup lang="ts">
defineProps<{
  text: string
}>()
</script>

<template>
  <button
    class="bg-theme-green transition hover:bg-theme-green-highlight active:bg-theme-green-hover rounded-xl p-3 px-8"
  >
    <p class="font-main font-semibold text-sm text-white">{{ text }}</p>
  </button>
</template>

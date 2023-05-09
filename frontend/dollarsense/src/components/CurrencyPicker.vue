<script lang="ts">
import Dropdown from '../components/Dropdown.vue'
import DownV from '../components/icons/IconDownV.vue'
import { countryCodes } from '../data/CountryCodes'

export default {
  props: {
    currencyState: String,
    buttonClass: String
  },
  methods: {
    handleSelect(event: any) {
      this.currentCurrency = event.target.value
      this.$emit('selectCurrency', this.currentCurrency)
    },
    getFlagCode(currency: string) {
      return Object.keys(countryCodes).find((key) => countryCodes[key].currency === currency)
    },
    getFlagUrl(currency: string) {
      const flagCode = this.getFlagCode(currency)
      return `https://api.iconify.design/circle-flags:${flagCode}.svg`
    }
  },
  emits: ['selectCurrency'],
  data() {
    return {
      showCurrencyPicker: false,
      currencies: ['NTD', 'AUD', 'USD'],
      currentCurrency: this.currencyState || 'NTD'
    }
  },
  components: {
    Dropdown,
    DownV
  }
}
</script>

<template>
  <div>
    <button
      @click="() => (showCurrencyPicker = true)"
      :class="`flex flex-row items-center bg-grey-pill p-2.5 px-3 hover:bg-grey-pill-highlight transition ${buttonClass}`"
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
              handleSelect(e)
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
</template>

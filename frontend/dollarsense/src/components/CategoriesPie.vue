<script lang="ts">
export default {
  props: {
    inputPercentages: {
      type: Object,
      required: true
    },
    label: {
      type: String,
      required: true
    },
    value: {
      type: Number,
      required: true
    },
    currency: {
      type: String,
      required: true
    }
  },
  setup(props) {},
  computed: {},
  methods: {
    setRange() {},
    setArcPercentage() {},
    getPercentageArray(percentage: number) {
      return percentage.toString() + ' ' + (100 - percentage).toString()
    },
    getOffset(categoryNum: number) {
      let currentOffset = 25
      for (let i = 0; i < categoryNum; i++) {
        currentOffset = currentOffset - this.inputPercentages[i]
      }

      // console.log('[getOffset] return: ', currentOffset + 25)
      return currentOffset
    }
  },
  components: {}
}
</script>

<template>
  <svg width="400px" height="400px" viewBox="0 0 50 50" class="donut">
    <text
      fill="white"
      x="25"
      y="22"
      text-anchor="middle"
      class="font-main text-[2.2px] font-semibold"
    >
      {{ label }}
    </text>
    <text
      fill="white"
      x="25"
      y="28"
      text-anchor="middle"
      class="font-numeric text-[5.5px] font-light"
    >
      {{ value }}
    </text>
    <text
      fill="white"
      x="25"
      y="31.5"
      text-anchor="middle"
      class="font-numeric text-[2.5px] font-light"
    >
      {{ currency }}
    </text>
    <circle
      class="stroke-bg-olive"
      cx="25"
      cy="25"
      r="15.91549430918954"
      fill="transparent"
      stroke-width="2"
    ></circle>
    <g v-for="number in [...Array(4).keys()]" :key="number" :filter="`url(#glow${number})`">
      <filter :id="`glow${number}`">
        <feDropShadow
          dx="0"
          dy="0"
          stdDeviation="0.7"
          :flood-color="`var(--category-${number + 1})`"
        />
      </filter>
      <circle
        cx="25"
        cy="25"
        r="15.91549430918954"
        fill="transparent"
        stroke-width="2"
        :stroke-dasharray="getPercentageArray(inputPercentages[number])"
        :stroke-dashoffset="getOffset(number)"
        stroke-linecap="round"
        :stroke="`var(--category-${number + 1})`"
      ></circle>
    </g>
  </svg>
</template>

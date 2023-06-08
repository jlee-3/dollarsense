<script lang="ts">
export default {
  // props: {},
  // setup(props) {
  //   return {}
  // },
  data() {
    return {
      valueLeft: 0,
      valueRight: 50
    }
  },
  computed: {},
  methods: {
    handleSlide(event: any) {
      const sliderId = event.target.id

      if (
        sliderId === 'sliderRight' &&
        this.valueRight <= this.getBuffer(this.valueLeft, undefined)
      ) {
        this.valueRight = this.getBuffer(this.valueLeft, undefined)
      } else if (
        sliderId === 'sliderLeft' &&
        this.valueLeft >= this.getBuffer(undefined, this.valueRight)
      ) {
        this.valueLeft = this.getBuffer(undefined, this.valueRight)
      }
    },
    getBuffer(valueLeft?: number, valueRight?: number) {
      const value = valueLeft ?? valueRight
      return valueLeft ? Number(value) + Number(14) : Number(value) - Number(14)
    }
  },
  components: {}
}
</script>

<template>
  <div class="my-5 mx-2 bg-theme-green-hover h-[10px] rounded-lg">
    <span
      :style="{
        width: valueRight - valueLeft + '%',
        left: valueLeft + '%'
      }"
      :class="`rounded-lg flex h-[10px] bg-theme-green
      `"
    >
    </span>
    <input
      id="sliderLeft"
      @input="handleSlide"
      type="range"
      :min="0"
      :max="100"
      v-model.number="valueLeft"
      :step="1"
      class="slider w-full"
    />
    <input
      id="sliderRight"
      @input="handleSlide"
      type="range"
      :min="0"
      :max="100"
      v-model.number="valueRight"
      :step="1"
      class="slider w-full"
    />
  </div>
</template>

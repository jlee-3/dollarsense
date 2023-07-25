<script lang="ts">
export default {
  props: {
    amounts: Object
  },
  setup(props) {
    // console.log('[setup] amounts: ', props.amounts)
    return {}
  },
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

      this.$emit('setRange', {
        valueLeft: this.valueLeft,
        valueRight: this.valueRight
      })
    },
    getBuffer(valueLeft?: number, valueRight?: number) {
      const value = valueLeft ?? valueRight
      return valueLeft ? Number(value) + Number(10) : Number(value) - Number(10)
    }
  },
  components: {}
}
</script>

<template>
  <div class="my-2 mx-2 bg-theme-green-hover h-[5px] rounded-lg">
    <span
      :style="{
        width: valueRight - valueLeft + '%',
        left: valueLeft + '%'
      }"
      :class="`rounded-lg flex h-[5px] bg-theme-green
      `"
    >
    </span>
    <input
      id="sliderLeft"
      @click.stop="handleSlide"
      type="range"
      :min="0"
      :max="100"
      v-model.number="valueLeft"
      :step="1"
      class="slider w-full"
    />
    <input
      id="sliderRight"
      @click.stop="handleSlide"
      type="range"
      :min="0"
      :max="100"
      v-model.number="valueRight"
      :step="1"
      class="slider w-full"
    />
  </div>
</template>

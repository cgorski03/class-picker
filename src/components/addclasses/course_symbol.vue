<template>
  <span
    v-if="isCompatible"
    style="color: green"
    class="symbol"
    aria-label="Class is compatible"
    @mouseover="show_symbol_tooltip"
    @mouseleave="hide_symbol_tooltip"
    >✓</span
  >
  <span
    v-else
    class="symbol x-mark"
    aria-label="Class is not compatible"
    @mouseover="show_symbol_tooltip"
    @mouseleave="hide_symbol_tooltip"
    >✕</span
  >
  <div v-if="show_symbol_tooltip" class="_symbol_tooltip">
    {{
      isCompatible
        ? "Class is compatible with schedule"
        : "Class has conflicts with " + course
    }}
  </div>
</template>

<style>
.symbol:hover + ._symbol_tooltip {
  display: block;
}

.symbol {
  position: absolute;
  top: 8px;
  left: 3%;
  font-size: 25px;
  font-weight: bold;
}
.checkmark {
  color: green;
}
.x-mark {
  color: red;
}
._symbol_tooltip {
  display: none;
  position: absolute;
  top: -10px;
  left: 3%;
  background-color: #fff;
  color: #000;
  padding: 2px;
  border: 2px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  white-space: nowrap;
  z-index: 1;
}
</style>

<script>
export default {
  props: {
    isCompatible: Boolean,
    course: String,
  },
  data() {
    return {
      is_symbol_tooltipVisible: false,
    };
  },
  methods: {
    show_symbol_tooltip() {
      this.is_symbol_tooltipVisible = true;
    },
    hide_symbol_tooltip() {
      this.is_symbol_tooltipVisible = false;
    },
  },
};
</script>

<template>
      <span class="checkmark" aria-label="Class is compatible" @mouseover="showTooltip" @mouseleave="hideTooltip">✓</span>
      <div v-if="showTooltip" class="tooltip">Class is compatible</div>
  </template>
  
  <style>
  .checkmark:hover +.tooltip {
    display: block;
  }
  
  .checkmark {
    position: relative;
    top: 5px;
    right: 5px;
    color: black; /* Change the color as needed */
    font-size: 20px; /* Adjust the font size as needed */
    font-weight: bold;
  }
  
  .tooltip {
    display: none;
    position: absolute;
    top: -15px; /* Adjust the distance from the checkmark */
    left: 7%;
    transform: translateX(-50%);
    background-color: #fff; /* Tooltip background color */
    color: #000; /* Tooltip text color */
    padding: 2px;
    border: 1px solid #ccc; /* Tooltip border */
    border-radius: 5px;
    font-size: 14px;
    white-space: nowrap;
    z-index: 1;
  }
  
  </style>
  
  <script>
export default {
  data() {
    return {
      isTooltipVisible: false,
    };
  },
  methods: {
    showTooltip() {
      this.isTooltipVisible = true;
    },
    hideTooltip() {
      this.isTooltipVisible = false;
    },
  },
};
</script>

  
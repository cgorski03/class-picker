<template>
    <span v-if="isCompatible" class="symbol checkmark" aria-label="Class is compatible" @mouseover="show_symbol_tooltip" @mouseleave="hide_symbol_tooltip">✓</span>
    <span v-else class="symbol x-mark" aria-label="Class is not compatible" @mouseover="show_symbol_tooltip" @mouseleave="hide_symbol_tooltip">✕</span>
    <div v-if="show_symbol_tooltip" class="_symbol_tooltip">{{ isCompatible ? 'Class is compatible with schedule' : 'Class has conflicts with ' + course}}</div>
</template>

<style>
.symbol:hover +._symbol_tooltip {
  display: block;

}

.symbol {
  position: absolute;
  top: 5px;
  left: 5px;
  font-size: 20px; /* Adjust the font size as needed */
  font-weight: bold;
}
.checkmark{
  color:green;
}
.x-mark{
  color:red;
}
._symbol_tooltip {
  display: none;
  position: absolute;
  top: -15px; /* Adjust the distance from the symbol */
  left: 3%;
  /*transform: translateX(-50%);*/
  background-color: #fff; /* _symbol_tooltip background color */
  color: #000; /* _symbol_tooltip text color */
  padding: 2px;
  border: 1px solid #ccc; /* _symbol_tooltip border */
  border-radius: 5px;
  font-size: 14px;
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


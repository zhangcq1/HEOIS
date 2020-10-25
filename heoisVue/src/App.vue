<template>
  <div class="MianPage">
    <HTopBar></HTopBar>
    <div class="body">
      <router-view />
    </div>
  </div>
</template>

<script>
import HTopBar from './views/HTopBar.vue'
export default {
  components: {
    HTopBar
  }
}
</script>

<style lang="less">
  .icon {
    width: 1em;
    height: 1em;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;
    width: 100%;
    height: 100%;
  }
</style>

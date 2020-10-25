<template>
  <div class="myicon">
    <svg class="icon" aria-hidden="true">
      <use :xlink:href="myclass"></use>
    </svg>
  </div>
</template>
<script>
export default {
  name: 'myicon',
  data () {
    return {
      myclass: '#' + this.iconclass
    }
  },
  props: {
    iconclass: String
  }
}
</script>
<style lang="less" scoped>
   .myicon{
     svg{
       height: 80%;
       // border:5px solid black;
     }
     display: flex;
     align-items: center;
     justify-content: center;
   }
</style>

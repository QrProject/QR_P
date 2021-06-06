<template>
  <div>
    hello
    {{ pmpInfo }}
  </div>
</template>

<script>
const TEMP_DOMAIN = 'http://3.35.235.144:3000/';
export default {
  data () {
    return {
      pmpInfo: {},
    }
  },
  async mounted() {
    const pmp = await fetch(`${TEMP_DOMAIN}${this.$route.params.id}`).then(res => res.json());
    this.pmpInfo = pmp;
  }
}
</script>

<style>

</style>
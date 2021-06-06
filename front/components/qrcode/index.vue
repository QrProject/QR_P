<template>
  <div>
    <canvas id="canvas"></canvas>
  </div>
</template>

<script>
import QRCode from 'qrcode';

export default {
  props: {
    url: {
      type: String,
    }
  },
  mounted () {
    const canvas = document.getElementById('canvas')
    QRCode.toCanvas(canvas, this.url, function (error) {
      if (error) console.error(error)
      console.log('success!');
    })
  }
}
</script>

<style>

</style>
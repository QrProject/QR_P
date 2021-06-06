<template>
  <div class="pmp-container">
    <h2>펌프 상세정보</h2>
    <div>
      <div class="flex">
        <div>현장명</div>
        <div>신나무실 5단지</div>
      </div>
      <div class="flex">
        <div>제조업체</div>
        <div>DY대영파워펌프</div>
      </div>
      <div class="flex">
        <div>납품업체</div>
        <div>규석이네 펌프가게</div>
      </div>
      <div class="flex">
        <div>무상AS기간</div>
        <div>2020.01.01~2022.12.31</div>
      </div>
      <div class="flex">
        <div>제조일</div>
        <div>2020.01.01</div>
      </div>

      <h2>펌프 수리 내역</h2>
      <div class="flex">
        <div>양규석</div>
        <div>2020.01.01</div>
      </div>
      <div class="flex">
        <div>오석기</div>
        <div>2020.01.01</div>
      </div>
      <div class="flex">
        <div>최윤어</div>
        <div>2020.01.01</div>
      </div>
      <br>
      <br>
      <div>
        real world api Call
      </div>
      <div>{{ pmpInfo }}</div>
    </div>
  </div>
</template>

<script>
const TEMP_DOMAIN = 'http://3.35.235.144:3000/model/';
const TEMP2_DOMAIN = 'http://192.168.10.102:3000/';

export default {
  head () {
    return {
      title: `DY펌프 model - ${this.$route.params.id}`
    }
  },
  data () {
    return {
      pmpInfo: null,
    }
  },
  async mounted() {
    const pmp = await fetch(`${TEMP_DOMAIN}${this.$route.params.id}`).then(res => res.json());
    this.pmpInfo = pmp;
  }
}
</script>

<style>
.flex {
  display: flex;
  justify-content: center;
}
.flex div {
  margin-right: 10px;
  width: 200px;
}
.pmp-container {
  margin: 0 auto;
}
</style>
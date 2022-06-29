<template>
  <div class="layout-header">
    <div class="logo-wrapper" @click="$router.push('/')">
      <img src="../assets/logo.png" />
      <div class="logo-text">DataToken</div>
    </div>
    <!-- 
    <div class="right-wrapper">
      <a-button type="primary" ghost>DataTracer</a-button>
    </div> -->
  </div>
</template>

<style lang="less" scoped>
  .layout-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 101;
    box-shadow: 0 2px 6px 0 rgba(0, 0, 0, 0.02);
    background: @white;
    transition: all 0.3s;
    padding: 0 @margin;
    display: flex;
    align-items: center;
    height: @header-height;

    .logo-wrapper {
      display: flex;
      align-items: center;
      cursor: pointer;
      flex: 1;
      img {
        width: 44px;
      }

      .logo-text {
        margin-left: 8px;
        font-size: 18px;
        font-weight: bold;
        color: #21325b;
      }
    }
  }
</style>

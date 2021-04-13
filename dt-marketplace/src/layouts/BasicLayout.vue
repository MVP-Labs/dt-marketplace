<template>
  <div class="basic-layout">
    <Header />

    <main class="layout-content">
      <router-view class="router-view"></router-view>
    </main>

    <Footer />
  </div>
</template>

<script>
import Header from "./Header";
import Footer from "./Footer";

export default {
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      keepAlive: [],
    };
  },
};
</script>

<style lang="less" scoped>
.basic-layout {
  .layout-content {
    padding-top: @header-height;
  }
}
</style>

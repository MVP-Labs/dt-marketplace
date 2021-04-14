<template>
  <div class="basic-layout">
    <Header />

    <main class="layout-content">
      <keep-alive :include="['home']">
        <router-view class="router-view"></router-view>
      </keep-alive>
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

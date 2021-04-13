<template>
  <div class="home">
    <div class="input-wrapper">
      <div class="title">
        A marketplace for trusted data and computing services
      </div>
      <a-input-search
        style="width: 460px"
        placeholder="Search the marketplace for"
        enter-button="Search"
        size="large"
      />
    </div>

    <div class="content-wrapper">
      <div class="filters-bar">
        <a-dropdown size="large" :trigger="['click']">
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            All products <a-icon type="down" />
          </a>
          <a-menu slot="overlay">
            <a-menu-item key="All products">All products</a-menu-item>
            <a-menu-item key="EN">EN</a-menu-item>
            <a-menu-item key="ES">ES</a-menu-item>
            <a-menu-item key="RU">RU</a-menu-item>
            <a-menu-item key="FA">FA</a-menu-item>
          </a-menu>
        </a-dropdown>

        <a-dropdown size="large">
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            Category <a-icon type="down" />
          </a>
          <a-menu slot="overlay" size="large">
            <a-menu-item key="Account">Account</a-menu-item>
            <a-menu-item key="Settings">Settings</a-menu-item>
          </a-menu>
        </a-dropdown>

        <a-dropdown size="large">
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            Sort by <a-icon type="down" />
          </a>
          <a-menu slot="overlay">
            <a-menu-item key="Account">Account</a-menu-item>
            <a-menu-item key="Settings">Settings</a-menu-item>
          </a-menu>
        </a-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: false,
    };
  },
};
</script>

<style lang="less" scoped>
.home {
  .input-wrapper {
    text-align: center;
    padding: 40px;

    .title {
      font-size: 19px;
      margin-bottom: 20px;
      color: rgb(114, 114, 114);
    }
  }

  .content-wrapper {
    background: @white;

    .filters-bar {
      padding: 20px 0;
      margin: 0 @margin;
      font-size: 16px;

      .ant-dropdown-trigger {
        margin-right: 30px;
      }
    }
  }
}

.ant-dropdown-menu-item {
  font-size: 16px;
  padding: 8px 20px;
}
</style>

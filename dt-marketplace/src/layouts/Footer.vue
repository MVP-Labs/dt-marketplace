<template>
  <div class="layout-footer">
    <div class="list">
      <div class="section" v-for="section in list" :key="section.title">
        <div class="title">{{ section.title }}</div>
        <div class="item" v-for="item in section.children" :key="item.text">
          {{ item.text }}
        </div>
      </div>
    </div>
    <div class="copyright">
      ©️ 2021 All Rights Reserved. Powered by <a href="#">DataToken Market</a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: [
        {
          title: "LEARN",
          children: [
            {
              text: "Top",
            },
            {
              text: "Network",
            },
            {
              text: "Marketplace",
            },
            {
              text: "Core",
            },
          ],
        },
        {
          title: "APPS",
          children: [
            {
              text: "Marketplace",
            },
            {
              text: "Core",
            },
          ],
        },
        {
          title: "PROJECT",
          children: [
            {
              text: "About",
            },
            {
              text: "Design Assets",
            },
            {
              text: "Blog",
            },
          ],
        },
        {
          title: "DOCS",
          children: [
            {
              text: "Streams",
            },
            {
              text: "Canvases",
            },
            {
              text: "Dashboards",
            },
            {
              text: "Products",
            },
          ],
        },
        {
          title: "CONTACT",
          children: [
            {
              text: "General",
            },
            {
              text: "Media",
            },
            {
              text: "Jobs",
            },
            {
              text: "Business",
            },
          ],
        },
        {
          title: "DOCUMENTS",
          children: [
            {
              text: "Whitepaper",
            },
            {
              text: "Contribution Summary",
            },
            {
              text: "Terms & Conditions",
            },
            {
              text: "Privacy",
            },
          ],
        },
      ],
    };
  },
};
</script>

<style lang="less" scoped>
.layout-footer {
  padding: 60px 120px;

  .list {
    display: flex;
    justify-content: space-between;
    margin-bottom: 60px;

    .section {
      .title {
        font-size: 15px;
        margin-bottom: 10px;
      }

      .item {
        color: rgb(82, 82, 82);
        margin-bottom: 8px;
        cursor: pointer;
        &:hover {
          color: @primary-color;
        }
      }
    }
  }

  .copyright {
    text-align: center;
    font-size: 15px;
  }
}
</style>

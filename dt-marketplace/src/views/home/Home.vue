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
        <a-dropdown>
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

        <a-dropdown>
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            Category <a-icon type="down" />
          </a>
          <a-menu slot="overlay">
            <a-menu-item key="Account">Account</a-menu-item>
            <a-menu-item key="Settings">Settings</a-menu-item>
          </a-menu>
        </a-dropdown>

        <a-dropdown>
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            Sort by <a-icon type="down" />
          </a>
          <a-menu slot="overlay">
            <a-menu-item key="Account">Account</a-menu-item>
            <a-menu-item key="Settings">Settings</a-menu-item>
          </a-menu>
        </a-dropdown>
      </div>

      <a-spin :spinning="loading">
        <div class="card-list">
          <a-card
            v-for="item in list"
            :key="item.name"
            class="card-item"
            hoverable
            :bordered="false"
            @click="$router.push(`/detail/${item.id}`)"
          >
            <img :src="item.source" />

            <div class="text-wrapper">
              <div class="name">{{ item.name }}</div>
              <div class="desc">{{ item.desc }}</div>
            </div>
          </a-card>
        </div>
      </a-spin>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true,
      list: [],
    };
  },
  mounted() {
    setTimeout(() => {
      this.loading = false;
      this.list = [
        {
          name: "Swash",
          desc: "SwashData Tech Oy",
          is_union: false,
          id:
            "6be8ceda7a3c4fe7991eab501975b85ec2bb90452d0e4c93bc252937476eae75",
          source:
            "https://streamr-public.s3.amazonaws.com/product-images/u5Kx9nEcRR6whI3NLjo0MAQnZyn3_fRzy6WIp9ZA73dA.png",
        },

        {
          name: "Swash",
          desc: "SwashData Tech Oy",
          is_union: false,
          id:
            "6be8ceda7a3c4fe7991eab501975b85ec2bb90452d0e4c93bc252937476eae75",
          source:
            "https://streamr-public.s3.amazonaws.com/product-images/Ir_tSV2SRtGLXdO1TnCwHQW6Y2ZM9gSa-1FYB4zWgBXg.jpg",
        },

        {
          name: "Swash",
          desc: "SwashData Tech Oy",
          is_union: false,
          id:
            "6be8ceda7a3c4fe7991eab501975b85ec2bb90452d0e4c93bc252937476eae75",
          source:
            "https://streamr-public.s3.amazonaws.com/product-images/lYdrpZamTTiy_emLw93viwFxM6_nLkQwGokzsObLRoBA.png",
        },
        {
          name: "Swash",
          desc: "SwashData Tech Oy",
          is_union: false,
          id:
            "6be8ceda7a3c4fe7991eab501975b85ec2bb90452d0e4c93bc252937476eae75",
          source:
            "https://streamr-public.s3.amazonaws.com/product-images/Ir_tSV2SRtGLXdO1TnCwHQW6Y2ZM9gSa-1FYB4zWgBXg.jpg",
        },
        {
          name: "Swash",
          desc: "SwashData Tech Oy",
          is_union: false,
          id:
            "6be8ceda7a3c4fe7991eab501975b85ec2bb90452d0e4c93bc252937476eae75",
          source:
            "https://streamr-public.s3.amazonaws.com/product-images/KQ1Bj0sQQWC_dfCjkUGsEA_WBsGnFxQI6SvEd6RI4DOw.png",
        },
        {
          name: "Swash",
          desc: "SwashData Tech Oy",
          id:
            "6be8ceda7a3c4fe7991eab501975b85ec2bb90452d0e4c93bc252937476eae75",
          is_union: false,
          source:
            "https://streamr-public.s3.amazonaws.com/product-images/Ir_tSV2SRtGLXdO1TnCwHQW6Y2ZM9gSa-1FYB4zWgBXg.jpg",
        },
      ];
    }, 2000);
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
    .filters-bar {
      padding: 20px 80px;
      font-size: 16px;
      background: @white;

      .ant-dropdown-trigger {
        margin-right: 30px;
      }
    }

    .card-list {
      min-height: 400px;
      padding: 20px 80px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      /deep/.ant-card-body {
        padding: 0;
      }
      .card-item {
        width: 240px;
        margin-bottom: 20px;
        img {
          width: 100%;
        }

        .text-wrapper {
          padding: 16px;
          .name {
            font-size: 16px;
          }

          .desc {
            font-size: 13px;
            color: @text-color-2;
            margin-top: 4px;
          }
        }
      }
    }
  }
}

.ant-dropdown-menu-item {
  font-size: 16px;
  padding: 8px 20px;
}
</style>

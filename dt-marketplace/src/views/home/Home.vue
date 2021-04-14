<template>
  <div class="home">
    <div class="input-wrapper">
      <div class="title">
        A marketplace for trusted data and computing services
      </div>
      <a-input-search
        style="width: 440px"
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

      <a-spin :spinning="loading" size="large">
        <div class="card-list">
          <a-card
            v-for="item in list"
            :key="item.dt"
            class="card-item"
            hoverable
            :bordered="false"
            @click="$router.push(`/detail/${item.dt}`)"
          >
            <div class="dot" v-if="item.union_or_not">Data Union</div>
            <img :src="item.fig" />

            <div class="text-wrapper">
              <div class="name">{{ item.name }}</div>
              <div class="desc">{{ item.issuer }}</div>
            </div>
          </a-card>
        </div>

        <div class="view-more">
          <a-button size="large" shape="round">VIEW MORE</a-button>
        </div>
      </a-spin>
    </div>
  </div>
</template>

<script>
import { getDtList } from "../../api/index";

const images = [
  "https://streamr-public.s3.amazonaws.com/product-images/u5Kx9nEcRR6whI3NLjo0MAQnZyn3_fRzy6WIp9ZA73dA.png",
  "https://streamr-public.s3.amazonaws.com/product-images/Ir_tSV2SRtGLXdO1TnCwHQW6Y2ZM9gSa-1FYB4zWgBXg.jpg",
  "https://streamr-public.s3.amazonaws.com/product-images/lYdrpZamTTiy_emLw93viwFxM6_nLkQwGokzsObLRoBA.png",
  "https://streamr-public.s3.amazonaws.com/product-images/KQ1Bj0sQQWC_dfCjkUGsEA_WBsGnFxQI6SvEd6RI4DOw.png",
];

export default {
  name: "home",
  data() {
    return {
      loading: true,
      list: [],
    };
  },
  methods: {
    async getDtList() {
      this.loading = true;
      const res = await getDtList();

      this.list = res.dt_list.map((item, index) => {
        item.fig = images[index % 4];
        return item;
      });

      this.loading = false;
    },
  },
  async mounted() {
    this.getDtList();
  },
};
</script>

<style lang="less" scoped>
.home {
  .input-wrapper {
    text-align: center;
    padding: 40px;

    .title {
      font-size: 18px;
      margin-bottom: 20px;
      color: rgb(114, 114, 114);
    }
  }

  .content-wrapper {
    .filters-bar {
      padding: 24px 80px;
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
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        img {
          width: 100%;
        }

        .dot {
          position: absolute;
          top: 0;
          left: 0;
          background: @primary-color;
          color: @white;
          border-bottom-right-radius: 8px;
          font-size: 13px;
          padding: 3px 5px;
        }

        .text-wrapper {
          padding: 18px;
          .name {
            font-size: 16px;
            font-weight: bold;
          }

          .desc {
            color: @text-color-2;
            margin-top: 4px;
          }
        }
      }
    }
  }

  .view-more {
    text-align: center;

    .ant-btn-round.ant-btn-lg {
      font-size: 14px;
      color: #323232;
      background: rgba(239, 239, 239, 0.9);
      border-color: rgba(239, 239, 239, 0.9);
    }
  }
}

.ant-dropdown-menu-item {
  font-size: 16px;
  padding: 8px 20px;
}

@media screen and (max-width: 900px) {
  .home {
    .content-wrapper {
      .card-list {
        .card-item {
          width: 200px;
        }
      }
    }
  }
}
</style>

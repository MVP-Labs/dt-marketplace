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
        <div class="bar-content">
          <a-dropdown>
            <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
              All products
              <a-icon type="down" />
            </a>
            <a-menu slot="overlay">
              <a-menu-item key="All products">All Products</a-menu-item>
              <a-menu-item key="EN">Data Products</a-menu-item>
              <a-menu-item key="ES">Data Unions</a-menu-item>
            </a-menu>
          </a-dropdown>

          <a-dropdown>
            <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
              Category
              <a-icon type="down" />
            </a>
            <a-menu slot="overlay">
              <a-menu-item key="Account">Dataset</a-menu-item>
              <a-menu-item key="Settings">Computa</a-menu-item>
            </a-menu>
          </a-dropdown>
        </div>
      </div>

      <a-spin :spinning="loading" size="large">
        <div class="card-list">
          <a-card
            v-for="item in list"
            :key="item.dt"
            class="card-item"
            :bordered="false"
            @click="$router.push(`/detail/${item.dt}`)"
          >
            <div class="img-wrapper">
              <div class="dot" v-if="item.union_or_not">Data Union</div>
              <img :src="item.fig" />
            </div>

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
    require("./images/1.jpeg"),
    require("./images/2.jpeg"),
    require("./images/3.jpeg"),
    require("./images/4.jpeg"),
    require("./images/5.png"),
    require("./images/6.jpeg"),
    require("./images/7.jpeg"),
    require("./images/8.jpeg"),
    require("./images/9.png"),
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
          item.fig = images[index % 8];
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
        font-size: 19px;
        margin-bottom: 20px;
        color: rgb(114, 114, 114);
      }
    }

    .content-wrapper {
      .filters-bar {
        font-size: 17px;
        background: @white;

        .bar-content {
          width: 1280px;
          margin: 0 auto;
          padding: 24px 0;
        }

        .ant-dropdown-trigger {
          margin-right: 40px;
        }
      }

      .card-list {
        min-height: 240px;
        width: 1280px;
        margin: 20px auto;
        display: flex;
        flex-wrap: wrap;
        /deep/.ant-card-body {
          padding: 0;
        }
        .card-item {
          cursor: pointer;
          width: 240px;
          margin-bottom: 20px;
          margin-right: 20px;
          border-radius: 4px;
          overflow: hidden;
          position: relative;
          &:nth-child(5n) {
            margin-right: 0;
          }

          .img-wrapper {
            width: 240px;
            height: 160px;
            position: relative;
            &:hover {
              &:after {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.4);
                content: "";
                transition: all 0.3s;
              }
            }
            img {
              width: 240px;
              height: 160px;
              object-fit: cover;
            }
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
            padding: 14px 0;
            background: @background-color;
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

  @media screen and (max-width: 1280px) {
    .home {
      .content-wrapper {
        .filters-bar {
          .bar-content {
            width: 240px * 4 + 60px;
          }
        }

        .card-list {
          width: 240px * 4 + 60px;

          .card-item {
            &:nth-child(5n) {
              margin-right: 20px;
            }

            &:nth-child(4n) {
              margin-right: 0px;
            }
          }
        }
      }
    }
  }
</style>

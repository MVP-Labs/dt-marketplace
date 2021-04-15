<template>
  <div class="home">
    <div class="home-navbar">
      <div class="logo-wrapper">
        <img alt="DataTracer logo" src="../assets/logo.png" />
        <div class="text">DataTracer</div>
      </div>
    </div>
    <div class="home-search">
      <div class="search-title">Trace the data lifecycle</div>
      <a-input-group compact>
        <a-select
          default-value="Task"
          size="large"
          :dropdownMatchSelectWidth="false"
          style="width: 8%; min-width: 72px"
        >
          <a-select-option value="Task"> Task </a-select-option>
          <a-select-option value="Job"> Job </a-select-option>
          <a-select-option value="Owner"> Owner </a-select-option>
          <a-select-option value="Dt"> Dt </a-select-option>
        </a-select>
        <a-input-search
          placeholder="Search by Data Token"
          enter-button
          size="large"
          style="width: 30%; min-width: 290px"
          @search="onSearch"
        />
      </a-input-group>

      <!-- <div class="search-tips">Trace the data lifecycle...</div> -->
    </div>

    <div class="home-num">
      <div class="num-item">
        <img src="../assets/icons/icon-1.svg" />
        <div class="right-wrapper">
          <div class="name">DataToken Num</div>
          <div class="value">325</div>
        </div>
      </div>
      <div class="num-item">
        <img src="../assets/logo.png" />
        <div class="right-wrapper">
          <div class="name">Template Num</div>
          <div class="value">15</div>
        </div>
      </div>
      <div class="num-item">
        <img src="../assets/icons/icon-3.svg" />
        <div class="right-wrapper">
          <div class="name">Task Num</div>
          <div class="value">10</div>
        </div>
      </div>
      <div class="num-item">
        <img src="../assets/icons/icon-5.svg" />
        <div class="right-wrapper">
          <div class="name">Job Num</div>
          <div class="value">32</div>
        </div>
      </div>
    </div>

    <div class="home-block">
      <div class="block-title">
        <div class="left">Result for dt:ownership:ec60...57df</div>

        <div class="right">
          <a-button color="rgba(119,131,143,.1)" @click="viewPath(item)">
            View Path
          </a-button>
        </div>
      </div>
      <div class="block-item" v-for="(item, index) in list" :key="index">
        <div class="item">
          <div class="circle">{{ item.dt }}</div>
        </div>
        <div class="item">{{ item.job }}</div>
        <div class="item">{{ item.task }}</div>
        <div class="item">{{ item.solver }}</div>
        <div class="item">{{ item.demander }}</div>
        <div class="item">{{ item.time }}</div>
      </div>
    </div>

    <div class="home-footer">
      <div class="footer-left">
        <img
          src="https://cn.etherscan.com/images/world-map-white.png"
          class="bg"
        />

        <div class="text-wrapper">
          <div class="text">Powered by Ownership Labs</div>
        </div>
      </div>

      <div class="footer-right">
        <div class="right-item">
          <div class="title">Company</div>

          <div class="item" v-for="item in company" :key="item.text">
            {{ item.text }}
          </div>
        </div>

        <div class="right-item">
          <div class="title">Community</div>

          <div class="item" v-for="item in community" :key="item.text">
            {{ item.text }}
          </div>
        </div>

        <div class="right-item">
          <div class="title">Other Products</div>

          <div class="item" v-for="item in products" :key="item.text">
            {{ item.text }}
          </div>
        </div>
      </div>
    </div>

    <Modal ref="modal" />
  </div>
</template>

<script>
import Modal from "./Madal";
export default {
  name: "Home",
  components: {
    Modal,
  },
  data() {
    return {
      list: [
        {
          dt: "Dt",
          job: "job 3",
          task: "task 1",
          solver: "Solver Org3",
          demander: "Demander: Org7",
          time: "2 hours ago",
        },
        {
          dt: "Dt",
          job: "job 4",
          task: "task 1",
          solver: "Solver Org3",
          demander: "Demander: Org7",
          time: "4 hours ago",
        },
        {
          dt: "Dt",
          job: "job 5",
          task: "task 2",
          solver: "Solver Org3",
          demander: "Demander: Org7",
          time: "6 hours ago",
        },
        {
          dt: "Dt",
          job: "job 8",
          task: "task 4",
          solver: "Solver Org5",
          demander: "Demander: Org8",
          time: "8 hours ago",
        },
        {
          dt: "Dt",
          job: "job 10",
          task: "task 4",
          solver: "Solver Org5",
          demander: "Demander: Org8",
          time: "10 hours ago",
        },
        {
          dt: "Dt",
          job: "job 12",
          task: "task 6",
          solver: "Solver Org4",
          demander: "Demander: Org9",
          time: "12 hours ago",
        },
        {
          dt: "Dt",
          job: "job 14",
          task: "task 7",
          solver: "Solver Org1",
          demander: "Demander: Org10",
          time: "14 hours ago",
        },
      ],
      company: [
        {
          text: "About Us",
        },
        {
          text: "Advertise",
        },
        {
          text: "Contact Us",
        },
        {
          text: "Brand Assets",
        },
        {
          text: "Careers",
        },
        {
          text: "Terms of Service",
        },
      ],
      community: [
        {
          text: "Developer APIs",
        },
        {
          text: "Knowledge Base",
        },
        {
          text: "Newsletter",
        },
        {
          text: "Network Status",
        },
      ],
      products: [
        {
          text: "Blockscan",
        },
        {
          text: "Diem Block Explorer",
        },
        {
          text: "ETHProtect",
        },
        {
          text: "Binace BSC Explorer",
        },
        {
          text: "Fantom Chain Explorer",
        },
      ],
    };
  },
  methods: {
    onSearch() {},
    viewPath(item) {
      this.$refs.modal.open(item);
    },
  },
};
</script>

<style lang="less" scoped>
@search-input-height: 46px;
@margin: 50px;

.home {
  &-navbar {
    display: flex;
    align-items: center;
    padding: 16px @margin;
    box-shadow: 0 1px 10px rgb(151 164 175 / 10%);
    background: @white;
    .logo-wrapper {
      display: flex;
      align-items: center;
      img {
        width: 40px;
      }

      .text {
        margin-left: 8px;
        font-size: 18px;
        font-weight: bold;
        color: #21325b;
      }
    }
  }
  &-search {
    background-color: #21325b;
    height: 264px;
    padding: @margin;
    background-image: url("../assets/icons/shapes.svg");

    .search-title {
      color: @white;
      font-size: 22px;
      margin-bottom: 12px;
    }

    .search-tips {
      color: hsla(0, 0%, 100%, 0.7);
      margin-top: 12px;
    }

    /deep/ .ant-select-lg {
      .ant-select-selection--single {
        height: @search-input-height;
      }

      .ant-select-selection__rendered {
        line-height: @search-input-height;
      }

      .ant-select-arrow {
        right: 8px;
      }
    }

    /deep/.ant-input-lg {
      height: @search-input-height;
    }

    /deep/.ant-btn-lg {
      height: @search-input-height;
    }
  }

  &-num {
    display: flex;
    border: 1px solid @border-color;
    margin: -50px @margin 0;
    box-shadow: 0 1px 5px rgb(189 197 209 / 20%);
    background: @white;
    border-radius: 8px;
    padding: 20px 0;

    .num-item {
      padding: 20px;
      flex: 1;
      display: flex;
      align-items: center;
      border-right: 1px solid @border-color;
      justify-content: center;

      &:last-child {
        border: none;
      }

      img {
        width: 42px;
      }

      .right-wrapper {
        margin-left: 40px;

        .name {
          color: #4a4f55;
          font-size: 15px;
        }

        .value {
          font-size: 16px;
          margin-top: 4px;
        }
      }
    }
  }

  &-block {
    border: 1px solid @border-color;
    margin: 20px @margin;
    box-shadow: 0 0.5rem 1.2rem rgb(189 197 209 / 20%);
    background: @white;
    border-radius: 8px;
    padding: 8px 0;
    .block-title {
      padding: 16px 20px;
      font-weight: bold;
      font-size: 18px;
      border-bottom: 1px solid @border-color;
      display: flex;
      align-items: center;
      justify-content: space-between;

      /deep/.ant-btn {
        color: #77838f;
        background: rgba(119, 131, 143, 0.1);
      }
    }

    .block-item {
      padding: 18px 12px;
      display: flex;

      .item {
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 1;

        .circle {
          color: #77838f;
          background: rgba(119, 131, 143, 0.1);
          width: 50px;
          height: 50px;
          line-height: 50px;
          font-weight: bold;
          border-radius: 50%;
          font-size: 15px;
        }
      }
    }
  }

  &-footer {
    background-color: #21325b;
    height: 264px;
    padding: 28px @margin;
    background-image: url("../assets/icons/shapes-2.svg");
    position: relative;
    display: flex;

    .bg {
      width: 200px;
      position: absolute;
      left: 100px;
      top: 80px;
    }

    .footer-left {
      flex: 1;
      .text-wrapper {
        display: flex;
        align-items: center;
        img {
          width: 20px;
        }

        .text {
          color: @white;
          font-size: 20px;
          margin-left: 12px;
        }
      }
    }

    .footer-right {
      display: flex;

      .right-item {
        width: 220px;
        margin-left: 80px;

        .title {
          color: white;
          padding-bottom: 9px;
          border-bottom: 1px solid rgba(231, 234, 243, 0.2);
        }

        .item {
          color: hsla(0, 0%, 100%, 0.7);
          margin-top: 9px;
          font-size: 12px;
          cursor: pointer;

          &:hover {
            color: @white;
          }
        }
      }
    }
  }
}

@media screen and (max-width: 768px) {
  .home {
    &-navbar {
      padding: 10px 16px;
    }

    &-search {
      padding: 40px 0 40px 16px;
    }

    &-num {
      margin: -80px 16px 0;
      flex-wrap: wrap;
      .num-item {
        width: 50%;
        flex: none;
        padding: 8px 8px 8px 16px;

        img {
          width: 28px;
          flex-shrink: 0;
        }

        .right-wrapper {
          flex: 1;
          margin-left: 20px;

          .name {
            font-size: 14px;
          }
        }
      }
    }

    &-block {
      margin: 20px 16px;
    }

    &-footer {
      display: block;
      height: 540px;
      padding: 16px 24px;

      .footer-left {
        .text-wrapper {
          .text {
            margin-left: 0;
            margin-bottom: 8px;
          }
        }
      }

      .footer-right {
        display: block;

        .right-item {
          margin-left: 0;
          margin-bottom: 8px;

          .title {
            padding-bottom: 8px;
          }

          .item {
            margin-top: 6px;
          }
        }
      }
    }
  }
}
</style>

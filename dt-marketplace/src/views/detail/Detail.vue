<template>
  <a-spin :spinning="loading" size="large">
    <div class="detail">
      <div class="detail-content" v-if="!loading">
        <div class="detail-info">
          <img :src="dt_info.fig" class="fig" />
          <div class="right-info">
            <div class="name">{{ dt_info.name }}</div>

            <div class="desc-item">
              <a class="label" @click="copy(dt_info.owner)">Owner</a>
            </div>

            <div class="desc-item">
              <div class="label">
                Sold by <a>{{ dt_info.issuer }}</a>
              </div>
            </div>
          </div>
        </div>

        <div class="detail-desc">
          <div class="desc-wrapper" v-html="dt_info.desc"></div>

          <div class="type-wrapper">
            <div class="label">Asset type</div>
            <div class="value">{{ dt_info.type }}</div>
          </div>
        </div>

        <div class="detail-table">
          <a-table
            :columns="columns"
            :data-source="service_lists"
            :pagination="false"
          >
            <div slot="action">
              <a-button color="rgba(119,131,143,.1)" @click="show = true">
                Constrains
              </a-button>

              <a-button style="margin-left: 20px" shape="circle" icon="plus" />
            </div>
          </a-table>
        </div>
      </div>
    </div>

    <a-modal
      v-model="show"
      title=""
      on-ok="handleOk"
      :footer="null"
      :centered="true"
      width="880px"
    >
      <pre id="result" v-html="json"></pre>
    </a-modal>
  </a-spin>
</template>

<script>
import { getDtDetail } from "../../api/index";
import { syntaxHighlight } from "../../utils";

const columns = [
  {
    title: "SERVICE",
    dataIndex: "sid",
    key: "sid",
    width: 100,
    align: "center",
  },
  {
    title: "OPERATOR",
    dataIndex: "op",
    key: "op",
    width: 100,
    align: "center",
  },
  {
    title: "PRICE",
    dataIndex: "price",
    key: "price",
    width: 100,
    align: "center",
  },
  {
    title: "ACTION",
    dataIndex: "action",
    key: "action",
    scopedSlots: { customRender: "action" },
    width: 100,
    align: "center",
  },
];

export default {
  data() {
    return {
      loading: false,
      dt_info: {},
      service_lists: [],
      union_data: [],
      columns,
      show: false,
      json: "",
    };
  },
  mounted() {
    this.getDtDetail();
  },
  methods: {
    copy(text) {
      this.$copyText(text).then(() => {
        this.$message.info("复制成功");
      });
    },
    async getDtDetail() {
      this.loading = true;
      const res = await getDtDetail(this.$route.params.dt);
      this.loading = false;
      this.dt_info = res.dt_info;
      this.dt_info.desc = `Digital Assets Power Play Ltd. is the leading provider of algorithmic trading tools, services and software.<br />
Only on the Streamr marketplace, this exclusive edition of DPP DataStreams offers access to a variety of live crypto data from five leading exchanges including Bitstamp, Coinbase Pro, Kraken, Bitmex, and Tokens. Connect to real-time trades, L1/L2 order books, OHLCV, technical indicators, indices, and news & sentiment feeds. Analyzing the crypto market, finding correlations, and discovering trading opportunities has never been easier.`;
      this.dt_info.fig =
        "https://streamr-public.s3.amazonaws.com/product-images/Ir_tSV2SRtGLXdO1TnCwHQW6Y2ZM9gSa-1FYB4zWgBXg.jpg";
      this.service_lists = res.service_lists.map((item) => {
        this.json = syntaxHighlight(
          JSON.parse(JSON.stringify(item.constrains))
        );
        item.op = item.op || "N/A";
        return item;
      });
      this.union_data = res.union_data;
    },
  },
};
</script>

<style lang="less" scoped>
.detail {
  background: @white;
  padding: 60px;
  min-height: 600px;
  .detail-content {
    width: 1080px;
    margin: 0 auto;
  }

  .detail-info {
    display: flex;
    align-items: center;
    border-bottom: 1px solid @border-color;
    padding-bottom: 40px;
    .fig {
      width: 480px;
      height: 300px;
      object-fit: cover;
      border-radius: 8px;
    }

    .right-info {
      margin-left: 100px;
      flex: 1;
      .name {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 12px;
        padding-left: 12px;
      }

      .desc-item {
        display: flex;
        border-bottom: 1px solid @border-color;
        padding: 18px 12px;
        .label {
          width: 180px;
          font-size: 16px;
        }

        .value {
          flex: 1;
          color: rgba(0, 0, 0, 0.65);
          font-size: 15px;
        }
      }
    }
  }

  .detail-desc {
    margin-top: 40px;
    display: flex;

    .desc-wrapper {
      flex: 1;
      margin-right: 140px;
      font-size: 16px;
      color: rgb(82, 82, 82);
    }

    .type-wrapper {
      width: 272px;
      background: @background-color;
      padding: 32px 24px;
      border-radius: 8px;

      .label {
        font-size: 18px;
        margin-bottom: 20px;
      }

      .value {
        color: rgb(82, 82, 82);
        font-size: 16px;
      }
    }
  }

  .detail-table {
    margin-top: 80px;

    /deep/.ant-table-thead > tr > th {
      background: rgb(239, 239, 239);
      border-bottom: 1px solid rgb(239, 239, 239);
    }

    /deep/.ant-table-tbody > tr > td {
      background: rgb(248, 248, 248);
      border-bottom: none;
    }

    /deep/.ant-table-row {
      border-bottom: 1px solid rgb(239, 239, 239);
      &:last-child {
        border-bottom: none;
      }
    }
  }
}
</style>

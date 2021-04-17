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

        <div class="detail-tree" v-if="this.option.series[0].data.length != 0">
          <div class="tree-top">Data Union</div>
          <div class="tree-bottom">
            <Chart style="height: 540px" :option="option" />
          </div>
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
import Chart from "../../components/Chart";

const data = {
  name: "",
  value: "owner: user1 <br/> issuer: org1",
  children: [
    {
      name: "",
      value: "aggregator: org2 <br /> service: leaf_sid0",
      children: [
        {
          name: "",
          value: "aggregator: org3 <br /> service: union_sid0",
          children: [
            {
              name: "",
              value: "job: 3 <br /> task: 1 <br /> demander: org",
              itemStyle: {
                color: "#21325b",
              },
            },
            {
              name: "",
              value: "job: 4 <br /> task: 1 <br /> demander: org7",
              itemStyle: {
                color: "#21325b",
              },
            },
            {
              name: "",
              value: "job: 5 <br /> task: 2 <br /> demander: org7",
              itemStyle: {
                color: "#21325b",
              },
            },
          ],
        },
      ],
    },
    {
      name: "",
      value: "aggregator: org4 <br /> service: leaf_sid1",
      children: [
        {
          name: "",
          value: "aggregator: org5 <br /> service: union_sid0",
          children: [
            {
              name: "",
              value: "job: 8 <br /> task: 4 <br /> demander: org8",
              itemStyle: {
                color: "#21325b",
              },
            },
            {
              name: "",
              value: "job: 10 <br /> task: 4 <br /> demander: org8",
              itemStyle: {
                color: "#21325b",
              },
            },
          ],
        },
        {
          name: "",
          value: "job: 12 <br /> task: 6 <br /> demander: org9",
          itemStyle: {
            color: "#21325b",
          },
        },
      ],
    },
    {
      name: "",
      value: "job: 14, task: 7 <br /> demander: org10",
      itemStyle: {
        color: "#21325b",
      },
    },
  ],
};

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
  components: {
    Chart,
  },
  data() {
    return {
      loading: false,
      dt_info: {},
      service_lists: [],
      union_data: [],
      columns,
      show: false,
      json: "",
      option: {
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove",
          formatter(params) {
            let str = "";
            if (typeof params.data.values == "string") {
              return "dt:" + params.data.values;
            } else {
              for (var key in params.data.values) {
                str += key + ":" + params.data.values[key] + "<br />";
              }
              return str;
            }
          },
        },
        series: [
          {
            type: "tree",

            data: [data],

            top: "1%",
            left: "7%",
            bottom: "1%",
            right: "20%",
            itemStyle: {
              color: "#21325b",
              borderColor: "#21325b",

              borderWidth: 2,
            },

            symbolSize: 7,
            symbol: "circle",

            label: {
              position: "left",
              verticalAlign: "middle",
              align: "right",
              fontSize: 14,
            },

            leaves: {
              label: {
                position: "right",
                verticalAlign: "middle",
                align: "left",
              },
              itemStyle: {
                color: "#fff",
                borderColor: "#e23a3a",
              },
            },

            emphasis: {
              // focus: "descendant",
            },

            expandAndCollapse: true,
            animationDuration: 550,
            animationDurationUpdate: 750,
          },
        ],
      },
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

      this.dt_info.fig =
        "https://streamr-public.s3.amazonaws.com/product-images/Ir_tSV2SRtGLXdO1TnCwHQW6Y2ZM9gSa-1FYB4zWgBXg.jpg";
      this.service_lists = res.service_lists.map((item) => {
        this.json = syntaxHighlight(
          JSON.parse(JSON.stringify(item.constrains))
        );
        item.op = item.op || "N/A";
        return item;
      });
      this.option.series[0].data = res.union_data ? [res.union_data] : [];
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
  .tree-top {
    height: 53px;
    line-height: 53px;
    background: #efefef;
    margin-top: 40px;
    padding-left: 40px;
    border-bottom: 1px solid #efefef;
  }
  .tree-bottom {
    background: #f8f8f8;
    border-bottom: none;
  }
}
</style>

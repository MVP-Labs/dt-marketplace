<template>
  <a-spin :spinning="loading" size="large">
    <div class="detail">
      <div class="detail-content" v-if="!loading">
        <div class="detail-info">
          <img :src="dt_info.fig" class="fig" />
          <div class="right-info">
            <div class="name">{{ dt_info.name }}</div>

            <div class="desc-item">
              <div class="label">Type</div>
              <div class="value">{{ dt_info.type }}</div>
            </div>

            <div class="desc-item">
              <a class="label" @click="copy(dt_info.owner)">Owner</a>
            </div>

            <div class="desc-item">
              <div class="label">Issuer</div>
              <div class="value">{{ dt_info.issuer }}</div>
            </div>
            <div class="desc-item">
              <div class="label">Decription</div>
              <div class="value">{{ dt_info.desc }}</div>
            </div>
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
                View constrains
              </a-button>

              <a-button style="margin-left: 12px" shape="circle" icon="plus" />
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
      width="840px"
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
    title: "SID",
    dataIndex: "sid",
    key: "sid",
  },
  {
    title: "OPERATOR",
    dataIndex: "op",
    key: "op",
  },
  {
    title: "PRICE",
    dataIndex: "price",
    key: "price",
  },
  {
    title: "ACTION",
    dataIndex: "action",
    key: "action",
    scopedSlots: { customRender: "action" },
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
      this.dt_info.fig =
        "https://streamr-public.s3.amazonaws.com/product-images/Ir_tSV2SRtGLXdO1TnCwHQW6Y2ZM9gSa-1FYB4zWgBXg.jpg";
      this.service_lists = res.service_lists.map((item) => {
        this.json = syntaxHighlight(
          JSON.parse(JSON.stringify(item.constrains))
        );
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
    .fig {
      width: 440px;
      border-radius: 8px;
    }

    .right-info {
      margin-left: 40px;
      flex: 1;
      .name {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
      }

      .desc-item {
        display: flex;
        border-bottom: 1px solid @border-color;
        padding: 18px 0;
        .label {
          width: 180px;
          text-align: center;
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

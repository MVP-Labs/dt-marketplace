<template>
  <a-modal
    v-model="show"
    class="modal-tree"
    title=""
    on-ok="handleOk"
    :footer="null"
    :width="840"
    :height="540"
    :centered="true"
  >
    <Chart style="height: 540px" :option="option" />
  </a-modal>
</template>

<script>
import Chart from "../components/Chart";

export default {
  components: {
    Chart,
  },
  props: {
    lifecycle: {
      type: Object,
      default() {
        return {};
      },
    },
    // show: {
    //   type: Boolean,
    //   default: true
    // }
  },
  data() {
    return {
      show: false,
      option: {
        backgroundColor: "#f8f8f8",
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove",
          formatter(params) {
            console.log("formatter -> params", params);
            let str = "";
            for (var key in params.data.values) {
              console.log(key);
              str += key + ":" + params.data.values[key] + "<br />";
            }
            return str;
          },
        },
        series: [
          {
            type: "tree",
            data: [],
            // data: [{
            //   name: "",
            //   value: "aggregator: org2 <br /> service: leaf_sid0",
            //   children: [
            //     {
            //       name: "",
            //       value: "aggregator: org3 <br /> service: union_sid0",
            //       children: [
            //         {
            //           name: "",
            //           value: "job: 3 <br /> task: 1 <br /> demander: org",
            //           itemStyle: {
            //             color: "#21325b",
            //           },
            //         },
            //         {
            //           name: "",
            //           value: "job: 4 <br /> task: 1 <br /> demander: org7",
            //           itemStyle: {
            //             color: "#21325b",
            //           },
            //         },]
            //     }
            //   ],
            // }],

            top: "1%",
            left: "7%",
            bottom: "1%",
            right: "20%",
            itemStyle: {
              borderColor: "#e23a3a",
              color: "#fff",
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
                color: "#21325b",
                borderColor: "#21325b",
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
    this.$nextTick(() => {
      this.option.series[0].data = [this.lifecycle];
    });
  },
  methods: {
    open() {
      this.show = true;
    },
  },
};
</script>

<style lang="less" scoped>
.modal-tree {
  background-color: #f8f8f8;
  ::v-deep {
    .ant-modal-body {
      background-color: #f8f8f8;
      padding: 0;
    }
  }
}
</style>

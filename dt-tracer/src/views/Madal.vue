<template>
  <a-modal
    v-model="show"
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

export default {
  components: {
    Chart,
  },
  data() {
    return {
      show: false,
      option: {
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove",
          formatter(params) {
            return params.data.value;
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
              color: "#fff",
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
            },

            emphasis: {
              // focus: "descendant",
            },

            expandAndCollapse: false,
            animationDuration: 550,
            animationDurationUpdate: 750,
          },
        ],
      },
    };
  },
  methods: {
    open() {
      this.show = true;
    },
  },
};
</script>

<style></style>

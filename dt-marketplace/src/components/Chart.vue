<template>
  <div ref="chartDom"></div>
</template>

<script>
  import * as echarts from 'echarts'

  import { debounce } from 'lodash'

  export default {
    props: {
      option: {
        type: Object,
        default: () => {},
      },
    },
    watch: {
      option: {
        handler(val) {
          this.chart.setOption(val)
        },
        deep: true,
      },
    },
    created() {
      this.resize = debounce(this.resize, 300)
    },
    mounted() {
      this.renderChart()
      addEventListener(this.$refs.chartDom, this.resize)
    },
    beforeDestroy() {
      removeEventListener(this.$refs.chartDom, this.resize)
      this.chart.dispose()
      this.chart = null
    },
    methods: {
      resize() {
        console.log('resize')
        this.chart.resize()
      },
      renderChart() {
        let _this = this
        // 基于准备好的dom，初始化echarts实例
        this.chart = echarts.init(this.$refs.chartDom)
        this.chart.setOption(this.option)
        this.chart.on('dblclick', function (param) {
          let flat = Object.prototype.hasOwnProperty.call(
            param.data.values,
            'dt'
          )
          if (flat) {
            let routeUrl = _this.$router.resolve({
              path: '/detail/' + param.data.values.dt,
            })
            window.open('http://localhost:8080/' + routeUrl.href, '_blank')
          }
        })
      },
    },
  }
</script>

<style></style>

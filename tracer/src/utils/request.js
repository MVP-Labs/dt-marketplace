import axios from 'axios'
import Vue from 'vue'

const CODE_OK = 'Success'
let loadCount = 0 // 当前请求 loading 的数量

const request = axios.create({
  timeout: 30000,
  baseURL: 'http://0.0.0.0:8000',
  _cache: false, // 接口缓存
  _loading: false, // 是否显示 loading
  _toast: true, // 报错后是否显示 toast
})

const loading = {
  open(text = '加载中') {
    Vue.prototype.$message.loading({
      content: text,
      duration: 0,
    })
  },
  close() {
    setTimeout(() => {
      Vue.prototype.$message.destroy()
    }, 500)
  },
}

request.interceptors.request.use(
  (config) => {
    if (config._loading && ++loadCount > 0) {
      loading.open()
    }

    return config
  },
  (err) => {
    Promise.reject(err)
  }
)

request.interceptors.response.use(
  (res) => {
    const { config, data } = res

    if (config._loading && --loadCount <= 0) {
      loading.close()
    }

    // success
    if (data.result === CODE_OK) {
      return data
    } else {
      console.log(config)
      config._toast &&
        Vue.prototype.$message.error({
          content: data.errMsg || '当前服务器繁忙，稍后再试哦~',
        })
    }

    return Promise.reject(data)
  },
  (err) => {
    const { config } = err

    if (config._loading && --loadCount <= 0) {
      loading.close()
    }

    config._toast &&
      Vue.prototype.$message.error({
        content: err.errMsg || '当前服务器繁忙，稍后再试哦~',
      })

    return Promise.reject(err)
  }
)

export default request

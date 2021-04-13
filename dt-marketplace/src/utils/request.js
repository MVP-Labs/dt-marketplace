import axios from "axios";
import Vue from "vue";
import { getToken, clearToken } from "./auth";

const CODE_OK = 0;
let loadCount = 0; // 当前请求 loading 的数量

const request = axios.create({
  timeout: 10000,
  baseURL: process.env.apiUrl,
  _cache: false, // 接口缓存
  _loading: false, // 是否显示 loading
  _toast: true, // 报错后是否显示 toast
});

const loading = {
  open(text = "加载中") {
    Vue.prototype.$message.loading({
      content: text,
      duration: 0,
    });
  },
  close() {
    setTimeout(() => {
      Vue.prototype.$message.destroy();
    }, 500);
  },
};

request.interceptors.request.use(
  (config) => {
    if (getToken()) {
      config.headers["Authorization"] = `Bearer ${getToken()}`;
    }

    if (config._loading && ++loadCount > 0) {
      loading.open();
    }

    return config;
  },
  (err) => {
    Promise.reject(err);
  }
);

request.interceptors.response.use(
  (res) => {
    const { config, data } = res;

    if (config._loading && --loadCount <= 0) {
      loading.close();
    }

    // success
    if (data.errCode === CODE_OK) {
      return data;
    } else {
      console.log(config);
      config._toast &&
        Vue.prototype.$message.error({
          content: data.errMsg || "当前服务器繁忙，稍后再试哦~",
        });

      if (data.errCode === 401) {
        clearToken();

        setTimeout(() => {
          location.reload();
        }, 1000);
        return;
      }
    }

    return Promise.reject(data);
  },
  (err) => {
    const { config } = err;

    if (config._loading && --loadCount <= 0) {
      loading.close();
    }

    config._toast &&
      Vue.prototype.$message.error({
        content: err.errMsg || "当前服务器繁忙，稍后再试哦~",
      });

    return Promise.reject(err);
  }
);

export default request;

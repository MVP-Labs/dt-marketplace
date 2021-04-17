"use strict";
const path = require("path");

function resolve(dir) {
  return path.join(__dirname, dir);
}

module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "https://zszhuan-dev.oss-cn-hangzhou.aliyuncs.com/web/data-tracer/"
      : "/",
  css: {
    loaderOptions: {
      less: {
        modifyVars: {
          "text-color": "#262626",
        },
        javascriptEnabled: true,
      },
    },
  },
  pluginOptions: {
    "style-resources-loader": {
      preProcessor: "less",
      patterns: [
        resolve("src/styles/var.less"),
        resolve("src/styles/mixins.less"),
      ],
    },
  },
  devServer: {
    // p`roxy: {
    //   "/api": {
    //     target: "http://128.14.226.29:3000",
    //     ws: true,
    //     changOrigin: true
    //     // pathRewrite: {
    //     //   "/sys/v1/": "/sys/v1/"
    //     // }
    //   }
    // }`
  },
};

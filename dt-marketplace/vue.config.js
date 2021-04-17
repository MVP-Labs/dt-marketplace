"use strict";
const path = require("path");

function resolve(dir) {
  return path.join(__dirname, dir);
}

module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "https://zszhuan-dev.oss-cn-hangzhou.aliyuncs.com/web/dt-marketplace/"
      : "/",
  css: {
    loaderOptions: {
      less: {
        modifyVars: {
          "primary-color": "#17a2b8",
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
};

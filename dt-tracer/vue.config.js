'use strict'
const path = require('path')

function resolve(dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  publicPath:
    process.env.NODE_ENV === 'production'
      ? 'https://zszhuan-dev.oss-cn-hangzhou.aliyuncs.com/web/data-tracer/'
      : '/',
  css: {
    loaderOptions: {
      less: {
        modifyVars: {
          'text-color': '#262626',
        },
        javascriptEnabled: true,
      },
    },
  },
  devServer: {
    port: 8081, // 端口号
  },
  pluginOptions: {
    'style-resources-loader': {
      preProcessor: 'less',
      patterns: [
        resolve('src/styles/var.less'),
        resolve('src/styles/mixins.less'),
      ],
    },
  },
}

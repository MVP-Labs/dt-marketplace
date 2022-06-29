import request from '../utils/request'

export function getStatInfo() {
  return request({
    url: '/api/get_stat_info',
  })
}

export function traceByDt(dt) {
  return request({
    url: '/api/trace_by_dt',
    method: 'post',
    data: dt,
  })
}

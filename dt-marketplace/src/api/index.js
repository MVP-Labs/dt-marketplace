import request from "../utils/request";

export function getDtList() {
  return request({
    url: "/api/get_dt_list",
  });
}

export function getDtDetail(dt) {
  return request({
    url: "/api/view_dt_details",
    method: "post",
    data: {
      dt,
    },
  });
}

export function getQueryString(name) {
  const res = location.href.match(new RegExp("[?&]" + name + "=([^&#]+)", "i"));

  if (res == null || res.length < 1) {
    return null;
  }

  return decodeURIComponent(res[1]);
}

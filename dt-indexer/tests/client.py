"""Client module."""
# Copyright 2021 The ownership-dapp Authors
# SPDX-License-Identifier: LGPL-2.1-only

import requests
import json

response = requests.get(f"http://127.0.0.1:8000/api/get_stat_info",
                        headers={'content-type': 'application/json'}, timeout=5)
print(response.text)
print(response.status_code)
print(response.json())

response = requests.get(f"http://127.0.0.1:8000/api/get_dt_list",
                        headers={'content-type': 'application/json'}, timeout=30)

print(response.text)
print(response.status_code)
print(response.json())

data = {'dt': "dt:ownership:b1a0eb5086a54cc2a79e13ee645dd4c9c5d28dcd071e43ba83c74c06164c509a"}

response = requests.post(f"http://127.0.0.1:8000/api/view_dt_details", data=json.dumps(data),
                         headers={'content-type': 'application/json'}, timeout=5)

print(response.text)
print(response.status_code)
print(response.json())

response = requests.post(f"http://127.0.0.1:8000/api/trace_by_dt", data=json.dumps(data),
                         headers={'content-type': 'application/json'}, timeout=5)
print(response.text)
print(response.status_code)
print(response.json())
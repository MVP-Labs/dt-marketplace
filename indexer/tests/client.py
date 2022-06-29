"""Client module."""
# Copyright 2021 The ownership-dapp Authors
# SPDX-License-Identifier: LGPL-2.1-only

import requests
import json

response = requests.get(f"http://0.0.0.0:8000/api/get_stat_info",
                        headers={'content-type': 'application/json'}, timeout=5)
print(response.text)
print(response.status_code)
print(response.json())

response = requests.get(f"http://0.0.0.0:8000/api/get_dt_list",
                        headers={'content-type': 'application/json'}, timeout=30)
print(response.text)
print(response.status_code)
print(response.json())


data = {'dt': "dt:ownership:6cdedef64614474697eaa2a912b67b56d08e9dc58e2f468698ac465078435804"}

response = requests.post(f"http://0.0.0.0:8000/api/view_dt_details", data=json.dumps(data),
                         headers={'content-type': 'application/json'}, timeout=5)
print(response.text)
print(response.status_code)
print(response.json())

data = {'dt': "dt:ownership:6f84a94e073e4185a7d9e3e52e0d0b6e82a360b823e34ba2984ff4eaa68aa20d"}

response = requests.post(f"http://0.0.0.0:8000/api/view_dt_details", data=json.dumps(data),
                         headers={'content-type': 'application/json'}, timeout=5)
print(response.text)
print(response.status_code)
print(response.json())

response = requests.post(f"http://127.0.0.1:8000/api/trace_by_dt", data=json.dumps(data),
                         headers={'content-type': 'application/json'}, timeout=5)
print(response.text)
print(response.status_code)
print(response.json())

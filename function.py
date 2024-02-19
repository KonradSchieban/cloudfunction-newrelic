# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import functions_framework
import requests
import json
import os

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):

    # Fetch data from Pub/Sub message
    data = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8')

    api_key = os.environ.get("API_KEY", "Specified environment variable API_KEY is not set.")
    api_url = os.environ.get('API_URL', "Specified environment variable API_URL is not set.")
    http_proxy  = os.environ.get("HTTP_PROXY", "Specified environment variable HTTP_PROXY is not set.")
    https_proxy  = os.environ.get("HTTPS_PROXY", "Specified environment variable HTTPS_PROXY is not set.")

    proxies = { 
                "http"  : http_proxy, 
                "https" : https_proxy
                }

    payload = {"data": data}

    headers =  {"Content-Type":"application/json",
                "Api-Key":api_key}

    response = requests.post(api_url, data=json.dumps(payload), headers=headers, proxies=proxies)
    print(response.json())
    print(response.status_code)

# New Relic / Cloud Function integration

This repository contains a sample implementation of a Google Cloud Function that sends log requests to New Relic via an HTTP Proxy. In my testing I configured Tinyproxy as a proxy server in my VPC.

Required environment variables for the Cloud Function:

 * `API_URL`: API endpoint of New Relic (most likely https://log-api.eu.newrelic.com/log/v1)
 * `HTTP_PROXY`: http://hostname:port
 * `HTTPS_PROXY`: http://hostname:port

Required *secret* environment variables for the Cloud Function:
 * `API_KEY`: API Key for New Relic

Example Pubsub Request message:
```
{
  "message": {
    "_comment": "data is base64 encoded string of 'Hello World'",
    "data": "SGVsbG8gV29ybGQ="
  }
}
```



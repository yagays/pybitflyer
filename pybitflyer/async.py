import time
import json
import hmac
import urllib
import hashlib
import asyncio
import aiohttp
import pybitflyer


class API(pybitflyer.API):

    def __init__(self, api_key=None, api_secret=None, timeout=None, loop=None):
        super(API, self).__init__(api_key, api_secret, timeout)
        self.loop = loop if loop else asyncio.get_event_loop()

    def _create_header_and_body(self, endpoint, method, params):
        if method == "POST":
            body = json.dumps(params)
        else:
            if params:
                body = "?" + urllib.parse.urlencode(params)
            else:
                body = ""

        if self.api_key and self.api_secret:
            access_timestamp = str(time.time())
            api_secret = str.encode(self.api_secret)
            text = str.encode(access_timestamp + method + endpoint + body)
            access_sign = hmac.new(api_secret,
                                   text,
                                   hashlib.sha256).hexdigest()
            auth_header = {
                "ACCESS-KEY": self.api_key,
                "ACCESS-TIMESTAMP": access_timestamp,
                "ACCESS-SIGN": access_sign,
                "Content-Type": "application/json"
            }

        else:
            auth_header = {}

        return auth_header, body

    # override
    async def request(self, endpoint, method="GET", params=None):
        url = self.api_url + endpoint
        header, body = self._create_header_and_body(endpoint, method, params)
        async with aiohttp.ClientSession(loop=self.loop) as s:
            try:
                if method == 'GET':
                    async with s.get(url, params=params, timeout=self.timeout, headers=header) as r:
                        try:
                            contents = await r.json()
                        except:
                            contents = await r.text()
                        return contents
                else:  # method == "POST":
                    async with s.post(url, data=json.dumps(params), timeout=self.timeout, headers=header) as r:
                        try:
                            contents = await r.json()
                        except:
                            contents = await r.text()
                        return contents
            except Exception as e:
                print(e)
                raise e

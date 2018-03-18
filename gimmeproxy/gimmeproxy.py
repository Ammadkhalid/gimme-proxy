import requests
from .exception import *

class GimmeProxy:

    endPoint = 'https://gimmeproxy.com/api/getProxy'

    def parseBody(self, req):
        try:
            return req.json()
        except ValueError:
            return req.text

    def request(self, proxy = None, **params):
        # send request
        if proxy is None:
            req = requests.get(self.endPoint, params=params)
        else:
            req = requests.get(self.endPoint, proxies={'https': proxy}, params=params)

        if req.ok:
            return self.parseBody(req)
        else:
            raise ProxiesLimitExceed('Proxies Limit exceed! content:\n{}'.format(req.text))

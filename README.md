# Gimme Proxy API package in python
```
└─[$] <git:(master*)> python
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from gimmeproxy import GimmeProxy
>>> GimmeProxy().request()
{'ip': '99.195.28.113', 'curl': 'socks5://99.195.28.113:14969', 'user-agent': True, 'port': '14969', 'type': 'socks5', 'country': 'US', 'speed': 32.28, 'websites': {'google': False, 'yelp': True, 'example': True, 'amazon': False}, 'tsChecked': 1521388636, 'ipPort': '99.195.28.113:14969', 'anonymityLevel': 1, 'otherProtocols': {}, 'referer': True, 'supportsHttps': True, 'cookies': True, 'get': True, 'post': True, 'protocol': 'socks5'}
>>>
```

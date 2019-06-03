from urllib import request
from urllib.request import ProxyHandler, build_opener
url='http://httpbin.org/ip'
proxy_handler=ProxyHandler({'http':'http://61.164.39.67:53281'})
opener=build_opener(proxy_handler)
resp=opener.open(url)
print(resp.read())
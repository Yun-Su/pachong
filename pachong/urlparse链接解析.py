from urllib import parse
url="http://www.baidu.com/s?wd=python&username=abc#1"
result=parse.urlparse(url)
print(result)#
#ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='', query='wd=python&username=abc', fragment='1')

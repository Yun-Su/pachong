from urllib import parse
url="http://www.baidu.com/s?wd=python&username=abc#1"
#一个示例链接
result=parse.urlsplit(url)
print(result)
print('scheme=',result.scheme)
print('netloc=',result.netloc)
print('path=',result.path)
#print('params',result.params)
#这玩意会报错,因为urllib无params的元素
print('query=',result.query)
print('fragment=',result.fragment)
#urlparse比urlsplit多了个params,其他保持一致
#例如url="http://www.baidu.com/s;hello?wd=python&username=abc#1"
#urlparse可以解析出hello关键字,而urlsplit则不能
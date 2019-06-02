from urllib import parse
url="http://www.baidu.com/s?wd=python&username=abc#1"
#一个示例链接
result=parse.urlparse(url)
print(result)#对url字段进行解析,输出内容如下
#ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='', query='wd=python&username=abc', fragment='1')
print('scheme',result.scheme)
print('netloc',result.netloc)
print('path',result.path)
print('params',result.params)
print('query',result.query)
print('fragment',result.fragment)
#
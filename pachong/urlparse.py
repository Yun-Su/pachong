from urllib import request
from urllib import parse
#对已编码的文件进行还原
params={'name':'张三','age':18,'greet':'helloworld'}
qs=parse.urlencode(params)
#将汉字转化为编码
print(qs)
#打印重新编码后的字符
result=parse.parse_qs(qs)
print(result)
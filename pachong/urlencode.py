from urllib import request
from urllib import parse
#params={'name':'张三',"age":18,"greet":"hello world"}
#result=parse.urlencode(params)
#print(result)#将汉字转化为对应的字符串编码

#url="http://www.baidu.com/s?wd=周杰伦"
#传入时函数无法将周杰伦转换为对应ascll,默认只识别英文字符数字,需要转换
url="http://www.baidu.com/s"
pd={"wd":"周杰伦"}
qs=parse.urlencode(pd)
#将"wd周杰伦"编码为函数可读形式
url=url+"?"+qs
print(url)#打印出 http://www.baidu.com/s?wd=周杰伦
resp=request.urlopen(url)
print(resp.read())
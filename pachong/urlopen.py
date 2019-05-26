from urllib import request
resp=request.urlopen("https://wwww.baidu.com")#读取网页
print(resp.read())
#print(resp.readline())读取一行
#print(resp.readlines())读取多行
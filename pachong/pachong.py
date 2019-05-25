from urllib import request
resp=request.urlopen("https://wwww.baidu.com")
print(resp.read())
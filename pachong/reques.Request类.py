from urllib import request
url='https://www.lagou.com/jobs/list_python?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput='
 
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

#部分网站做了反爬机制,所以要用定制请求头,请求头元素越多越真实,越不容易被识别出来
req=request.Request(url,headers=headers)
resp=request.urlopen(req)
print(resp.read())
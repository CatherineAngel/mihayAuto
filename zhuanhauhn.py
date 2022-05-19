import re

s = '''
GET https://api.gotokeep.com/tapers-webapp/run/group/grade/week?runGroupId=625fa1dff7bfd3000103ab7a&pageSize=50&pageNum=3 HTTP/1.1
Host: api.gotokeep.com
Connection: keep-alive
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1YTA4MGZiY2U2NjY4NjBhNjIwOTA5YWYiLCJ1c2VybmFtZSI6IkdyaWxMb3ZlciIsImF2YXRhciI6Imh0dHBzOi8vc3RhdGljMS5nb3Rva2VlcC5jb20vYXZhdGFyLzIwMTcvMTEvMTIvMTcvOWY5N2RmYjBmZGFkMGI4YmM2NDJiZTRkODY5NTdmYTBjNTg3MGYwOS5qcGciLCJfdiI6IjEiLCJfZWQiOiJ5TUVxcG9TNzRYdDV6WlNNSUNzZE1nPT0iLCJnZW5kZXIiOiJNIiwiZGV2aWNlSWQiOiIiLCJpc3MiOiJodHRwczovL3d3dy5nb3Rva2VlcC5jb20vIiwiZXhwIjoxNjc2MTg5ODM1LCJpYXQiOjE2NTI4NjE4MzV9.tlqzXa1ttuaXvPkHCggSo-C23nmsrqmbQ0OTyADDnbA
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat
content-type: application/json
openid: oGw-94o0Z7kSH7wl2JylwRvXGJ0Y
unionId: oLJRcuGX6BodIQhYkDAKmU8eWOUw
x-app-platform: wechatapp
x-locale: zh_CN
x-model: microsoft
x-network-type: wifi
x-os: Windows
x-os-version: 10
x-screen-height: 736
x-screen-width: 414
x-timestamp: 1652862038732
x-user-id: 5a080fbce666860a620909af
x-version-name: 3.2.0
x-wechatapp-id: wx192e59a8067e04e5
x-wechatapp-sdk: 2.19.2
x-wechatapp-wxversion: 3.4.0
Referer: https://servicewechat.com/wx192e59a8067e04e5/76/page-frame.html
Accept-Encoding: gzip, deflate, br


HTTP/1.1 200
Server: TencentWAF
Date: Wed, 18 May 2022 08:20:39 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Application-Context: tapers-webapp:9753
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Credentials: true
Content-Encoding: gzip


'''

s2 = re.sub(r'^([^:\n]+):?\s?(.*)$', r'"\1": "\2",', s, flags=re.M)
print(s2)
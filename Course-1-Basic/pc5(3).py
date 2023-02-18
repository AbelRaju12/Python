import requests
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print("GET request URL:",r.url)
#get?parametername=value&parametername=value

url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )

print("request body(get):", r.request.body)
print("request body(post):", r_post.request.body)

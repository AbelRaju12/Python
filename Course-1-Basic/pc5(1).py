#Rest API--> HTTP protocol
#URL-->scheme//:internetadress or base url/route
#status codes: 1xx-info|100-ok|2xx-sucess|3xx-redirection|300-multichoice|4xx-client error|401-unauth|403-forbidden|404-not found|500-server error|501-not implemented
import requests

url0='https://www.ibm.com/'
r0=requests.get(url0)
print("Request status:",r0.status_code) #200 sigs success
print(r0.request.headers)
print("Request body:",r0.request.body)
header=r0.headers
print(header['date'])
print(header['content-type'])


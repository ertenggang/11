import base64
import urllib
import urllib2

# f = open('./images/test.jpg','rb')
# m1 = base64.b64encode(f.read())

# f = open('./images/snow2.jpg','rb')
# m2 = base64.b64encode(f.read())
m1 = 'hello'
m2 = 'world'

test_data = {'m1':m1, 'm2':m2}
test_data_urlencode = urllib.urlencode(test_data)
requrl = 'http://127.0.0.1/5000/image_match_api/'
headers = {  
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}  
req = urllib2.Request(url=requrl, data=test_data_urlencode, headers = headers)
print test_data_urlencode

req.add_header("Content-Type", "application/x-www-form-urlencoded")

res_data = urllib2.urlopen(req)
res = res_data.read()

print res
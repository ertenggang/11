import base64
import urllib
import urllib2

level = 'match'
# level = 'duplication'

f = open('./images/cat11.jpg','rb')
# m1 = base64.b64encode(f.read())

f = open('./images/cat12.jpg','rb')
# m2 = base64.b64encode(f.read())

# m1 = 'hello'
# m2 = 'world'

m1 = base64.b64encode('hello')
m2 = base64.b64encode('world')

test_data = {'m1':m1, 'm2':m2}
test_data_urlencode = urllib.urlencode(test_data)
requrl = 'http://127.0.0.1:5000/image_match_api/'+level
req = urllib2.Request(url=requrl, data=test_data_urlencode)

# req.add_header("Content-Type", "application/x-www-form-urlencoded")

res_data = urllib2.urlopen(req)
res = res_data.read()

print res
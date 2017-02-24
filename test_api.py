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
requrl = 'http://127.0.0.1/5001/'
req = urllib2.Request(url = requrl, data=test_data_urlencode)
print test_data_urlencode

res_data = urllib2.urlopen(req)
res = res_data.read()

print res
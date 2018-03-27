import httplib, urllib

params = urllib.urlencode({'field2': image.jpg,'key':'18O57G6079EBGBKU'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"image/jpg"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()

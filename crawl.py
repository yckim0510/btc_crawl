import urllib
import time
import requests
import json


#resp = requests.get('https://api.coinone.co.kr/ticker/?currency=BTC').text
#btc_krw = float(json.loads(resp)["last"])

#print('Coinone: %d' % (btc_krw))

url = "https://api.coinone.co.kr/trades/?currency=btc&period=hour"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

print(response.getheaders())
result = data["result"]
print(result)
print(response.status)
print(data['result'])
print(data['errorCode'])
print(data['completeOrders'])
print(len(data['completeOrders']))


url2 = "https://api.coinone.co.kr/ticker_utc/?currency=btc"
response = urllib.request.urlopen(url2)
data = json.loads(response.read())

print(data)
print(data['result'])
print(data['errorCode'])
print(data['timestamp'])
print(data['currency'])
print(data['last'])


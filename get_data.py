#サーバー
import requests
import json
import time
from datetime import datetime

apikey = "c6cebfad880aa0a2fa834875a30620f15c1d90ec9b74271ca209dfa4f2b7faf3"
api = "https://api-tokyochallenge.odpt.org/api/v4/odpt:Train?&acl:consumerKey={key}"
url_train = api.format(key=apikey)
api = "https://api-tokyochallenge.odpt.org/api/v4/odpt:Bus?&acl:consumerKey={key}"
url_bus = api.format(key=apikey)


d = {}
for i in range(3):
	r1 = requests.get(url_train)
	r2 = requests.get(url_bus)
	try:
		data1 = json.loads(r1.text)
		data2 = json.loads(r2.text)
	except json.decoder.JSONDecodeError:
		data1 = r1.text
		data2 = r2.text

	for dic in data1:
		try:
			d[dic["owl:sameAs"]] = {'operator':dic['odpt:operator'],'from':dic['odpt:fromStation'],'to':dic['odpt:toStation']}
		except KeyError:
			pass

	for dic in data2:
		try:
			d[dic["owl:sameAs"]] = {'operator':dic['odpt:operator'],'from':dic['odpt:fromBusstopPole'],'to':dic['odpt:toBusstopPole']}
		except KeyError:
			pass

	time.sleep(10)

now = datetime.now()
filename = "{0:%H%M}.json".format(now)

with open(filename,'w') as Obj:
	json.dump([d],Obj)

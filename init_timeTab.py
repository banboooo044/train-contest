#サーバー
import requests
import json
import time
from datetime import datetime

apikey = "c6cebfad880aa0a2fa834875a30620f15c1d90ec9b74271ca209dfa4f2b7faf3"
api = "https://api-tokyochallenge.odpt.org/api/v4/odpt:BusroutePattern?&acl:consumerKey={key}"
url = api.format(key=apikey)

r = requests.get(url)

try:
	data = json.loads(r.text)
		
except json.decoder.JSONDecodeError:
	data = r.text

with open("./route.json",'r') as obj:
	route = json.load(obj)

Table = {}
for lis in route:
	for j in lis:
		if not j in Table:
			Table[j] = {}

	for i in range(len(lis)-1):
		Table[lis[i]][lis[i+1]] = 2.0
		Table[lis[i+1]][lis[i]] = 2.0


route_total = []
for dic in data:
	r = []
	for pole in dic['odpt:busstopPoleOrder']:
		r.append(pole['odpt:busstopPole'])

	route_total.append(r)


gragh = {}
for r in route_total:
	for i in range(len(r)-1):
		if r[i] in gragh:
			gragh[r[i]][r[i+1]] = 2.0
		else:
			gragh[r[i]] = {r[i+1]:2.0}

		if r[i+1] in gragh:
			gragh[r[i+1]][r[i]] = 2.0
		else:
			gragh[r[i+1]] = {r[i]:2.0}

Table.update(gragh)
print(Table['odpt.Station:JR-East.ChuoRapid.Tachikawa'])
with open("./timeTab.json",'w') as obj:
	json.dump(Table,obj)







import json
with open("./route.json",'r') as obj:
	route = json.load(obj)

for r in route:
	print(r)
	print()
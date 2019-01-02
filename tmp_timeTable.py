import json
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

with open("./timeTab.json",'w') as obj:
	json.dump(Table,obj)


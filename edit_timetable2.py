import json


with open("./timeTable_short.json",'r') as obj:
	data = json.load(obj)
with open("./route.json",'r') as obj:
	route = json.load(obj)

shdic = {}
for key,lis in data.items():
	shdic[key] = {}
	for dic in lis:
		if (dic['odpt:trainType'],dic['odpt:destinationStation'])in shdic[key]:
			shdic[key][(dic['odpt:trainType'],dic['odpt:destinationStation'])].append(dic['odpt:departureTime'])
		else:
			shdic[key][(dic['odpt:trainType'],dic['odpt:destinationStation'])] = [dic['odpt:departureTime']]


timeTable = {}
def timedelta(p,q):
	ret = []
	lp = len(p) 
	lq = len(q)
	if lp == lq:
		for x,y in zip(p,q):
			minu = int(y[3:]) - int(x[3:])
			hour = int(y[0:2]) - int(x[0:2])
			if minu < 0:
				minu += 60
				hour -= 1
			ret.append(minu+hour*60)		

	elif lp > lq:
		P = 0
		Q = 0
		while P < lp and Q < lq:
			if p[P] > q[Q]:
				P += 1
				continue

			else:
				minu = int(p[P][3:]) - int(p[P][3:])
				hour = int(q[Q][0:2]) - int(q[Q][0:2])
				if minu < 0:
					minu += 60
					hour -= 1
				ret.append(minu+hour*60)
				
				P += 1
				Q += 1

	else:
		P = 0
		Q = 0
		while P < lp and Q < lq:
			if p[P] > q[Q]:
				Q += 1
				continue

			else:
				minu = int(p[P][3:]) - int(p[P][3:])
				hour = int(q[Q][0:2]) - int(q[Q][0:2])
				if minu < 0:
					minu += 60
					hour -= 1
				ret.append(minu+hour*60)
				
				P += 1
				Q += 1

	if len(ret) == 0 or sum(ret) / len(ret) <= 0 :
		return 2.0 #平均

	return sum(ret) / len(ret)


for r in route:
	for i in range(len(r)-1):
		if (not r[i] in shdic or not r[i+1] in shdic):
			break

		timeTable[r[i]] = {}
		for key1 in shdic[r[i]].keys():
			for key2 in shdic[r[i+1]].keys():
				if key1 == key2:
					timeTable[r[i]][r[i+1]] = timedelta(shdic[r[i]][key1],shdic[r[i+1]][key2])

with open('timeTable_between.json','w') as obj:
	json.dump(timeTable,obj)

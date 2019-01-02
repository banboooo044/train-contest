import json


with open("./timeTable.json",'r') as obj:
	data = json.load(obj)


short_data = {}
for dic in data:
	short_data[dic['odpt:station']] = dic['odpt:stationTimetableObject']


with open("./timeTable_short.json",'w') as obj:
	json.dump(short_data,obj)
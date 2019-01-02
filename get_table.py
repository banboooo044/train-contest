import json
prev = {}	#電車id : [時刻,from,to]
table = []

for i in range(1440):
	minute = i % 60
	hour = i // 60
	minute = '{0:02d}'.format(minute)
	hour = '{0:02d}'.format(hour)
	filename = "./data/{}.json".format(hour+minute)

	with open(filename,'r') as obj:
		data_t = json.load(obj)

	data = data_t[0]

	for key,lis in prev.items():
		if key in data:
			if 'delay' in dic and dic['delay'] != 0:
				continue

			if len(lis) == 2 and (not data[key]['to'] is None) and data[key]['from'] == lis[1]:
				prev[key][2] = data[key]['to']

			elif lis[2] == data[key]['from']:
				m = int(minute)
				if lis[0] > m:
					lis[0] = (lis[0] - m)  
				else:
					print(lis[0],m)
					exit(0)
					lis[0] = (60 - lis[0] + m)


				table.append(lis)
				prev[key] = [m,data[key]['from']]
				if not data[key]['to'] is None:
					prev[key].append(data[key]['to'])

	for key , dic in data.items():
		if not key in prev:
			if 'delay' in dic and dic['delay'] == 0:
				if dic['to'] is None:
					prev[key] = [int(minute),dic['from']]

				elif dic['from'] is None:
					prev[key] = [int(minute),dic['to']]

print(table)



import json
filename ="./kk.txt"
with open(filename,'r') as obj:
	data = json.load(obj)

print(data)
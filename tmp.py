import requests
import json
import time
from datetime import datetime,timedelta


filename1 = "./data/0815.json"
filename2 =  "./data/0814.json"
filename3 = "./data/0816.json"


with open(filename1,'r') as Obj:
        data1 = json.load(Obj)

with open(filename2,'r') as Obj:
        data2 = json.load(Obj)

with open(filename3,'r') as Obj:
        data3 = json.load(Obj)

print(len(data1[0]))
print(len(data2[0]))
print(len(data3[0]))
print("1-2")
print(len(set(data1[0].keys()) & set(data2[0].keys())))
print("2-3")
print(len(set(data2[0].keys()) & set(data3[0].keys())))
print("1-3")
print(len(set(data1[0].keys()) & set(data3[0].keys())))


import json
import time
from datetime import datetime


with open("./name.json",'r') as obj:
	name = json.load(obj)

with open("./name.txt",'w') as obj:
	obj.write("NAME = ")
	obj.write(str(name))
	
	



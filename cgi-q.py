#! /usr/bin/python3                                                             
import cgi
import json
from datetime import datetime,timedelta
print("Content-Type: text/html\n\n")
form = cgi.FieldStorage()
ID = form["id"].value
print("<html>")
print("<body>")
print("<H1>hello</H1>")
print("ID => " + ID + "<br>")
with open("./timeTab.json",'r') as obj:
	Table = json.load(obj)

info = []
time_info = []
time = datetime.now()
cnt = 0
time = time + timedelta(minutes=(-1)) + timedelta(hours=9)
filename = "/var/www/html/takeshi/data/" + "{0:%H%M}.json".format(time)

while True:
    cnt += 1
    with open(filename,'r') as obj:
        data_tmp = json.load(obj)

    data = data_tmp[0]

    if cnt > 30:
        print("ERROR")
        exit(0)

    if ID in data:
        delta = 0
        if data[ID]['to'] == 0:
            prev = (-1)
            info.append((data[ID]['from'],"{0:%H%M}".format(time)))
        else:
            info.append((data[ID]['to'],"{0:%H%M}".format(time)))
            prev = data[ID]['from']
        break

    else:
        time = time + timedelta(minutes=-1)
        filename = "/var/www/html/takeshi/data/" + "{0:%H%M}.json".format(time)

while True:
    cnt += 1
    delta += 1
    time = time + timedelta(minutes=-1)
    filename = "/var/www/html/takeshi/data/" + "{0:%H%M}.json".format(time)
    try:
        with open(filename,'r') as obj:
            data_tmp = json.load(obj)

    except FileNotFoundError:
        print("FILE NOT FOUND")
        break

    data = data_tmp[0]

    if cnt > 120:
        break

    if (not ID in data):
        continue

    if prev == (-1) and data[ID]['to'] != 0:
        prev = data[ID]['from']

    elif data[ID]['to'] == prev or (data[ID]['to'] == 0 and data[ID]['from'] == prev):
        time_info.append(Table[prev][info[-1][0]] - delta)
        info.append((prev,"{0:%H%M}".format(time)))
        delta = 0

        if data[ID]['to'] != 0:
            prev = data[ID]['from']
        else:
            prev = (-1)


print(info[0][1] + " : " + info[0][0] + " <----- now")
for delta_t , (station,time) in zip(time_info,info):
	print("<br>")
	print("----" + str(delta_t) + "----")
	print("<br>")
	print(time + " : " + station)

print("</body>")
print("</html>")
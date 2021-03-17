import re
import datetime
import time 

file = open("datetime.txt", "r")
f = open("unixtime.txt", "w")

dateArr = []
for line in file:
    # element = datetime.datetime.strptime(line.replace("\n", ""),"%d/%m/%Y %H:%M:%S") 
    element = datetime.datetime.strptime(line.replace("\n", ""),"%d/%m/%Y %H:%M") 
    tuple = element.timetuple() 
    timestamp = time.mktime(tuple) 
    # print(int(timestamp))
    f.write(str(int(timestamp)) + "\n")

f.close()
file.close()

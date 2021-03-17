import re
import datetime
import time

file = open("datetime.txt", "r")
f = open("unixtime.txt", "w")

dateArr = []
for line in file:
    start_date = line.split(",")[0].replace("\n", "")
    end_date = line.split(",")[1].replace("\n", "")
    start_date = start_date.replace("\t", "")
    end_date = end_date.replace("\t", "")
    start_date = start_date+":00"
    end_date = end_date+":00"
    element1 = datetime.datetime.strptime(start_date, "%d/%m/%Y %H:%M:%S")
    element2 = datetime.datetime.strptime(end_date, "%d/%m/%Y %H:%M:%S")
    # element1 = datetime.datetime.strptime(start_date, "%d/%m/%Y %H:%M")
    # element2 = datetime.datetime.strptime(end_date, "%d/%m/%Y %H:%M")
    tuple1 = element1.timetuple()
    tuple2 = element2.timetuple()
    timestamp1 = time.mktime(tuple1)
    timestamp2 = time.mktime(tuple2)
    f.write(str(int(timestamp1)) + "\t" + str(int(timestamp2)) + "\n")


f.close()
file.close()

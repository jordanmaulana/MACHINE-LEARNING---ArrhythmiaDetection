import csv
import time

now = 150
start = False

foo = open('datatestR.csv','a')

counter = 0
start = False
line = ""

#you have to change the directory below
with open('C:\\Users\\asus\\Desktop\\data 1 minute\\135.csv','rt') as f:
    reader = csv.reader(f)

    for row in reader:
        value = int(row[0])

        if start == True:
            counter += 1
        if value>150 :
            if value > now:
                now = value
            else:
                if start == True:
                    line = "%f,%s\n" % (counter,"TC")
                    foo.write(line)
                    counter = 0
                    now = 150
                start = True
        else:
            now = 150
foo.close()
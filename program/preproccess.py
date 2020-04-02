import csv
import time

now = 150
start = False


foo = open('datasetR.csv','a')

counter = 0
start = False
line = ""

#you have to change the directory below
#File names that ends with 0 is dataset. You have to change file name (Line 8) to datasetR.csv
#File names that ends with 5 is datatest. You have to change file name (Line 8) to datatestR.csv
with open('../dataset/130.csv','rt') as f:
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

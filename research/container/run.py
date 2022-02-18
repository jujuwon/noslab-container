import time
import csv
import sys
import ftplib
import os

start = time.time()

index = sys.argv[1]
fileName = 'data.csv'

with open(fileName, 'r', encoding='utf-8') as f_read:
    reader = csv.reader(f_read)
    with open('temp.txt', 'w+') as f_write:
        for line in reader:
            f_write.write(str(line))    

end = time.time()
duration = end - start

logFileName = 'log' + index + '.txt'

with open(logFileName, "w+", encoding='utf-8') as f:
    data = '[' + index + '] : ' + str(duration)
    f.write(data)

time.sleep(60)
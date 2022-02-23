import time
import csv
import sys
from MeasureCpu import MeasureCpuUtil

index = sys.argv[1]

def workload():
    # Copy workload 시작
    start = time.time()

    fileName = 'data.csv'
    with open(fileName, 'r', encoding='utf-8') as f_read:
        reader = csv.reader(f_read)
        with open('temp.txt', 'w+') as f_write:
            for line in reader:
                f_write.write(str(line))    

    logFileName = 'log' + index + '.txt'
    
    # Copy workload 끝
    end = time.time()
    duration = end - start

    with open(logFileName, "w+", encoding='utf-8') as f:
        data = '[' + index + '] : ' + str(duration)
        f.write(data)

if __name__ == "__main__":
    # cpu_thread = MeasureCpuUtil(index)
    # cpu_thread.start()
    workload()
    # cpu_thread.DONE = True
    # time.sleep(30)

    
import sys
import os
import psutil
import datetime
import time

pid = int(sys.argv[1])
sys.stdout = open("hostResult.txt", 'a')

def _check_usage_of_cpu_and_memory():
    
    py  = psutil.Process(pid)
    
    cpu_usage   = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
    cpu_usage   = cpu_usage.replace("\n","")
    
    memory_usage  = round(py.memory_info()[0] /2.**30, 2)

    now = datetime.datetime.now()
    print(now)
    print("cpu usage\t\t:", cpu_usage, "%")
    print("memory usage\t\t:", memory_usage, "%")

while True:
    _check_usage_of_cpu_and_memory()
    time.sleep(0.1)
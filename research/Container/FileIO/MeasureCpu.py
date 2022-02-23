import sys
import os
import psutil
import datetime
import time
import threading

class MeasureCpuUtil(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.pid = 1
        self.DONE = False
        self.file = 'cpu_log' + index + '.txt'
        

    def run(self):
        f = open(self.file, 'a')
        sys.stdout = f
        while not self.DONE:
            py  = psutil.Process(self.pid)
    
            cpu_usage   = os.popen("ps aux | grep " + str(self.pid) + " | grep -v grep | awk '{print $3}'").read()
            cpu_usage   = os.popen("ps aux | grep python | grep -v grep | awk '{print $3}'").read()
            cpu_usage   = cpu_usage.replace("\n","")
            
            # memory_usage  = round(py.memory_info()[0] /2.**30, 2)

            # now = datetime.datetime.now()
            # print(now)
            print(cpu_usage, "%")
            # print("memory usage\t\t:", memory_usage, "%")
            time.sleep(0.1)
        f.close()
        

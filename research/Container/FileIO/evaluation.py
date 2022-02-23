from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from MeasureCpu import MeasureCpuUtil

colors = ['#93DAFF', '#87CEFA', '#00BFFF', '#00A5FF', '#1EA4FF',
        '#1E90FF', '#96A5FF', '#86A5FF', '#6495ED', '#0078FF',
        '#0064FF', '#0000FF', '#4169E1', '#0064CD', '#5A5AFF', '#7B68EE']
time_log_list = []
cpu_log_list = []

def plot_time():    

    for i in range(5):
        # 디렉토리 하나 오픈
        dir_index = 2**i
        temp = []
        path =  './logs/cont_' + str(dir_index)
        for j in range(1, dir_index+1):
            # 파일 하나씩 오픈
            fileName = path + '/log' + str(j) + '.txt'
            with open(fileName, 'r') as f:
                temp.append(f.read()[6:])
        
        res = 0
        for k in temp:
            res += float(k)
        time_log_list.append(res / dir_index)
    
    print(time_log_list)
    plt.plot([1, 2, 4, 8, 16], time_log_list, color='blue', marker='^', label='container runtime')
    plt.legend()
    plt.xticks([1, 2, 4, 8, 16])
    plt.yticks(np.arange(8, 14, 0.5))
    plt.xlabel('number of container')
    plt.ylabel('runtime(sec)')
    plt.show()
    # plt.savefig('result.png')

def plot_cpu_usage():

    for i in range(5):
        # 0, 1, 2, 3, 4
        # 디렉토리 하나 오픈
        dir_index = 2**i
        cpu_log_list.clear()

        path =  './logs/cont_' + str(dir_index)
        for j in range(1, dir_index+1):
            # 파일 하나씩 오픈
            cpu_log_list.append(list())
            fileName = path + '/cpu_log' + str(j) + '.txt'
            temp = []
            with open(fileName, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.split()[0]
                    cpu_log_list[j-1].append(float(line))

        for k in range(2**i):
            plt.plot(cpu_log_list[k], color=colors[k], label='Cont.' + str(k+1))
            plt.legend()        
            plt.yticks(np.arange(0, 200, 10))
        
        
        plt.xlabel('logical time')
        plt.ylabel('cpu usage(%)')
        plt.show()
        # plt.savefig('result.png')
if __name__ == "__main__":
    plot_time()
    plot_cpu_usage()
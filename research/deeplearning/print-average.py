from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# numOfContainer = int(sys.argv[1])
refactor_list = []
host_cpu_usage_list = []
colors = ['#c1edfe', '#47c9ff', '#0090cc', '#004561']
result = [[0] * 521, [0] * 521, [0] * 521, [0] * 420]
cont1 = [0] * 521

def render():
    path = os.getcwd() + "/matplotlib/host.txt"
    f = open(path, 'r')
    lines = f.readlines()
    for line in lines:
        host_cpu_usage_list.append(float(line))
    f.close()
    plt.plot(host_cpu_usage_list, 'r', label='host')
    plt.xlabel('logical time')
    plt.ylabel('cpu usage')
    plt.xlim([0, 550])
    plt.ylim([0, 100])
    plt.legend()

    # for i in range(2):
    #     path = os.getcwd() + "/data/result2-1/cont" + str(i+1) + ".txt"
    #     f = open(path, 'r')
    #     lines = f.readlines()        
    #     cont1.clear()
    #     for line in lines:
    #         cont1.append(float(line))
    #     f.close()
    #     plt.plot(cont1, color=colors[i],label = "container" + str(i+1))
    #     plt.xlabel('logical time')
    #     plt.ylabel('cpu usage')
    #     plt.xlim([0, 550])
    #     plt.ylim([0, 100])
    #     plt.legend()
    # plt.show()

    for i in range(4): # 1, 2, 4, 8
        for j in range(5):
            for k in range(2**i):
                path = os.getcwd() + "/data/result" + str(2**i) + "-" + str(j+1) + "/"
                fileName = "cont" + str(k+1) + ".txt"
                file = path + fileName
                f = open(file, 'r')
                lines = f.readlines()
                print(file + " : " + str(len(lines)))
                index = 0
                for line in lines:
                    result[i][index] += float(line.strip())
                    index += 1
                f.close()
    
    for i in range(521):
        result[0][i] /= 5
    for i in range(521):
        result[1][i] /= 10
    for i in range(521):
        result[2][i] /= 20
    for i in range(420):
        result[3][i] /= 40

    for i in range(4):
        plt.plot(result[i], color=colors[i], label="avg of cont" + str(2**i))
    plt.xlabel('logical time')
    plt.ylabel('cpu usage')
    plt.xlim([0, 550])
    plt.ylim([0, 100])
    plt.legend()
    plt.show()

    # cont_cpu_usage_list = list()
    # for i in range(numOfContainer):
    #     cont_cpu_usage_list.append(list())
    # for i in range(numOfContainer):
    #     path = os.getcwd() + "/matplotlib/cont" + str(i+1) + ".txt"
    #     f = open(path, 'r')
    #     lines = f.readlines()
    #     for line in lines:
    #         cont_cpu_usage_list[i].append(float(line))
    #     f.close()
    #     plt.plot(cont_cpu_usage_list[i], color=colors[i],label = "container" + str(i+1))
    #     plt.xlabel('logical time')
    #     plt.ylabel('cpu usage')
    #     plt.xlim([0, 550])
    #     plt.ylim([0, 100])
    #     plt.legend()
    # plt.savefig('result.png')
    

if __name__ == "__main__":
    render()
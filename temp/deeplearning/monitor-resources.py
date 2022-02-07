from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

numOfContainer = int(sys.argv[1])
refactor_list = []
host_cpu_usage_list = []
colors = ['#c1edfe', '#99e1ff', '#70d5ff', '#47c9ff', '#1ebdff',
        '#00adf4', '#0090cc', '#0073a3', '#005c82', '#004561']

def readfile(filename):
    path = os.getcwd() + filename
    f = open(path, 'r')
    refactor_list.clear()

    lines = f.readlines()
    for line in lines:
        if not "cpu" == line[0:3]: continue
        # TODO cpu 뒤 내용이 없으면 continue
        if len(line) < 14: continue
        temp = line.strip()[13:]
        usage = temp.split(".")[0][-2:] + "." + temp.split(".")[1][0:1]
        refactor_list.append(usage)
    f.close()
    
def make_cont_file():
    for i in range(numOfContainer):
        readfile('/data/result' + str(i+1) + '.txt')
        path = os.getcwd() + "/matplotlib/cont" + str(i+1) + ".txt"
        f = open(path, 'w')
        f.write('\n'.join(refactor_list))
        f.close()
    

def make_host_file():
    readfile('/hostResult.txt')
    path = os.getcwd() + "/matplotlib/host.txt"
    f = open(path, 'w')
    f.write('\n'.join(refactor_list))
    f.close()

def make_file():
    # make_host_file()
    make_cont_file()

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
    #plt.show()

    cont_cpu_usage_list = list()
    for i in range(numOfContainer):
        cont_cpu_usage_list.append(list())
    for i in range(numOfContainer):
        path = os.getcwd() + "/matplotlib/cont" + str(i+1) + ".txt"
        f = open(path, 'r')
        lines = f.readlines()
        for line in lines:
            cont_cpu_usage_list[i].append(float(line))
        f.close()
        plt.plot(cont_cpu_usage_list[i], color=colors[i],label = "container" + str(i+1))
        plt.xlabel('logical time')
        plt.ylabel('cpu usage')
        plt.xlim([0, 550])
        plt.ylim([0, 100])
        plt.legend()
    plt.savefig('result.png')
    

if __name__ == "__main__":
    make_file()
    render()
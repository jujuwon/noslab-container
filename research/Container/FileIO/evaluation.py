from turtle import color
import matplotlib.pyplot as plt
import numpy as np

log_list = []

def render():    
    path = './logs/cont_1'
    fileName = path + '/log1.txt'

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
        log_list.append(res / dir_index)
    
    print(log_list)
    plt.plot([1, 2, 4, 8, 16], log_list, color='blue', marker='^', label='container runtime')
    plt.legend()
    plt.xticks([1, 2, 4, 8, 16])
    plt.yticks(np.arange(8, 14, 0.5))
    plt.xlabel('number of container')
    plt.ylabel('runtime(sec)')
    # plt.show()
    plt.savefig('result.png')
    
if __name__ == "__main__":
    render()
import matplotlib.pyplot as plt

colors = ['#93DAFF', '#1EA4FF', '#6495ED', '#4169E1', '#7B68EE']

def parse_mpstat():
    logs = []
    
    path = '../logs/stat_logs/'
    for i in range(5):
        temp = []
        
        file = 'mpstat_log' + str(2**i) + '.txt'
        fileName = path + file

        with open(fileName, 'r') as f:
            first = True
            lines = f.readlines()
            for line in lines:
                if first:
                    first = False
                    continue
                else:
                    col = line.rstrip().split()
                    
                    if col:
                        cpu_util = col[4]
                        # 헤더 처리
                        if cpu_util[0] == '%':
                            pass
                        else:
                            print(f'file : {file} content : {float(cpu_util)}')
                            temp.append(float(cpu_util))
                    # 공백 처리
                    else:
                        pass
                    

        logs.append(temp)
    
    for j in range(5):
        plt.plot(logs[j], color=colors[j], label='Cont.' + str(2**j))
        plt.legend()
    
    plt.xlabel('duration(sec)')
    plt.ylabel('cpu utilization(%)')
    plt.show()

def parse_iostat():
    read_logs = []
    write_logs = []
    
    path = '../logs/stat_logs/'
    for i in range(5):
        read_temp = []
        write_temp = []
        
        file = 'iostat_log' + str(2**i) + '.txt'
        fileName = path + file

        with open(fileName, 'r') as f:
            first = True
            lines = f.readlines()
            for line in lines:
                col = line.rstrip().split()

                # 헤더 제거
                if first:
                    first = False
                    continue
                else:
                    if col:
                        if col[0] == "nvme0n1":
                            print(col)
                            
                            read_temp.append(float(col[2]))
                            write_temp.append(float(col[3]))
                    # 공백 처리
                    else:
                        pass
                    

        read_logs.append(read_temp)
        write_logs.append(write_temp)
    
    for j in range(5):
        plt.plot(read_logs[j], color=colors[j], label='Cont.' + str(2**j))
        plt.legend()
    
    plt.xlabel('duration(sec)')
    plt.ylabel('read KB/s')
    plt.show()

    for k in range(5):
        plt.plot(write_logs[k], color=colors[k], label='Cont.' + str(2**k))
        plt.legend()
    
    plt.xlabel('duration(sec)')
    plt.ylabel('write KB/s')
    plt.show()

if __name__ == "__main__":
    parse_mpstat()
    parse_iostat()
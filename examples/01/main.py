# Get the current CPU and Memory Usage in the system, Plus top 3 CPU & Memory Process.

import psutil

def system_usage():
    pcpu=psutil.cpu_percent()
    pemm=psutil.virtual_memory().percent
    print(f"\tPercentage Cpu - {pcpu}")
    print(f"\tPercentage Memory - {pemm}")

def top_cpu_usage():
    pout = []
    pid_list=psutil.pids()
    for pid in pid_list:
        pinfo = psutil.Process(pid)
        pname = pinfo.name()
        pcpu  = pinfo.cpu_percent()
        pout.append((pid, pcpu, pname))
        pout.sort(key=lambda x: x[1], reverse=True)

    print(f"{'PID':<10}{'CPU %':<0}{'Process Name'}")
    for pid, cpu, pname in pout:
        print(f"{pid:<10}{cpu:<10}{pname}")

if __name__ == '__main__':
    print('System Usage')
    print('*' * 50)
    system_usage()

    print('\nTop 3 Cpu Process')
    print('*' * 50)
    top_cpu_usage()

    print('\nTop 3 Mem Process')
    print('*' * 50)



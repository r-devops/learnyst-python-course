# Get the current CPU and Memory Usage in the system, Plus top 3 CPU & Memory Process.

import psutil

def system_usage():
    print(psutil.cpu_percent())
    print(psutil.virtual_memory())

if __name__ == '__main__':
    print('System Usage')
    print('*' * 50)
    system_usage()

    print('\nTop 3 Cpu Process')
    print('*' * 50)

    print('\nTop 3 Mem Process')
    print('*' * 50)



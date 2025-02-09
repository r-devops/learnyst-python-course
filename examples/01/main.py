# Get the current CPU and Memory Usage in the system, Plus top 3 CPU & Memory Process.
import psutil

def all_cpu():
    all_pids = psutil.pids()
    for pid in all_pids:
        pname = psutil.Process(pid).name()
        pcpu = psutil.Process(pid).cpu_percent()
        print(f"PID: {pid} Percentage: {pcpu} Name : {pname}")

def all_memory():
    processes = []
    all_pids = psutil.pids()
    for pid in all_pids:
        pname = psutil.Process(pid).name()
        pmem = psutil.Process(pid).memory_percent()
        processes.append((pid, pname, pmem))
        # print(f"PID: {pid} Percentage: {pcpu} Name : {pname}")
        # print(sorted(pcpu, key=lambda x: x[0], reverse=True))
        processes.sort(key=lambda x: x[2], reverse=True)

if __name__ == '__main__':
    cpu_percentage = psutil.cpu_percent()
    print(f"Cpu Usage Percentage - {cpu_percentage}")

    mem_percentage = psutil.virtual_memory().percent
    print(f"Memory Usage Percentage - {mem_percentage}")

    print("\nAll Process with CPU Usage")
    print("--------------------------")
    all_cpu()
    print("--------------------------")

    print("\nAll Process with Memory Usage")
    print("--------------------------")
    print(all_memory().sort(key=lambda x: x[1]))
    print("--------------------------")


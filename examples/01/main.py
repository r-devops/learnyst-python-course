# Get the current CPU and Memory Usage in the system, Plus top 3 CPU & Memory Process.
import psutil

def top_cpu():
    all_pids = psutil.pids()
    for pid in all_pids:
        pname = psutil.Process(pid).name()
        pcpu = psutil.Process(pid).cpu_percent()
        print(f"PID: {pid} Percentage: {pcpu} Name : {pname}")

if __name__ == '__main__':
    cpu_percentage = psutil.cpu_percent()
    print(f"Cpu Usage Percentage - {cpu_percentage}")

    mem_percentage = psutil.virtual_memory().percent
    print(f"Memory Usage Percentage - {mem_percentage}")

    top_cpu()

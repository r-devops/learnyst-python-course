# Get the current CPU and Memory Usage in the system, Plus top 3 CPU & Memory Process.
import psutil

def top_cpu:


if __name__ == '__main__':
    cpu_percentage = psutil.cpu_percent()
    print(f"Cpu Usage Percentage - {cpu_percentage}")

    mem_percentage = psutil.virtual_memory().percent
    print(f"Memory Usage Percentage - {mem_percentage}")


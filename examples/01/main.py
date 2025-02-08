# Get the current CPU and Memory Usage in the system, Plus top 3 CPU & Memory Process.
import psutil

if __name__ == '__main__':
    cpu_percentage = psutil.cpu_percent()
    print(f"Cpu Usage Percentage - {cpu_percentage}")

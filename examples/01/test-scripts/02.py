import psutil

print(psutil.pids())
x = psutil.Process(1424)
print(x.cpu_percent)

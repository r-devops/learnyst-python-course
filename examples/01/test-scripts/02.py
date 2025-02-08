import psutil

all = psutil.pids()
p = psutil.Process(3897)
print(p.cpu_percent())


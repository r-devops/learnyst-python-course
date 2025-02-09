import psutil

print(psutil.pids())
x = psutil.Process(1424)
print(dir(x))

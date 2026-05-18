import os
import psutil

my_pid = os.getpid()
me = psutil.Process(my_pid)

print(f"This script is a process!")
print(f"  Process ID (PID): {my_pid}")
print(f"  Program name:     {me.name()}")
print(f"  Status:           {me.status()}")
print(f"  Started at:       {me.create_time()}")
print(f"  Memory used:      {me.memory_info().rss / 1024 / 1024:.1f} MB")

import os

print(f"This script is a process!")
print(f"  My PID:        {os.getpid()}")
print(f"  Parent PID:    {os.getppid()}")
print(f"  CPU cores:     {os.cpu_count()}")

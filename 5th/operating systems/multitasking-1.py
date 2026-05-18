import subprocess
import platform

if platform.system() == "Windows":
    result = subprocess.run(["tasklist"], capture_output=True, text=True)
else:
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True)

lines = result.stdout.strip().split("\n")
print(f"Processes found: {len(lines)}\n")
for line in lines[:20]:
    print(line)


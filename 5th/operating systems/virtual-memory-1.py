import subprocess
import platform

system = platform.system()

if system == "Linux":
    # Read directly from the kernel's virtual filesystem
    with open("/proc/meminfo") as f:
        for line in f.readlines()[:5]:
            print(line.strip())

elif system == "Windows":
    result = subprocess.run(
        ["wmic", "OS", "get", "TotalVisibleMemorySize,FreePhysicalMemory"],
        capture_output=True, text=True
    )
    print(result.stdout)

elif system == "Darwin":  # macOS
    result = subprocess.run(["vm_stat"], capture_output=True, text=True)
    print(result.stdout[:300])

import psutil

processes = list(psutil.process_iter(['pid', 'name', 'status']))

print(f"Your computer is currently running {len(processes)} processes.\n")
print(f"{'PID':<8} {'Name':<30} {'Status'}")
print("-" * 50)

for p in processes[:20]:   # show first 20 to keep output manageable
    print(f"{p.info['pid']:<8} {p.info['name']:<30} {p.info['status']}")

print(f"\n...and {len(processes) - 20} more.")

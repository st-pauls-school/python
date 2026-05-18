import psutil

ram = psutil.virtual_memory()
swap = psutil.swap_memory()

print("=== Physical RAM ===")
print(f"  Total:     {ram.total    / 1e9:.1f} GB")
print(f"  Used:      {ram.used     / 1e9:.1f} GB")
print(f"  Available: {ram.available/ 1e9:.1f} GB")
print(f"  Usage:     {ram.percent}%")

print("\n=== Swap / Virtual Memory (overflow space on disk) ===")
print(f"  Total: {swap.total / 1e9:.1f} GB")
print(f"  Used:  {swap.used  / 1e9:.1f} GB")

print("\n=== What individual processes think they have ===")
print(f"{'Name':<30} {'Virtual (MB)':>14} {'Physical (MB)':>14}")
print("-" * 60)
for p in list(psutil.process_iter(['name', 'memory_info']))[:10]:
    m = p.info['memory_info']
    print(f"{p.info['name']:<30} {m.vms/1e6:>14.1f} {m.rss/1e6:>14.1f}")

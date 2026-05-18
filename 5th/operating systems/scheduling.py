import psutil
import time

print("Watching CPU usage across all cores for 5 seconds...\n")

for i in range(5):
    usage = psutil.cpu_percent(interval=1, percpu=True)
    bar = "  ".join(f"Core {j}: {'#' * int(u // 5):<20} {u:5.1f}%"
                    for j, u in enumerate(usage))
    print(f"Second {i+1}: {bar}")

# Which processes are using the most CPU right now?
print("\nTop 5 CPU-hungry processes:")
top = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']),
            key=lambda p: p.info['cpu_percent'], reverse=True)[:5]
for p in top:
    print(f"  {p.info['name']:<30} {p.info['cpu_percent']}%")


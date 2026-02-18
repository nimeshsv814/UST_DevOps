# Monitor system resource usage and send alert if exceeds threshold.

import psutil
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
def monitor():
    while True:
        cpu=psutil.cpu_percent(interval=1)
        memory=psutil.virtual_memory().percent
        if cpu>CPU_THRESHOLD:
            print("CPU usage exceeded threshold limit")
        if memory>MEMORY_THRESHOLD:
            print("Memory usage exceeded threshold limit")
monitor()
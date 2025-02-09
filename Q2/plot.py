import subprocess
import re
import matplotlib.pyplot as plt
import time

bash_script = "./start.sh"
python_script = "client.py"
clients_range = range(10, 101, 10)

num_runs = 3

total_execution_times = []
average_execution_times = []

for clients in clients_range:
    print(f"Running {clients} clients {num_runs} times...")
    total_time_sum = 0
    avg_time_sum = 0
    valid_runs = 0

    for _ in range(num_runs):
        result = subprocess.run([bash_script, python_script, str(clients)], capture_output=True, text=True)
        
        match_total = re.search(r"Total Execution Time:\s*([\d.]+)", result.stdout)
        match_avg = re.search(r"Average Execution Time per script:\s*([\d.]+)", result.stdout)
        
        if match_total and match_avg:
            total_time = float(match_total.group(1))
            avg_time = float(match_avg.group(1))
            total_time_sum += total_time
            avg_time_sum += avg_time
            valid_runs += 1
        else:
            print(f"Failed to extract execution time for {clients} clients on this run")
    
    if valid_runs > 0:
        total_execution_times.append(total_time_sum / valid_runs)
        average_execution_times.append(avg_time_sum / valid_runs)
        print(f"Final Total Execution Time for {clients} clients: {total_execution_times[-1]:.2f} seconds")
        print(f"Final Average Execution Time for {clients} clients: {average_execution_times[-1]:.2f} seconds")
    else:
        total_execution_times.append(None)
        average_execution_times.append(None)

# Plot Total Execution Time
plt.figure(figsize=(10, 5))
plt.plot(clients_range, total_execution_times, marker='o', linestyle='-', color='b', label="Total Execution Time")
plt.xlabel("Number of Clients")
plt.ylabel("Execution Time (seconds)")
plt.title("Number of Clients vs Total Execution Time")
plt.legend()
plt.grid(True)
plt.savefig("total_execution_time_multi_thread.png")

# Plot Average Execution Time per Script
plt.figure(figsize=(10, 5))
plt.plot(clients_range, average_execution_times, marker='o', linestyle='-', color='r', label="Average Execution Time")
plt.xlabel("Number of Clients")
plt.ylabel("Execution Time (seconds)")
plt.title("Number of Clients vs Average Execution Time per Script")
plt.legend()
plt.grid(True)
plt.savefig("average_execution_time_multi_thread.png")

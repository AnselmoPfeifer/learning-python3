import psutil

cpu_count = psutil.cpu_count()
cpu_times_percent = psutil.cpu_times_percent(interval=1, percpu=False)
all_memory = psutil.virtual_memory()

total = all_memory[0]
available = all_memory[1]
percent = all_memory[2]
used = all_memory[3]
free = all_memory[4]
active = all_memory[5]
inactive = all_memory[6]
wired = all_memory[7]

cpu_user = cpu_times_percent[0]
cpu_nice = cpu_times_percent[1]
cpu_system = cpu_times_percent[2]
cpu_idle = cpu_times_percent[3]

print("CPU Times Percent {}".format(cpu_times_percent))
print("CPU Count {}".format(cpu_count))
print("CPU User {}".format(cpu_user))
print("CPU Nice {}".format(cpu_nice))
print("CPU System {}".format(cpu_system))
print("CPU Idle {}".format(cpu_idle))


print("All Memory\n {}".format(all_memory))
print("Total {}".format(total))
print("Available {}".format(available))
print("Percent {}".format(percent))
print("Used {}".format(used))
print("Free {}".format(free))
print("Active {}".format(active))
print("Inactive {}".format(inactive))
print("Wired {}".format(wired))



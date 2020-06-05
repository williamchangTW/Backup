import psutil as ps

def average(var):
	sum(var) / len(var)

cpu_each = ps.cpu_percent(interval = 1, percpu = True)
average(cpu_each)



import psutil as ps
import sys, os

def sys_check(percent):
	global warn_F
	cpu_each = ps.cpu_percent(interval = 1, percpu = True)
	cpu_average = sum(cpu_each) / len(cpu_each)
	if percent >= int(100 - ps.virtual_memory().percent) or percent >= int(100 - cpu_average):
		warn_F = 1
		print("warning sys")
	else:
		pass

def bat_check(flag, percent = None):
	global warn_F
	battery = ps.sensors_battery()
	plugged = battery.power_plugged
	if bool(flag) == True and plugged == False:
		warn_F = 1
		print("warning bat")
	elif bool(flag) == False and bool(percent) == True:
		b_percent = int(battery.percent)
		if b_percent < percent:
			warn_F = 1
			print("warning bat")
		else:
			pass
	else:
		pass
		


def wifi_check(flag):
	global warn_F
	print(type(flag))
	net_stat = os.popen("hostname -I").read().strip()
	if bool(flag) == True and bool(net_stat) == False:
		warn_F = 1
		print("warning sys")
	else:
		print("pass")
		pass


if __name__ == "__main__":
	warn_flag = 0
	def_F = input("Default Setting?(1:Yes, 0:No)")
	if bool(int(def_F)) == True:
		sys_check(70)
		bat_check(1)
		wifi_check(1)
	else:
		wifi_F = input("Connect to Wifi(1:Yes, 0:No)")	
		if bool(int(wifi_F)) == True:
			wifi_check(1)
		else:
			wifi_check(0)
		
		bat_F = input("Plug-in Charger(1:Yes, 0:No)")
		if bool(int(bat_F)) == True:
			bat_check(1)
		else:
			bat_per = input("Battery Percentage(from 100 to 40)")
			bat_check(0, bat_per)
			
		sys_F = input("System Loading(1:Yes, 0:No)")
		if bool(int(sys_F)) == True:
			sys_per = input("Upbound(from 80 ~ 10)")
			sys_check(int(sys_per))
		else:
			sys_check(70)

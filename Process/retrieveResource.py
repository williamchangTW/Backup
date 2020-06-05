# Description: 
# 	when too much suspended id exist need to slove 
# 	still have the place that not retrieve back to system
#	suspeded process by "SIGSTOP"
#	resume process by "SIGCONT"
# Targtet:
#  	retrive system resource back to system when too much suspeded process or triggered by button when it pushed by USER


# suspended process button
# File 1 suspended freqently

import psutil as ps
import time, os, sys, signal

# suspend process
def suspend_train():
	with open("rencentPID.txt", "r") as df:
		pid = int(df.read())
		p = ps.Process(pid)
		p.suspend()
		print("PID: " + str(pid) + "is suspended!")
		

# button pushed
def suspend_cancel():
	temp = []
	with open("historyPID.txt", "r") as df:
		for line in df.readlines():
			temp.append(line.strip())
	While len(temp) != 0:
		pid = temp.pop(0)
		try:
			os.kill(pid, signal.SIGTERM)
		except:
			print("PID: " + str(pid) + "is not EXIST!")

	print("All Suspended Process is Cleaning!")

# auto retrieve
def exit_retrieve():
	temp = []
	with open("historyPID.txt", "r") as df:
		for line in df.readlines():
			temp.append(line.strip())
	While len(temp) != 0:
		pid = temp.pop(0)
		try:
			os.kill(pid, signal.SIGTERM)
		except:
			print("PID: " + str(pid) + "is not EXIST!")

	print("All Suspended Process is Cleaning!")
	sys.exit(0)



if __name__ == "__main__":
	# store in 2 files to keep infomation
	# File 1: store file frequently
	# File 2: store history of suspended pid(use except and try)
	# suspended button pushed
	suspended_train()
	# cancel button pushed
	suspend_cancel()
	# exit the program
	exit_retrieve()

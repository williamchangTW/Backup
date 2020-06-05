# Use Monitor method to check process status
# keypoint: process name and transfer STATUS with different words
import os
import psutil as ps
import subprocess
import time

def get_pid(name):
	child = subprocess.Popen(['pgrep', '-f', name], stdout=subprocess.PIPE, shell=False)
	response = child.communicate()[0]
	return [int(pid) for pid in response.split()]


if __name__ == "__main__":
	# assume we have 4 process in the same time	
	# process name(all process name, if not work just show it is waiting)	
	# process status
	# process ID
	# process useage
	# additional condition: process percentage
	# check STATUS.txt exists
	# More information about training and checkpoint jobs content more detail
	# STATUS:
	# D -> Uninterruptible sleep
	# R -> Running or runable or in run queue
	# S -> Interrupible sleep or waiting for an event complete
	# T -> Stopped 
	# Z -> Defunct or call zombie process
	# Others STATUS ... 
	# <: high-priority
	# N: low-priority
	# L: has pages locked inti memory
	# s: is a session leader
	# l: mulrithread
	# +: in the top of queue
	while True:
		if os.path.exists("STATUS.txt") == True:
	    		os.remove("STATUS.txt")
		process_list = ["FileCorrect.py", "EnvironmentDaemon.py", "Training.py"]
		for times in range(len(process_list)):
			var1 = process_list[times]
			var2 = get_pid(var1)
			if len(var2) == 0:
				continue
			temp = os.popen("ps -aux | grep " + str(var2[0])).read()
			# status
			temp = temp.split(" ")
			var3_list = [value for index, value in enumerate(temp) 
				if value or (not value and temp[index - 1])] 
			var3 = var3_list[13]
			# time
			var4 = var3_list[15]
			with open("STATUS.txt", "a+") as wf:
				wf.writelines("Process Name: " + var1 + "\n")
				wf.writelines("Process ID: " + str(var2[0]) + "\n")
				wf.writelines("Process Status: " + str(var3) + "\n")
				wf.writelines("Process Created Time: " + str(var4) + "\n")
		time.sleep(10)


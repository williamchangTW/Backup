import threading
import os
import sys
# daemon
# enable & registeration, daemon since this step run in background
class daemon:
	def __init__(self):	
		print("registration...\n")
	def registered(self):
		name = os.getlogin()
		path = os.getcwd()
		python = sys.executable
		with open("envir_daemon.service", "w") as wf:
			wf.write("[Unit]\nDescription=envir_daemon\nAfter=network.target network-online.target\n[Service]\nType=simple\nUser=" + name + "\nExecStart="+ python + " " + path + "/envir_daemon.py\nWorkingDirectory=" + path + "/" + "\n[Install]\nWantedBy=multi-user.target\n")

	def enable(self):
		os.popen("mv envir_daemon.service /lib/systemd/system/")

thread = threading.Thread(target=daemon().registered())
thread.start()
# waiting
thread.join()
# move file to systemd
thread1 = threading.Thread(target=daemon().enable())
thread1.start()
# waiting
thread1.join()
# start run daemon
os.popen("systemctl enable envir_daemon.service")
os.popen("systemctl start envir_daemon.service")
print(os.popen("systemctl status envir_daemon.service").read())
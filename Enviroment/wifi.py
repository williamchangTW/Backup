import os
flag = 0
net = os.popen("hostname -I").read().strip()
# check wifi enviroment
if bool(net) == True:
	flag = 1
# TODO do something when wifi was connected

# TODO do something when wifi wasnt connected

import psutil as ps
import time

def suspend(flag, pid):
	p = ps.Process(pid)
	if flag == True:	
		p.suspend()
		print("Process " + str(pid) + "suspend!")
	else:	
		p.resume()
		print("Process " + str(pid) + "resume!")	


if __name__ == "__main__":
	with open("processpid.txt", "r") as df:
		reader = int(df.read())
		for i in range(1, 10):
			temp = i % 2
			suspend(temp, reader)
			time.sleep(5)
			print("No. " + str(i))

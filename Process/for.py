import time, os
def count():
	for i in range(0, 20):
		time.sleep(10)
	
if __name__ == "__main__":
	pid = os.getpid()
	with open("processpid.txt", "w") as df:
		df.write(str(pid))
		df.close()
	count()
	
	

	

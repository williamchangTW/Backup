import psutil as ps
import sys

def env_warning():
	print("Emergency!")

def mem_check(mem_per = 70):
	if int(mem_per) > int(100 - ps.virtual_memory().percent):
		env_warning()
	else:
		pass

if __name__ == "__main__":
	mem_per_f = input("Memory Environment Setting?(1: true, 0: false)")
	if bool(mem_per_f) == True:
		mem_per = input("Memory Usage Setting(Key in integer from 90 ~ 0):")
		mem_check(mem_per)

	else:
		sys.exit()


# tmp: store temporary files
# others

import csv
import psutil as ps
import os
import numpy as np

# get file size
# get system memory infomation
class CSVLoader:
	def __init__(self, fd):
		super(CSVLoader, self).__init__()
		self.fd = fd
		
	def _protect_available_memory(self):
		# caculate mem that need to be protect for more stable environment
		total_memory = int(ps.virtual_memory().total * 0.05)
		data_size = os.path.getsize(self.fd)
		if  data_size > total_memory:
			#print("large")
			#protect_range = int(ps.virtual_memory().available * 0.05)
			protect_range = int(self._get_sys_available_memory() * 0.05)
			return protect_range
		else:
			#print("small")
			#protect_range = int(ps.virtual_memory().available * 0.1)
			protect_range = int(self._get_sys_available_memory() * 0.1)
			return protect_range
	
	def _get_sys_available_memory(self):
		return ps.virtual_memory().available
	
	def _get_file_size(self):
		return os.path.getsize(self.fd)
	
	def _dynamic_allocate(self):
		# workflow: check ckpt -> open file -> store records -> looping until finished
		# check ckpt
		file_size = self._get_file_size()
		ava_mem = self._protect_available_memory()
		if os.path.exists("./tmp/file_pointer.txt") == True:
			# has a record
			last_point = file_operation(self.fd)._file_load_pointer()
		else:
			# first time
			# just once when training task running
			if file_size < ava_mem:
				file_operation(self.fd, data_size = file_size)._file_store_pointer()
				return numpy_converter(self.fd, data_size = file_size, case = 3)._status()
			elif file_size >= ava_mem:
				file_operation(self.fd, data_size = ava_mem)._file_store_pointer()
				return numpy_converter(self.fd, data_size = ava_mem, case = 4)._status()
				
		if last_point < file_size:                
			left_data_size = file_size - last_point
			# smaller than momory size
			if left_data_size < ava_mem:
				agg_size = left_data_size + last_point # 目前讀取總共佔檔案大小
				file_operation(self.fd, agg_size)._file_store_pointer()
				# return train data and test data
				del agg_size
				return numpy_converter(self.fd, data_size = left_data_size, case = 0)._status()
			# bigger than memory size
			elif left_data_size >= ava_mem:
				agg_size = ava_mem + last_point # 目前讀取總共佔檔案大小
				file_operation(self.fd, agg_size)._file_store_pointer() # store last data size to file
				del agg_size
				return numpy_converter(self.fd, data_size = ava_mem, case = 1)._status()

class numpy_converter():
	def __init__(self, 
				 fd, 
				 data_size,
				 case = None):
		self.fd = fd
		self.data_size = data_size
		self.case = case
	
	def _status(self):
		# 0 ~ 1: has a record
		# 2 ~ 3: hasn't record
		# case0: read all 
		if self.case == 0:
			with open(self.fd, "r") as df:
				df.seek(self.data_size, 0)
				reader = df.readlines()
				Lines = [line.strip().split(",") for line in reader[1:]]
				del reader
				data = np.array(Lines)
				del Lines
				return data
		# case1:read a specific size
		elif self.case == 1:
			with open(self.fd, "r") as df:
				df.seek(self.data_size, 0)
				reader = df.readlines(self.data_size)
				Lines = [line.strip().split(",") for line in reader[1:]]
				del reader
				data = np.array(Lines)
				del Lines
				return data
		# case2: read all
		elif self.case == 2:
			with open(self.fd, "r") as df:
				reader = df.readlines()
				Lines = [line.strip().split(",") for line in reader[1:]]
				del reader
				data = np.array(Lines)
				del Lines
				return data
		# case3: read a specific size
		elif self.case == 3:
			with open(self.fd, "r") as df:
				reader = df.readlines(self.data_size)
				Lines = [line.strip().split(",") for line in reader[1:]]
				del reader
				data = np.array(Lines)
				del Lines
				return data

class file_operation:
	def __init__(self,
				fd, 
				data_size = None):
		self.fd = fd
		self.data_size = data_size
	
	def _file_store_pointer(self):
		# read file and build each length in list
		with open(self.fd, "rb") as df:
			row_size = SizedReader(df)
			reader = csv.reader(row_size)
			for row in reader:
				pos = row_size.size
				if pos > self.data_size:
					with open("./tmp/file_ckpt.txt", "w") as wf:
						wf.write(str(pos))
						break
	
	def _file_load_pointer(self):
		# load last position about csv file
		with open("./tmp/file_ckpt.txt", "r") as df:
			reader = df.read()
			last_pos = int(reader)
			return last_pos

class SizedReader:
    def __init__(self, fd, encoding='utf-8'):
        self.fd = fd
        self.size = 0
        self.encoding = encoding   # specify encoding in constructor
    def __next__(self):
        line = next(self.fd)
        self.size += len(line)
        return line.decode(self.encoding)   # returns a decoded line
    def __iter__(self):
        return self

# TODO: need
# ckpt aggregation all tmp file and clean
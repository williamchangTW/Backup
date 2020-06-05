import os
import shutil
# import correctness_check
# list file path and do correctness check
# move uncorrect file to TEMP
# searching DATA File
# checkDATA renew
# read file that content "DONE"
# mantain COR filepath only exist 2 correct data file
def checkDATA(data_path, cor_path):
	data_list = os.listdir(data_path)
	for elements in range(len(data_list) - 1):
		with open(data_path + data_list[elements], "r") as df:
			firstline = len(df.readline().split(","))
			secondline = len(df.readline().split(","))
			if secondline > firstline:
				os.remove(data_path + data_list[elements])
			
	'''
	# for tensorflow dataset
	with open(data_path + data_list[0], "r") as df: 
		origin_data = df.read()
		with open(data_path + data_list[0], "w") as wf:
			wf.write("import tensorflow\n" + origin_data)
	with open(data_path + data_list[1], "r") as df:
		origin_data = df.read()
		with open(data_path + data_list[1], "w") as wf:
			wf.write("import tensorflow\n" + origin_data)
	'''
	while len(os.listdir(data_path + cor_path)) > 2:
		cor_num = os.listdir(model_path + cor_path) 
		var1 = os.path.getctime(data_path + cor_path + cor_num[0]) // 1000
		var2 = os.path.getctime(data_path + cor_path + cor_num[1]) // 1000
		var3 = os.path.getctime(data_path + cor_path + cor_num[2]) // 1000
		if var1 > var3 and var1 > var2:
			os.remove(data_path + cor_path + cor_num[0])
		elif var2 > var3 and var2 > var1:
			os.remove(data_path + cor_path + cor_num[1])
		elif var3 > var1 and var3 > var2:
			os.remove(data_path + cor_path + cor_num[2])
		else:
			os.remove(data_path + cor_path + cor_num[2])
			
# check model file structure
# add checkpoint to model file
# mantian COR filepaht only exist 1 correct model file
def checkMODEL(model_path, cor_path):
	model_list = os.listdir(model_path)
	# import every necessary library to model file
	for elements in range(len(model_list) - 1):
		with open(model_path + model_list[elements], "rt") as df:
			origin_model = df.read()
			with open(model_path + model_list[elements], "wt") as wf:
				wf.write("import keras\n" +
					"from keras.models import *\n" +
					"from keras.layers import *\n" +
					"from keras.optimizers import *\n" +
					 origin_model)
			# add checkpoint to file
			# write to corrct file
			with open(model_path + model_list[elements], "rt") as file:
				pos = file.read().find("model.fit(")
				file.seek(pos + 10)
				ch = file.read().find("callbacks")
				if ch != -1:
					pos = pos + ch
					file.seek(pos)
					ch_leftbracket = file.read().find("[")
					file.seek(pos + ch_leftbracket)
					ch_rightbracket = file.read().find("]")
					length = ch_rightbracket
					file.seek(pos + ch_leftbracket + 1)
					rep = file.read(length - 1)
					file.seek(0)
					data = file.read().replace(rep, "checkPoint()")
					fout = open(model_path + cor_path + model_list[elements], "wt")
					fout.write(data)
					fout.close()
				else:
					cor_flag = False
					while cor_flag == False:
						file.seek(pos)
						left_bracket = file.read().find("(")
						file.seek(pos)
						terminator = file.read().find("\n")
						if terminator < left_bracket:
								file.seek(pos)
								right_bracket = file.read().find(")")
								if right_bracket < terminator:
									pos = pos + right_bracket
									file.seek(0)
									data = file.read()
									with open(model_path + cor_path + model_list[elements], "wt") as fout:
										fout.write(data)
										fout.seek(0)
										fout.seek(pos)
										fout.write(", callbacks=[checkPoint()])")
										fout.close()
									cor_flag = True
						elif left_bracket == -1:
							file.seek(pos)
							right_bracket = file.read().find(")")
							pos = pos + right_bracket
							file.seek(0)
							data = file.read()
							with open(model_path + cor_path + model_list[elements], "wt") as fout:
								fout.write(data)
								fout.seek(0)
								fout.seek(pos)
								fout.write(", callbacks=[checkPoint()])")
								fout.close()
							cor_flag = True
						else:
							pos = pos + terminator + 2
	while len(os.listdir(model_path + cor_path)) > 1:
		cor_num = os.listdir(model_path + cor_path) 
		var1 = os.path.getctime(model_path + cor_path + cor_num[0]) // 1000
		var2 = os.path.getctime(model_path + cor_path + cor_num[1]) // 1000
		if var1 > var2:
			os.remove(model_path + cor_path + cor_num[0])
		else:
			os.remove(model_path + cor_path + cor_num[1])

def clearPATH(data_path, model_path, cor_path):
	if os.path.exists(data_path + "__pycache__") == True:
		shutil.rmtree(data_path + "__pycache__")
	if os.path.exists(data_path + cor_path + "__pycache__") == True:
		shutil.rmtree(data_path + cor_path +"__pycache__")
	if os.path.exists(model_path + "__pycache__") == True:
		shutil.rmtree(model_path + "__pycache__")
	if os.path.exists(model_path + cor_path + "__pycache__") == True:
		shutil.rmtree(model_path + cor_path +"__pycache__")

if __name__ == "__main__":				
	data_path = "./DATA/"
	model_path = "./MODEL/"
	cor_path = "COR/"
	# check model & data file are not empty
	while len(os.listdir(data_path)) == 0 or len(os.listdir(model_path)) == 0:
		print("data file or model file is empty!")
		time.sleep(10)
	os.mkdir(data_path + cor_path)
	os.mkdir(model_path + cor_path)
	clearPATH(data_path, model_path, cor_path)
	# check file is correct and write to COR path 
	checkDATA(data_path, cor_path)
	# check file is correct and write to COR path
	checkMODEL(model_path, cor_path)
	



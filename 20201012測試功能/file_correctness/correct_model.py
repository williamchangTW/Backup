import os
import shutil
import sys
import time
# import correctness_check
# list file path and do correctness check
# move uncorrect file to TEMP
# read file that content "DONE"
# mantain COR filepath only exist 2 correct data file
# check model file structure
# add checkpoint to model file
# mantian COR filepaht only exist 1 correct model file
def checkMODEL():
	model_path = "./model/"
	cor_path = model_path + "cor/"
	# check file path
	if len(os.listdir(model_path)) == 0:
		print("model path is empty!\n")
		sys.exit(0)
	model_list = os.listdir(model_path)
	# if path file more than 1 then just read newest
	# list all model file
	for elements in range(len(model_list)):
	# can not found the keyword
		if model_list[elements] == "cor":
			continue
		df = open(model_path + model_list[elements], "rt")
		pos1 = df.read().find("model.fit(")
		print(str(pos1))
		df.seek(0)
		pos2 = df.read().find("train")
		print(str(pos2))
		df.seek(0)
		pos3 = df.read().find("test")
		print(str(pos3))
		# keyword can not found
		if pos1 == -1 or pos2 == -1 or pos3 == -1:
			print("model file doesnt follow the rules to write\n")
			sys.exit(0)
	# move all model file to cor
		else:
			shutil.copyfile(model_path + model_list[elements], cor_path + model_list[elements])
	# bubble sort
	# keep a newest one
	model_list = os.listdir(cor_path)
	if len(model_list) > 2:
		for elements in range(len(model_list) - 1):
			var1 = cor_path + model_list[elements]
			var2 = cor_path + model_list[elements + 1]
			if os.path.exists(var1) and os.path.exists(var2) == True:
				time1 = os.path.getctime(var1) // 1000
				time2 = os.path.getctime(var2) // 1000
				if time1 > time2:
					os.remove(var2)
				else:
					os.remove(var1)
			else:
				break
	# add checkpoint to file
	# write to corrct file
	with open(cor_path + "model.py", "rt") as wf:
		pos = wf.read().find("model.fit(")
		wf.seek(pos + 10)
		ch = wf.read().find("callbacks")
		if ch != -1:
			pos = pos + ch
			wf.seek(pos)
			ch_leftbracket = wf.read().find("[")
			wf.seek(pos + ch_leftbracket)
			ch_rightbracket = wf.read().find("]")
			length = ch_rightbracket
			wf.seek(pos + ch_leftbracket + 1)
			rep = wf.read(length - 1)
			wf.seek(0)
			data = wf.read().replace(rep, "checkpoint.modelCkpt()")
			fout = open(cor_path + "model.py", "wt")
			fout.write(data)
			fout.close()
		else:
			cor_flag = False
			while cor_flag == False:
				wf.seek(pos)
				left_bracket = wf.read().find("(")
				wf.seek(pos)
				terminator = wf.read().find("\n")
				if terminator < left_bracket:
						wf.seek(pos)
						right_bracket = wf.read().find(")")
						if right_bracket < terminator:
							pos = pos + right_bracket - 2
							wf.seek(0)
							data = wf.read()
							with open(cor_path + "model.py", "wt") as fout:
								fout.write(data)
								fout.seek(0)
								fout.seek(pos)
								fout.write(", callbacks=[checkpoint.modelCkpt()])")
								fout.close()
							cor_flag = True
				elif left_bracket == -1:
					wf.seek(pos)
					right_bracket = wf.read().find(")")
					pos = pos + right_bracket - 2
					wf.seek(0)
					data = wf.read()
					with open(cor_path + "model.py", "wt") as fout:
						fout.write(data)
						fout.seek(0)
						fout.seek(pos)
						fout.write(", callbacks=[checkpoint.modelCkpt()])")
						fout.close()
					cor_flag = True
				else:
					pos = pos + terminator + 2	


# make a single checkpoint file

def make_ckpt():
	# data path in tmp
	# read and open every log files
	log_path = "./tmp/"
	# record data pointer
	with open(log_path + "data_pointer.txt") as df:
		d_p = df.read().strip()
	# record data coherence path
	with open(log_path + "data_path.txt") as df:
		d_c = df.read().strip()
	# record model coherence path
	with open(log_path + "model_path.txt") as df:
		m_c = df.read().strip()
	# record model already training epochs
	# record model lase training epochs
	with open(log_path + "t_epochs.txt") as df:
		t_e = df.readline().strip()
		l_e = df.readline().strip()
	# record training path
	with open(log_path + "training_path.txt") as df:
		t_p = df.read().strip()
	# aggregate to a single file
	with open("./ckpt/" + t_p + "training_log.txt", "w") as wf:
		wf.write(d_p + "\n" 
				+ d_c + "\n" 
				+ m_c + "\n" 
				+ t_e + "\n"
				+ l_e + "\n")
	# clean path?
	


# target:
# 1. daemon registration
# 2. daemon execution
# 3. chekc data
# 4. check model
# 5. change epoch

import os
import glob
import sys
import subprocess
import filecmp
import threading
from ..csv_loader import csv_loader

# produce a semaphore key
key = threading.Semaphore(value = 1)

# call daemon to work in background
class start_daemon:
    def __init__(self):
        path = os.getcwd()
        subprocess.Popen(args=["gnome-terminal", "--command=python3 " + path + "./environment_detector/envir_daemon.py"], shell=False)

# find epoch position and return its value
class find_epoch:
    def __init__(self, 
                 path):
        self.path = path
    def get_epochs(self):
        with open(self.path, "r") as df:
	        # checkpoint compare epochs
            pos_begin = df.read().find("epochs")
            if pos_begin != -1:
                # <<epoch search section>>
                # scan next char
                loc = pos_begin + 5
                df.seek(loc)
                pos_eq = df.read().find("=")
                # scan next char
                loc_eq = pos_begin
                df.seek(loc_eq)
                pos_end = df.read().find(",")
                # <<epoch search section>>
                # <<model fit search section>>
                df.seek(0)
                pos_fit = df.read().find("model.fit")
                # scan next char
                df.seek(loc + pos_eq + 1)
                tar = df.readline().split(",")
                # <<model fit search section>>
                # <<validation search section>>
                # scan validation
                df.seek(0)
                val_loc = df.read().find("validation_split")
                df.seek(val_loc + 16)
                temp_eq = df.read().find("=")
                df.seek(val_loc + 16 + temp_eq + 1)
                tar = df.readline().split(",")
                pos_val = tar[0]
                # <<validatino search section>>
                # returm position in a file
                # pos_begin: epochs begin point
                # pos_end: epochs end point
                # pos_fit: model fit point
                # pos_val: validation point
                return pos_begin, pos_end, pos_fit, pos_val
            else:
                print("file is not correct!")
                return IOError 


# recover system status
class recovery_check:
    def __init__(self,
                 fd = None):
        self.fd = fd
    
    def _check(self):
        # col0: data seek pointer
        # col1: data path
        # col2: model path
        # col3: training ckpt path
        # col4: training epochs
        # col5: training last epochs
        try:
            with open(self.fd, "r") as df:
                for i in range(0, 6):
                    tar = df.readline()
                    if i == 1:
                        # data path
                        recovery_check()._check_data(tar)
                    elif i == 2:
                        # model path 
                        recovery_check()._check_model(tar)
                        tmp = tar
                    elif i == 5:
                        # model path and epochs
                        if tar != 0:
                            recovery_check()._change_epochs(tmp, tar)
                            recovert_system_status()
                        else:
                            # presenct training task is done
                            print("Training is finished!")
                            sys.exit(0)
        except:
            return IOError    
    def _check_data(self, data_path):
        # data procedure path
        try:
            if os.path.exists(data_path) and filecmp.cmp("./data/cor/data.csv", data_path):
                print("correct!")
            else:
                return IOError
        except:
            return IOError

    def _check_model(self, model_path):
        # model ckpt path
        try:
            if os.path.exists(model_path) and filecmp.cmp("./model/cor/model.py", model_path):
                print("correct!")
            else:
                return IOError
        except:
            return IOError

    def _change_epochs(self, model_path, epochs):
        # change epochs
        pos1, pos2, pos3, pos4 = find_epoch(model_path).get_epochs()
        with open(model_path, "r+") as df:
            forehead = df.read(pos3)
            df.seek(0)
            df.seek(pos1 + pos2)
            button = df.read()
            with open(model_path, "w+") as wf:
                wf.write(forehead + 
                        "model.load_weights('" +
                        epochs + 
                        "')\n" +
                        "model.fit(train, test, validation_split=" +
                        str(pos3) + 
                        ",epochs=" + 
                        str(pos4) +
                        button)
        

# starting recovery training task
# steps:
# 1. loading process of file operation
# 2. loading model training result and keep training until finish
def recovert_system_status():
    # call ckpt to run tarining task
    subprocess.call([sys.executable, "model.py"])
import sys, subprocess, os, signal
#import platform components
import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Reshape, Conv2D, AveragePooling2D, Flatten
from keras.layers import MaxPooling2D
from keras.optimizers import adam
from DynamicLoader import dynamic_memory, numpy_converter
from FileCorrect import correct_model, correct_data, clear_path
from Checkpoint import checkpoint, checkpoint_debug
from Recovery import recovery_process, recovery_check
from EnvironmentCheck import envir_daemon, wifi_check, bat_check, sys_check, mem_check, start_daemon

def datapreprocess(data_train, x_test):
    n_samples_test = x_test.shape[0]
    y_train = np.array(data_train[:, 0])
    x_train = np.array(data_train[:, 1:])
    y_train = keras.utils.to_categorical(y_train, num_classes = 10)
    return x_train, y_train

class GracefulKiller:
	kill_now = False
	def __init__(self):
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)
	def exit_gracefully(self,signum, frame):
		self.kill_now = True

# make sure process is not duplicate
pid = os.getpid()
with open("train_pid.txt", "w") as wf:
	wf.write("tradinPID: " + str(pid) + "\n")
	wf.close()
# recieve user input and run file correctness check
# start to read user input
# dynamic loader
train = dynamic_memory.dynamicLoad("./DATA/COR/train.csv")
test = dynamic_memory.dynamicLoad("./DATA/COR/test.csv")
train, test = datapreprocess(train, test)
killer = GracefulKiller()
# model part

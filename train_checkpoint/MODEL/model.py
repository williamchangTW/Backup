import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *
import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *
import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *
model = tensorflow.keras.models.Sequential([
	keras.layers.Dense(512, activation='relu', input_shape=(784,)),
	keras.layers.Dropout(0.2),
	keras.layers.Dense(10, activation='softmax')
  ])

model.compile(optimizer='adam',
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy'])

model.fit(train_images,
	train_labels,
	epochs = 10,
	validation_data = (test_images, test_labels),
	callbacks=[checkpoint()]
	)

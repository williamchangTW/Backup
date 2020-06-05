import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *
# test comment
# test comment
#testtemp
'''
test comment
'''
model_name = "LaNet5"
model = Sequential()
model.add(Reshape(target_shape=(1, 28, 28), input_shape=(784,)))
model.add(Conv2D(kernel_size=(3, 3), filters=6, padding="same", data_format="channels_first", kernel_initializer="uniform", use_bias=False))
model.add(MaxPooling2D(pool_size=(2, 2), data_format="channels_first"))
model.add(Conv2D(kernel_size=(5, 5), filters=16, padding="same", data_format="channels_first", kernel_initializer="uniform", use_bias=False))
model.add(MaxPooling2D(pool_size=(2, 2), data_format="channels_first"))
model.add(Conv2D(kernel_size=(5, 5), filters=120, padding="same", data_format="channels_first", kernel_initializer="uniform", use_bias=False))
model.add(Flatten())
model.add(Dense(output_dim=120, activation='relu'))
model.add(Dense(output_dim=120, activation='relu'))
model.add(Dense(output_dim=10, activation='softmax'))

adam = keras.optimizers.Adam(lr=0.0005, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])

model.fit(x_train, y_train, epochs=20, batch_size=64)
y_pred = model.predict_classes(x_test)
#output_prediction(y_pred, model_name)
y_all_pred[0] = y_pred

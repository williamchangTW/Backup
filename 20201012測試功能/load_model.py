import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

def get_model():
    model = keras.Sequential()
    model.add(keras.layers.Dense(1, input_dim=784))
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=0.1),
        loss="mean_squared_error",
        metrics=["mean_absolute_error"],
    )
    return model

# Load example MNIST data and pre-process it
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

# Limit the data to 1000 samples
x_train = x_train[:1000]
y_train = y_train[:1000]
x_test = x_test[:1000]
y_test = y_test[:1000]

file_path = "tmp/"

model = get_model()
'''
model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=30,
    verbose=1,
    validation_split=0.5
)
'''
loss, acc = model.evaluate(x_train,  x_test, verbose=1)
print("Untrained model, accuracy: {:5.2f}%".format(100*acc))
import tensorflow
(train_images, train_labels), (test_1, test_2) = tensorflow.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0

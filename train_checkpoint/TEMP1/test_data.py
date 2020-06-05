import tensorflow
(train_1, train_2), (test_images, test_labels) = tensorflow.keras.datasets.mnist.load_data()

test_labels = test_labels[:1000]
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

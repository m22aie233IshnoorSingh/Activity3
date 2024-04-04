import tensorflow as tf
from tensorflow.keras import layers, models

#creating a basic model architecutre here
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

print(model.summary())

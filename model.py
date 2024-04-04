import tensorflow as tf
from tensorflow.keras import layers, models

# better model architecture for version2.0 this has
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

model.summary()

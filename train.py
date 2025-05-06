import numpy as np
import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout
import tensorflow as tf

# Directory and Image Parameters
base_dir = './data/'
img_size = 224
batch = 64
epochs = 30

# Image Data Generator with augmentation
train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, validation_split=0.2)
test_datagen = ImageDataGenerator(rescale=1. / 255, validation_split=0.2)

# Creating training and validation datasets
train_generator = train_datagen.flow_from_directory(base_dir, target_size=(img_size, img_size), subset='training', batch_size=batch, class_mode='categorical')
validation_generator = test_datagen.flow_from_directory(base_dir, target_size=(img_size, img_size), subset='validation', batch_size=batch, class_mode='categorical')

# CNN Model Definition
model = Sequential([
    Conv2D(64, (5, 5), padding='same', activation='relu', input_shape=(img_size, img_size, 3)),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), padding='same', activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(5, activation='softmax')  # 5 classes for the flowers
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Training the model
history = model.fit(train_generator, epochs=epochs, validation_data=validation_generator)

# Save the model
model.save('Model.h5')

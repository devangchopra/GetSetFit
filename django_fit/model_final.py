import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D, Flatten
from tensorflow.keras.optimizers import Adam, SGD


class ModelPredictor:
    def ml_search(image_path):
        model =tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Conv2D(64, (3,3), activation ='relu'),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dense(7, activation='softmax')
        ])


        checkpoint_path="./checkpoint/cp.ckpt"
        # checkpoint_dir=os.path.dirname(checkpoint_path)
        model.load_weights(checkpoint_path)


        labels=['bread', 'chai', 'egg_boiled', 'egg_omlet', 'rice', 'roti', 'yellow_dal']


        #---------------------------path for image
        path=image_path


        
        # path=r"C:\Users\arora\OneDrive\Desktop\45.jpg"
        img= image.load_img(path,target_size=(150,150))
        x= image.img_to_array(img)
        x=np.expand_dims(x, axis=0)

        images=np.vstack([x])
        classes=model.predict(images, batch_size=7)[0]

        cout=0

        for i in range(6):
            if classes[i]>classes[i+1]:
                classes[i+1]=classes[i]
            else:
                cout+=1

        return labels[cout]
    

# try:
#     mk =ModelPredictor.ml_search(image_path="/home/vaibhav/Documents/hack_the_mountains/data/test/rice/45.jpg")
#     print("++", mk, "++")

# except:
#     print(Exception)
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import load_model
import tensorflow as tf
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# def predict(img_path):
def getPrediction(filename):
     print(dir_path)
     path_to_file = os.path.join(dir_path,"Model")
     print("file directory is--> "+ path_to_file)
     if os.path.isfile(path_to_file):
          print("------------ Model file exists -----------")
     model = load_model(os.path.join(dir_path,"Model"))

     path_to_image = os.path.join(dir_path,"upload",filename)
     img = load_img(path_to_image, target_size=(180, 180))
     img = img_to_array(img)
     img = img / 255
     img = np.expand_dims(img,axis=0)
     category = np.argmax(model.predict(img), axis=-1)
     answer = category[0]
     probability = model.predict(img)
     probability_results = 0

     if answer == 1:
          answer = "Recycle"
          probability_results = probability[0][1]
     else:
          answer = "Organic"
          probability_results = probability[0][0]

     answer = str(answer)
     probability_results=str(probability_results)

     values = [answer, probability_results, filename]
     return values[0], values[1], values[2]

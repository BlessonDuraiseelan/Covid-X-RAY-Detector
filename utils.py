import os
#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"]="-1"  # or even "-1"

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from glob import glob

model = load_model('resnet_chest.h5')

def pipeline_model(path):
    model = load_model('resnet_chest.h5')
    img = image.load_img(path,target_size=(224,224))
    img = image.img_to_array(img)
    img = img/255.0
    img = np.expand_dims(img,axis=0)

    pred = model.predict(img)
    probability = pred[1]
    print("Resnet Predictions:")
    if probability[0] > 0.5:
      pred_resnet = str('COVID') 
    else:
      pred_resnet = str('NonCOVID')

    return pred_resnet
    
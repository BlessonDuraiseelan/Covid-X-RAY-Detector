# Covid-X-RAY-Detector

This python web app based on Transfer Learning and Convolution Neural Nerwork is developed for the detection of Covid in a patient  from the X-Ray that is uploaded by the  the user. The model is trained  on multiple
images of Covid X Rays and Non-Covid X Rays. Resnet 50 model is used to train the model. A Flask App was developed where the user can upload Chest X-rays and get the output of possibility of COVID infection.

# Dataset and Model
The model which was developed for the training of detection of Covid from the X-Rays had to be trained on multiple X-Ray images of Covid samples as well as Non-Covid Samples.

The following datasets were used to train the model for our requirements:

COVID X-RAY DATASET -https://github.com/ieee8023/covid-chestxray-dataset

NORMAL X-RAY - https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

The model was trained on the mentioned image datasets and  Transfer Learning algorithm Resnet 50 was used in order to check its performance on training the images as well as training the base leyers.

After the Resnet operation was completed the model was trained by performing  normal convolution operations on the subsequent layers keeping the initial layers non-active.

The model was trained for 95 epochs in order for the model to learn the features of the training images.
Various metrics were used in order to check the performance of the model.
The trained  model was  saved in h5 format saved for futher use in flask api for prediction purposes.

![kisspng-flask-python-web-framework-bottle-microframework-django-5b3d0ba62504c0 3512153115307273341516](https://user-images.githubusercontent.com/76935226/149612516-23d78698-0718-4537-acb8-042ab27f4d3e.jpg)
![image](https://user-images.githubusercontent.com/76935226/149612569-32b26f50-2363-473a-81bb-caea72043eaa.png)
![0_py5zo1OGahLBVM-o](https://user-images.githubusercontent.com/76935226/150628579-076b199f-8e9b-4005-ba99-0e6805a0d73b.gif)


A Flask app was developed where the user can provide thier X-Ray image and the model will detect if the image input belongs to Covid or NonCovid group.

![Screenshot (184)](https://user-images.githubusercontent.com/76935226/150754595-7d3a4369-b358-4acd-89a1-a960bc0276b1.png)
![Screenshot (182)](https://user-images.githubusercontent.com/76935226/150754618-a8d1d416-0962-41fd-90c4-108e02faefc6.png)
![Screenshot (183)](https://user-images.githubusercontent.com/76935226/150754644-051043aa-bbf7-4cec-8ceb-2c4806f887d1.png)





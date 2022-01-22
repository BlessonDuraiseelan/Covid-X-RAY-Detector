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

The model was trained for 90 epochs in order for the model to learn the features of the training images.
Various metrics were used in order to check the performance of the model.
The trained  model was  saved in h5 format saved for futher use.

![kisspng-flask-python-web-framework-bottle-microframework-django-5b3d0ba62504c0 3512153115307273341516](https://user-images.githubusercontent.com/76935226/149612516-23d78698-0718-4537-acb8-042ab27f4d3e.jpg)
![image](https://user-images.githubusercontent.com/76935226/149612569-32b26f50-2363-473a-81bb-caea72043eaa.png)

A Flask app was developed where the user can provide thier X-Ray image and the model will detect if the image input belongs to Covid or NonCovid group.

![Screenshot (162)](https://user-images.githubusercontent.com/76935226/148753898-dbeb483f-680b-4cd1-a2d3-c1ec96257ea7.png)
![Screenshot (163)](https://user-images.githubusercontent.com/76935226/148753914-d10af011-f637-41e2-a392-3cc1b43ca3f1.png)
![Screenshot (164)](https://user-images.githubusercontent.com/76935226/148753923-8c53581e-f830-40f1-a815-1bd086702c54.png)
![Screenshot (165)](https://user-images.githubusercontent.com/76935226/148753853-93c201e3-5022-44ff-bac2-879fab731acf.png)

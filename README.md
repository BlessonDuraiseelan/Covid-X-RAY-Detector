# Covid-X-RAY-Detector

This web app is developed for the detection of Covid from the X-Ray that is uploaded by the  the user. We have trained the model on multiple
images of Covid X Rays and Non-Covid X Rays. Resnet 50 model is used to train the model. A Flask App was developed where the user can upload Chest X-rays and get the output of possibility of COVID infection.

# Dataset and Model
When training the model of Covid detection there is a requirement of Covid  X-Ray images and non- Covid X-Ray Images.
The following datasets were used to train the model for our requirements:

COVID X-RAY DATASET -https://github.com/ieee8023/covid-chestxray-dataset

NORMAL X-RAY - https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

The model was trained on the mentioned image datasets and  Transfer Learning algorithm Resnet 50 was used where training process was applied on the the base layers and then normal convolution operations were performed keeping the initial layers.
We ran around 90 epochs for the model for the model to learn and ran metrics to check for the performance.
The trained  model was  saved in h5 format saved for futher use.

A Flask app was developed where the user can provide thier X-Ray image and the model will detect if the image input belongs to Covid or NonCovid group.

![Screenshot (162)](https://user-images.githubusercontent.com/76935226/148753898-dbeb483f-680b-4cd1-a2d3-c1ec96257ea7.png)
![Screenshot (163)](https://user-images.githubusercontent.com/76935226/148753914-d10af011-f637-41e2-a392-3cc1b43ca3f1.png)
![Screenshot (164)](https://user-images.githubusercontent.com/76935226/148753923-8c53581e-f830-40f1-a815-1bd086702c54.png)
![Screenshot (165)](https://user-images.githubusercontent.com/76935226/148753853-93c201e3-5022-44ff-bac2-879fab731acf.png)

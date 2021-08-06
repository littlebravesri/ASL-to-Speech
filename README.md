# American Sign Language translation to Speech 

## Microsoft Student Accelerator Program 

A project to use Azure Services to build a web app that converts real time sign language gestures into text and speech

### Idea

The idea of the project is to help the people who cannot hear and/or speak to communicate with others naturally and effortlessly. The web app will detect the sign language in real time and convert the actions in video to text which will also be recited. 

AI can be used to automate the sign language detection and prediction in real time. With the AI enabled web application, people who know and do not know sign language can communicate withiut any barrier. 

### Approach and Implementation

The architecture of the web app includes a machine learning model and a web cam. The macine learning model manipulates image classification algorithm. The signs in the frames of the video captured the webcam will be predicted and the corresponding alphabet will be displayed and spoken in the web app next to the camera. 

Image classification method was the chosen approach to implement the project where the signs are classified into 26 classes/categories (26 alphabets). The project can also be extended to by being implemented by object detection method and using an IoT device/camera to detect the objects/signs in real time.

The web app was implemented with the help of Azure services. Images of the American Sign Language was uploaded in the Azure portal after being preprocessed [converting color images to grayscale, edge detection (in file Data Preprocessing.ipynb)]. The machine learning model was trained using the Azure Custom Vision service. The model was published and the web app is deployed using the Azure App Service. 

In future, in addition the the ASL alphabets, words and phrases can be added to train the model to scale the use of the application. Due to the limitation of allowed number of training images for the project and the API calls for the Azure free account, 15 images per alphabet were uploaded to train the model, resulting in less accurate predictions. More number of images can be added for more accurate predictions with more training time. 
 
### Result and Summary

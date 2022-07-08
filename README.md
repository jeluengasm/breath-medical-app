# Breath Medical App

Project created to reduce diagnosis time, improve its accuracy and reduce the probability of a misdiagnosis in low-level hospitals. This  will be accomplished by making use of specifically respiratory sounds as indicators of both respiratory health disorders, this sound  is directly related to air movement, changes within lung tissue and the position of secretions within the lung, and is captured with a stethoscope. This element can also give early  alerts about possible diseases that the patient may suffer.

In this repository, you will find the breathe application, whose general objective is diagnostic support for diseases related to heart sounds. Seven main views were created, in which there are forms, patient list, audio analysis section, EDA page and authentication page. 
One of the main views is the patient's page, where the data of each recorded audio is stored with the same id, so the diagnosis made by the doctor is known. Another view is the list of patients where it is redirected to their personal data forms, in which the information is edited. Within this same view is the option to add a new patient

## Create an account

Creating an account is required to manage the app. To do this, it is recommended that you locate it in the 'breath-medical-app/breathmedical/' folder:

$ breath-medical-app/breathmedical/ python manage createsuperuser

It will ask you for some data to create the user. Once the user is created, you will be able to see the information of the application administrator (if the link)

http://breath-medical-app.herokuapp.com/admin

## Download files

Next, the dataset used is presented, as well as the files corresponding to the weights of the constructed neural network and other elements. You can download the information at the following link:

https://drive.google.com/drive/folders/13Pec9kDipsa4OTe6VrEbgrJs5ntrnJbT?usp=sharing


## Important links:

### Administrator for managing the models in the database (superuser permissions required):

http://breath-medical-app.herokuapp.com/admin
![image](https://user-images.githubusercontent.com/22754704/177916130-49044369-8321-4994-a235-d3b0e58ac637.png)

![image](https://user-images.githubusercontent.com/22754704/177916180-7448ee98-5096-4dd9-9a92-514ce149d094.png)

![image](https://user-images.githubusercontent.com/22754704/177916206-1d3d50aa-4a33-4cff-ab26-5373b73627c8.png)

![image](https://user-images.githubusercontent.com/22754704/177916237-457aa9bd-33f6-43cb-890f-2a8f1e0cbdcc.png)


### Menu for entry of registered users:

http://breath-medical-app.herokuapp.com/login/

![image](https://user-images.githubusercontent.com/22754704/177916686-f97dc942-2907-4de6-bf94-aa8daa6e400e.png)


###New user registration form (patients only):

http://breath-medical-app.herokuapp.com/register/

![image](https://user-images.githubusercontent.com/22754704/177916697-64bdccca-3062-459e-aa98-c3cd5321206a.png)


### Main page for patient view:

http://breath-medical-app.herokuapp.com/patient/<int:patient_id>/

![image](https://user-images.githubusercontent.com/22754704/177916056-19e028cf-f248-4048-8e0b-b7707642dc7e.png)


### Dashboard of doctors who have access credentials to the platform

http://breath-medical-app.herokuapp.com/medic/<int:medic_id>/

![image](https://user-images.githubusercontent.com/22754704/177916359-0a3a5032-a550-4077-a634-0e6c2ea62bfc.png)


### Form for creating new audios and passing the audios to the trained model:

http://breath-medical-app.herokuapp.com/medic/<int:medic_id>/history/<int:history_id>/new-audio/

![image](https://user-images.githubusercontent.com/22754704/177916471-0087a888-1361-4186-9c81-8a9c43925ce3.png)


### Analysis of the audio introduced by the doctor, with the diagnosis given by the trained model:

http://breath-medical-app.herokuapp.com/history/<int:history_id>/analysis/<int:audio_id>/

![image](https://user-images.githubusercontent.com/22754704/177916859-b0fb82d4-f805-4f74-a12c-1325148bb698.png)

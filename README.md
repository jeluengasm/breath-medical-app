# Breath Medical App

Project created to reduce diagnosis time, improve its accuracy and reduce the probability of a misdiagnosis in low-level hospitals. This  will be accomplished by making use of specifically respiratory sounds as indicators of both respiratory health disorders, this sound  is directly related to air movement, changes within lung tissue and the position of secretions within the lung, and is captured with a stethoscope. This element can also give early  alerts about possible diseases that the patient may suffer.

In this repository, you will find the breathe application, whose general objective is diagnostic support for diseases related to heart sounds. Seven main views were created, in which there are forms, patient list, audio analysis section, EDA page and authentication page. 
One of the main views is the patient's page, where the data of each recorded audio is stored with the same id, so the diagnosis made by the doctor is known. Another view is the list of patients where it is redirected to their personal data forms, in which the information is edited. Within this same view is the option to add a new patient

## Create an account

Se requiere crear una cuenta para administrar la aplicación. Para ello, se recomienda que se ubique en la carpeta 'breath-medical-app/breathmedical/':

$ breath-medical-app/breathmedical/ python manage createsuperuser

Le pedirá unos datos para crear el usuario. Una vez esté creado el usuario, usted podrá ver la información del administrador de la aplicación (if al enlace)

http://breath-medical-app.herokuapp.com/admin 

## Download files

A continuación, se presenta el dataset utilizado, así como los archivos correspondientes a los pesos de la red neuronal construida y demás elementos. En el siguiente enlace se puede descargar la información:

https://drive.google.com/drive/folders/13Pec9kDipsa4OTe6VrEbgrJs5ntrnJbT?usp=sharing


## Enlaces importantes:

### Administrador para la gestión de los modelos en la base de datos (requieren permisos de superusuario):

http://breath-medical-app.herokuapp.com/admin
![image](https://user-images.githubusercontent.com/22754704/177916130-49044369-8321-4994-a235-d3b0e58ac637.png)

![image](https://user-images.githubusercontent.com/22754704/177916180-7448ee98-5096-4dd9-9a92-514ce149d094.png)

![image](https://user-images.githubusercontent.com/22754704/177916206-1d3d50aa-4a33-4cff-ab26-5373b73627c8.png)

![image](https://user-images.githubusercontent.com/22754704/177916237-457aa9bd-33f6-43cb-890f-2a8f1e0cbdcc.png)


### Menú para ingreso de usuarios registrados:

http://breath-medical-app.herokuapp.com/login/

![image](https://user-images.githubusercontent.com/22754704/177916686-f97dc942-2907-4de6-bf94-aa8daa6e400e.png)


###Formulario de registro de usuarios nuevos (solo pacientes):

http://breath-medical-app.herokuapp.com/register/

![image](https://user-images.githubusercontent.com/22754704/177916697-64bdccca-3062-459e-aa98-c3cd5321206a.png)


### Página principal para vista del paciente:

http://breath-medical-app.herokuapp.com/patient/<int:patient_id>/

![image](https://user-images.githubusercontent.com/22754704/177916056-19e028cf-f248-4048-8e0b-b7707642dc7e.png)


### Dashboard de los médicos que tienen credenciales de acceso a la plataforma

http://breath-medical-app.herokuapp.com/medic/<int:medic_id>/

![image](https://user-images.githubusercontent.com/22754704/177916359-0a3a5032-a550-4077-a634-0e6c2ea62bfc.png)


### Formulario para la creación de nuevos audios y el paso de los audios al modelo entrenado:

http://breath-medical-app.herokuapp.com/medic/<int:medic_id>/history/<int:history_id>/new-audio/

![image](https://user-images.githubusercontent.com/22754704/177916471-0087a888-1361-4186-9c81-8a9c43925ce3.png)


### Análisis del audio introducido por el médico, con el diagnóstico otorgado por el modelo entrenado:

http://breath-medical-app.herokuapp.com/history/<int:history_id>/analysis/<int:audio_id>/

![image](https://user-images.githubusercontent.com/22754704/177916546-a1c78c63-fa10-4f02-a65c-3d970b5ac8f5.png)


# INSTALLITE

## Author
- Chepkirui Betty

### Description  
This is a clone of  Instagram where people share their  images and videos for other users to view. 
Users can sign up, login, view and post photos, search and follow other users.  

### User Story  
  
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  
  
## deployed link
- https://fastinsta.herokuapp.com/

  
### Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/chepkiruibetty/Instagram-clone
```
##### Navigate into the folder and install requirements  
 ```bash 
cd instagram pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.1.28](https://docs.djangoproject.com/en/1.11/)  
* [Heroku](https://heroku.com)  
* [Git]()
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [chepkiruibetty64@gmail.com]  

## Database
<img src="db.png">

## codebeat
- [![codebeat badge](https://codebeat.co/badges/dd43cf3b-9449-413b-8437-2d993fa8d2d2)](https://codebeat.co/projects/github-com-chepkiruibetty-installite-master)

## license

licensed under[MIT license](license).
  
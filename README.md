# Hood Search
A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Screenshot
<img src="https://github.com/AliKheirAbdi/neighborhood/blob/master/screen.png"> 

## User Story  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/AliKheirAbdi/neighborhood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Reviewer pip install -r requirements.txt 
```
##### Install and activate Virtual Env
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  On your database setup User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Migrate  
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
Open the application on your browser `127.0.0.1:8000`.  

## BDD
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Register      | Fill out the reg form | user is created |
| Login     | Enter username and pwd   | Application logs user in |
| Edit Profile | User fills out biodata and photo | Profile is created|
| Add a Neighborhood|Form for neighboord add details| User can add name, neighborhood, location|
| Add a Business|Form for business add details| User can add name, neighborhood, location|
| Share a Post|Form for post add details| User can a post with neighborhood members|

  
## Technologies used  
  
* [Python3.7](https://www.python.org/)  
* [Django 2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com) 
* [Javascript]
  
## Known Bugs  
* There are currently no known bugs.  
  
## Contact Information   
If you are interested in this project or making contributions, please email me at [akheirali(@)gmail.com]  
  
## License 
 MIT License
*Copyright (c) 2019 **Ali Kheir**

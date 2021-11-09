# Asset-inventory

## Author
  - Ali Hared(gediali019@gmail.com)
 

### Description  
This is an asset inventory system that enables an organization to keep track of all the assets and their state, to ensure easy identification of any asset which need repair or purchase.

## User Stories
Procurement Manager
* Sign in with the application to start using it.
* See profile and update it
* Purchase new assets from manufacturers
* Register new assets
* Create new asset category
* Update and delete them

Manager
* Sign in with the application and start using it
* See profile and update it
* Locate assets to employees
* Approve and decline requests from employees

Employees
* Sign in with the application and start using it
* See profile and update it
* Request for a new asset
* Request for repair of an asset

Note: A system admin can do all this from django admin dashboard.

### Deployed link
 assets-inventoryy.herokuapp.com/

### Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/Gedihared6409/asset-inventory.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd asset-inventory pipenv  install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python -m venv virtual 
-(linux)  source virtual/bin/activate
-(windows) virtual/Scripts/activate
```  
##### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations assets
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
```  

##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 3.0.8](https://docs.djangoproject.com/en/3.0/) 
* [Heroku](https://heroku.com)  
* [Git](for version control)

## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug.  

## License

- Licensed under[MIT license](license).

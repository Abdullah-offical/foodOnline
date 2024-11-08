1 Open folder
2 create virtual envormenet           --> python -m venv env  
2 activate envorment                 --> source env/bin/activate      deactivate
3 install Django.                  
4 create Django project 
5 add git ignore file to root directory and setup Github       https://www.toptal.com/developers/gitignore


6 push project to github repository 

7 setup django template   and create first template hello world

8 Run migrate command and then Create supper user

9 Homepage templete load
10 Static files config

11 Run collect static command to copy all the static file in root directory   --> python manage.py collect static

Collect static is used for prodection website not for local computer

12 configuration Postgres data base 
		Postgres data base is for large data base for use mostly compines but sqlite 3 is not good good so that's why I use.
		1 crete database 
		2 configure setting file 
		3 run this command   ->  pip install psycopg2    
		4 then migrate command run 
		5 create super user again for new database

13 Hide sensitive information and push code to getHub
		1 install python decuple 
		2 config the decouple

14 Create custom user model 
		1 create accounts app
		2 configure model and settings
		3 delete old database and create new database with same name
		4 run migrate commands
		5 Create supper user again new

15 password is editable change to readonly mode
16 set admin side other filter

17 set user profile

18 media file config

19 Automatic create user profile to create or register new user, create in userPfrofile model
		use Django signals.   --> learn Django signals for me I'm use this first time


20 setup user registration path

21 templetes inheritance

22 use Django form to registration implement, User or Customer save there data of user to database.

23 Django messages use


24 Resturent registration or vendor registration 

25 registration complete for vendor 

26 Display vendor admin profile 

27 Login logout and dashboard functionality 



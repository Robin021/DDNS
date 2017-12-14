# DDNS

Client_ip.py used for client side to get and post your ip to backend

other files for backend to process the post request.


### Server side

* install django 

`pip install django`

* install mariadb

`yum install mariadb*`

* create django project 

`django-admin.py startproject getip`

* create app in getip project

`django-admin.py startapp ipapp`

* start service 

`python manage.py runserver 0.0.0.0:8000`

### Client side

* install urllib3

`pip install urllib3`

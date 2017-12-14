# DDNS

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

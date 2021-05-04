
# [Django Blog](https://baz-django-blog.herokuapp.com)
    This blog was created with Python's Django Framework

## Functions
- Registration of new users
- Login of registered users
- Logged in users can create, edit and delete posts
- Only Admin and author of post can edit and delete post
- Logout 
- A comment section(only logged in users can comment)

## How to run on local Machine(Windows)
- git clone https://www.github.com/mrbazzan/zuri-blog.git
- cd "parent directory"
- python -m venv venv/
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
(follow the necessary instructions to create superuser)
- python manage.py runserver

## How to deploy on Heroku
- Sset up an account on heroku
- Install heroku CLI
- heroku create
- git push heroku main
- heroku config:set DJANGO_SECRET_KEY='enter about 50 random characters'
- heroku config:set DJANGO_DEBUG=False

If further help is needed to deploy on heroku, check this [link](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

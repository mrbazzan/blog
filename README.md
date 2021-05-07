
# [Django Blog](https://baz-django-blog.herokuapp.com)
    This blog was created with Python's Django Framework

## Functions
- Registration of new users
- Login of registered users
- Logged in users can create, edit and delete posts
- Only Admin and author of post can edit and delete post
- Logout
- Password reset
- A comment section(only logged in users can comment)
- Different tests can be carried out

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
- Set up an account on heroku
- Install heroku CLI
- heroku create
- git push heroku main
- heroku config:set DJANGO_SECRET_KEY='enter about 50 random characters'
- heroku config:set DJANGO_DEBUG=False

If further help is needed to deploy on heroku, check this [link](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)


## How to run Tests
The test file is located in blog/tests.py

To run everything;
```shell script
python manage.py test blog
```

To run test for a class;
- python manage.py blog.`class_name`

e.g
```shell script
python manage.py test blog.BlogHomePage
```

To run test for a function;
- python manage.py test blog.`class_name`.`function_name`

e.g
```shell script
python manage.py blog.BlogHomePage.test_index
```



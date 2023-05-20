# URL Shortener
#### **A simple Django based URL shortening web app.**

![ShortenThisLink](https://github.com/AhmetAI/django-url-shortener/assets/49074377/bb6ceeb1-896d-48e2-b656-5d330c8abb8e)

# Setup
Let's start with the Django installation first.

`````
$ pip install Django
`````
Now let's get the database working properly
`````
$ python manage.py makemigrations
`````
and
`````
$ python manage.py migrate
`````
Now you can launch the project and start using it.
`````
$ python manage.py runserver
`````
# Admin Page
**Let's go to the admin page to see all URL shorteners.**

Go to **127.0.0.1:8000/admin** to access the admin page
##### Admin information
username: admin
password: admin

#### If you can't login to the admin page or want to create your own admin account
`````
$ python manage.py createsuperuser
`````
And write the requested information.

**Great! Now we can use our project :)**

# Support
<a href="https://www.buymeacoffee.com/AhmetAI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

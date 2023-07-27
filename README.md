# Quiz project
The purpose of this project is to make a prototype of an online store with a flexible system for setting up products, reviews, registration and a bunch of small features.

<p float="center", align="justify">
  <img src="https://github.com/TBR-Group-software/django-web-store/blob/main/img/mob_1.gif" width="250" />

  <img src="https://github.com/TBR-Group-software/django-web-store/blob/main/img/mob_2.gif" width="250" />
     
  <img src="https://github.com/TBR-Group-software/django-web-store/blob/main/img/mob_3.gif" width="250" />
</p>
<p>
  <img src="https://github.com/TBR-Group-software/django-web-store/blob/main/img/desk_1.gif" width="750" />
</p>

## Features

- Responsive design for all types of devices
- Order product
- Reviews
- Contact us page
- Cart
- Register and login
- Docker container
- Unit tests

## Built with
- [Django](https://www.djangoproject.com/) - Back-end server side web framework
- [daphne](https://github.com/django/daphne/) - HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP, developed to power Django Channels.
- [Visual Studio Code](https://code.visualstudio.com/) - Code Editing.
- [pre-commit](https://pre-commit.com/) - Framework for managing and maintaining multi-language pre-commit hooks.
- [black](https://github.com/psf/black) - The uncompromising Python code formatter.
- [Flake8](https://github.com/pycqa/flake8) - Python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.
- [Bootstrap 5](https://getbootstrap.com/) - Bootstrap is a powerful, feature-packed frontend toolkit. Build anything-from prototype to production—in minutes.
- [Sass](https://sass-lang.com/) - Preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets.
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/) - Programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS
- [Docker](https://www.docker.com/) - Set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.
- [Nginx](https://www.nginx.com/) -  Web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
- [PostgreSQL](https://www.postgresql.org/) - Relational database management system emphasizing extensibility and SQL compliance.
- [RabbitMQ](https://www.rabbitmq.com/) - Message-broker software that originally implemented the Advanced Message Queuing Protocol.

## Build

**Step 1:**

Download or clone this repo by using the link below:

```
https://github.com/TBR-Group-software/django-web-store.git
```

**Step 2:**

Create in root folder .env file and write in this values:

```
PSQL_NAME = 'django_store'
PSQL_USER = 'postgres'
PSQL_PASSWORD = 'XXX'
PSQL_HOST = 'localhost'
PSQL_PORT = 5432

DJANGO_DEBUG = True/False
DJANGO_ALLOWED_HOSTS = 'XXX'
DJANGO_SECRET_KEY = 'XXX'
```

**Step 3:**
#### If you want launch with Docker:

```
docker-compose up --build
```

Quiz project is now available at http://127.0.0.1/

#### Launch without Docker:

**Step 1:**
Create and activate python env
```
python3 -m venv env
. env/bin/activate
```
**Step 2:**
Install requirements-dev.txt
```
pip3 install -r requirements-dev.txt
```
**Step 3:**
Run PostgreSQL

**Step 4:**
Run django migrations
```
python3 manage.py migrate
```
**Step 5:**
Run Django server
```
python3 manage.py runserver
```

Quiz project is now available at http://127.0.0.1:8000/


## License
This project is licensed under the GNU GPL v3 License - see the [LICENSE.md](https://github.com/TBR-Group-software/django-web-store/blob/main/LICENSE) file for details.

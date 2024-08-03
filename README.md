<h1 align="center">
AnimeHoshi
</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-%23339933.svg?style=for-the-badge&logo=python&logoColor=%23ffffff"/></a>
  <a href="#"><img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/></a>
</p>

<p align="center">
  <a href="#">
    <img src="https://thullydev.github.io/thullyDevStatics/images/animehoshi-logo.png" alt="Logo" width="200"/>
  </a>
</p>

## What is AnimeHoshi?

Welcome to **AnimeHoshi** - your go-to destination for anime! 🌟 Dive into the anime world with **[AnimeHoshi](https://www.animehoshi.com)**. Our site features a modern and sleek design, powered by **Django** and **PostgreSQL**, ensuring a fast and enjoyable experience.

<div align="center">

#### Necessary repos

| Repos                   | Links                                                                     | Frameworks | 
| ----------------------- | ------------------------------------------------------------------------- |------------|
| AnimeHoshi Site                 | [AnimeHoshi](https://github.com/thullyDev/AnimeHoshi.git)         | <p align="start"> <img src="https://img.shields.io/badge/python-%23339933.svg?style=for-the-badge&logo=python&logoColor=%23ffffff"/> <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/> </p> |
| LiveChat Api                 | [liveChat](https://github.com/thullyDev/liveChat)         | <p align="start"> <img src="https://img.shields.io/badge/fastapi-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge"/> <img src="https://img.shields.io/badge/redis-%23DC382D.svg?style=for-the-badge&logo=redis&logoColor=white" alt="Redis Badge"/> </p> |

</div>

## Images
**[AnimeHoshi Preview Images](https://imgur.com/a/OyePglf)** 

## Installation and Local Development 💻

#### Clone these repos 

##### AnimeHoshi site

```bash
git clone https://github.com/thullyDev/AnimeHoshi.git

cd AnimeHoshi

touch .env

pip install -r requirements.txt

python manage.py runserver
```


###### .env (change accordingly)

```
SQL_URL=*****
SQL_ENGINE=django.db.backends.postgresql_psycopg2
SQL_DB=DB_NAME 
SQL_USER=DB_USER
SQL_PASSWORD=DB_PASS
SQL_HOST=DB_HOST
SQL_PORT=DB_PORT
REDIS_URL=*****
REDIS_PORT=****
REDIS_HOST=*****
REDIS_PASSWORD=*****
SITE_EMAIL=*****
SITE_EMAIL_PASS=******
SITE_NAME=AnimeHoshi
SITE_KEY=0000
IMAGEKIT_ID=****
CAPTCHA_SITE_KEY=******
CAPTCHA_SECRET_KEY=*******
IMAGEKIT_PUBLIC_KEY=******
IMAGEKIT_PRIVATE_KEY=*******
IMAGEKIT_URL_ENDPOINT=https://ik.imagekit.io/*****
DEBUG=True
LIVECHAT_API_URL=127.0.0.1:8001/v1
```


##### liveChat api

```bash
git clone https://github.com/thullyDev/liveChat.git

cd liveChat

touch .env

pip install -r requirements.txt

python -m venv env

uvicorn app.main:app --reload --port 8001
```

###### .env (change accordingly)
```
REDIS_PORT=****
REDIS_HOST=****
REDIS_PASSWORD=****
```

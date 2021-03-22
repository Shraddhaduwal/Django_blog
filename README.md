# Django_blog

This is a blog made in django. It allows users to perform CRUD operations like adding posts, deleting post and updating posts. In additions, the users can update their information, profile pictures, can register and so on. Here, crispy-forms is used. In the development environment, `sqlite` is used as database and `postgresql` is used for production. The blog is hosted in heroku [here](new-django-blog-app.herokuapp.com)

## Start Django Project
`django-admin startproject <project_name>`

## Start Django app
`python manage.py startapp <app_name>`
## Start Dev Server
`python manage.py runserver`

## Make migrations
- `python manage.py makemigrations <app_name>`
- `python manage.py migrate`

## Shell
`python manage.py shell`

#### This project is completed in reference to django series by [Corey Schafer](https://github.com/CoreyMSchafer)
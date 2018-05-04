Simple Blog App
===============================

A Django 2.0 blog template.


Features:
---------
* Built with Python 3.6 and Django 2.0.5
* Navigation menu is modular; Separate menu files with dropdown capabilities
* Custom User module based Django auth
* Uses Django Flat Pages (for informational pages like About, Policies, etc.)
* Custom CSS design


Project structure
-----------------

Project will have the following directory structure:

```

    <project_slug>
    ├──  config
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── local.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├──  docs
    ├──  gulp
    ├──  requirements
    │   ├── base.txt
    │   ├── local.txt
    │   ├── production.txt
    │   └── test.txt
    ├── webapp
    │   ├── assets
    |   │   ├── css
    |   │   |   └── styles.css
    |   │   ├── img
    |   │   ├── js
    |   │   |   └── app.js
    │   ├── contrib
    |   │   ├── sites
    |   |   │   ├── migrations
    |   │   |   └── __init__.py
    │   |   └── __init__.py
    │   ├── static
    |   │   ├── css
    |   │   |   └── styles.css
    |   │   ├── img
    |   │   ├── js
    |   │   |   └── app.js
    │   ├── users
    │   ├── __init__.py
    │   └── templates
    ├── .env
    ├── .gitignore
    ├── .gulpfile.js
    ├── manage.py
    ├── package.json
    ├── Pipfile
    ├── Procfile
    ├── README.rst
    ├── web.config
    └── webpack.config.js
```

Docker Commands
---------------
To run commands on the docker container:

```
    docker-compose run web <command>
    
```

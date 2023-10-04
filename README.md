# [Star Admin Flask](https://appseed.us/product/star-admin/flask/)

Open-source **[Flask Dashboard](https://appseed.us/admin-dashboards/flask/)** generated by `AppSeed` on top of an iconic `Bootstrap 5` Design. For newcomers, **Star Admin** is a beautifully designed admin template featuring a fine selection of useful Bootstrap components and elements. The pre-built pages of the templates are intuitive and very well-designed.

- 👉 [Star Admin Flask](https://appseed.us/product/star-admin/flask/) - product page
- 👉 [Star Admin Flask](https://flask-star-admin.appseed-srv1.com/) - LIVE deployment

<br />

> 🚀 Built with [App Generator](https://appseed.us/generator/), Timestamp: `2022-06-08 12:24`

- ✅ `Up-to-date dependencies`
- ✅ Database: `sqlite`
- ✅ `DB Tools`: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- ✅ Session-Based authentication (via **flask_login**), Forms validation
- ✅ Deployment: [Render](#deploy-on-render)
  - 👉 See [VIDEO Presentation](https://youtu.be/mGaqgHvBnug)

<br />

![Star Admin - Full-Stack Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/168732392-51748c85-f2c2-45ad-978c-2b64e52292e2.png)

<br /> 

## Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/flask-star-admin.git
$ cd flask-star-admin
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br /> 

## How to use it

> Download the code 

```bash
$ git clone https://github.com/app-generator/flask-star-admin.git
$ cd flask-star-admin
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

## Deploy on Render

The product can be easily deployed on Render using [Python Deployer](https://github.com/app-generator/deploy-automation-render) (`open-source` tool).

<br />

> 👉 **Step 1**: Set UP a [Render](https://render.com/) account 

- Create account
- Create an [API_KEY](https://render.com/docs/api)
- Attach a `credit card` to the account
  - **Note**: Each Python service deployed on Render requires a monthly payment

<br />

> 👉 **Step 2**: Download [Python Deployer](https://github.com/app-generator/deploy-automation-render)

```bash
$ git clone https://github.com/app-generator/deploy-automation-render.git   
$ cd deploy-automation-render
$ pip install -r requirements.txt
```

<br />

> 👉 **Step 3**: Set up the `ENV` as suggested in the [deployer](https://github.com/app-generator/deploy-automation-render) help

```bash
$ export RENDER_API_KEY=<RENDER_API_KEY>   # mandatory
$ export RENDER_OWNER_ID=<RENDER_OWNER_ID> # needs to have a CC attached, used for Billing
```

<br />

> 👉 **Step 4**: Deploy the repo

```bash
$ python.exe deployer.py flask https://github.com/app-generator/flask-star-admin "run:app"
```

The new service should be visible on your Render Dashboard and soon be LIVE. 

<br />

### 👉 Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:5000/register`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:5000/login`

<br />

## ✨ Code-base structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes  
   |    |    |-- models.py                  # Defines models  
   |    |    |-- forms.py                   # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # App Dependencies
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

## PRO Version

> For more components, pages and priority on support, feel free to take a look at this amazing starter:

Soft UI Dashboard is a premium Bootstrap 5 Design now available for download in Flask. Made of hundred of elements, designed blocks, and fully coded pages, Soft UI Dashboard PRO is ready to help you create stunning websites and web apps.

- 👉 [Soft UI Dashboard PRO Flask](https://appseed.us/product/soft-ui-dashboard-pro/flask/) - Product Page
- 👉 [Soft UI Dashboard PRO Flask](https://flask-soft-ui-dashboard-pro.appseed-srv1.com/) - LIVE Demo 

<br >

![Soft UI Dashboard PRO - Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/170829870-8acde5af-849a-4878-b833-3be7e67cff2d.png)

<br />

---
[Star Admin Flask](https://appseed.us/product/star-admin/flask/) - Open-source starter generated by **[App Generator](https://appseed.us/generator/)**.

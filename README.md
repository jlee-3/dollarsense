# dollarsense
Expenses and budgeting app.
Control your spending, take control of your finances 💪
>"Changing habits starts with making the invisible visible"

Core functions
-   Help manage spending by recording expenses and categorising them
-   Set and track budgets, saving goals
-   Smart visualisations of spending categories, savings ratio and more

## Installation
**Django**

Go to the root `backend` folder, create a virtual environment and activate it
```
python3 -m venv env
source env/bin/activate
```
Install packages
```
pip install -r requirements.txt
```

**Postgres**

To more closely resemble a producion environment, we're swapping out the default sqlite database for a postgres one. Assuming Docker & docker-compose is already installed, within the `docker` directory create/run the postgres container
```
docker-compose up
```

With the virtual environment running, migrations can be run identially to the default django setup
```
python manage.py migrate
```

Verify the installation by booting the server. This repo uses [django-shortcuts](https://github.com/jgorset/django-shortcuts) for convenience
```
django r
```

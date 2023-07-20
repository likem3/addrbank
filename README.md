# Addrbank Dashboard
#django #postgree #blockchain #python3.9

Address Dashboard is a django dashboard to manage, handle and providing availability of the addresses that will be requested by another applications. Before let them requesting addresses from this dashboard, need to make sure that the address is available.

## Local Development
1. Clone this repository
    ```
    git clone git@github.com:likem3/addrbank.git
    ```
2. Go to your project directory and create virtualenv then activate
    ```
    cd addrbank
    python -m venv venv
    source venv/bin/activate
    ```
3. install all requirement package
    ```
    (venv) pip install -r requirements.txt
    ```
4. create ```.env``` file on root directory base on ```.env.example``` then adjust the variable value
5. create file settings inside ```main/settings/settings_{your .env ENVIRONMENT_SETTING value}.py```
6. set following variables to tour environtment setting file
   ```
    # set debug false on production environtment
    # fill this base on the environtment
    DEBUG = True

    ALLOWED_HOSTS = ["your_host_ip", "or_your_domain"]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "db_name",
            "USER": "db_user",
            "PASSWORD": "db_pass",
            "HOST": "db_host",
            "PORT": "db_port",
        }
    }
   ```
7. run application server
   ```
    (venv) python manage.py runserver
   ```

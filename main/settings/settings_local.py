# fill this base on the environtment
DEBUG = True

ALLOWED_HOSTS = ["10.20.30.130", "localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "addrbank_db",
        "USER": "postgres",
        "PASSWORD": "toor",
        "HOST": "127.17.0.4",
        "PORT": "5432",
    }
}

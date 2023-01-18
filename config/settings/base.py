from pathlib import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# To connect to an existing postgres database, first:
# pip install psycopg2
# then overwrite the settings above with:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testorm',
        'USER': 'testorm',
        'PASSWORD': 'testorm',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

INSTALLED_APPS = ("app.core",)

USE_TZ = True

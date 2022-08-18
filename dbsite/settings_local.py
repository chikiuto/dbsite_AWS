# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g^o+&6=iffu4z=6sk!!!z&lif@#_wa&c&v@_tyiz=j=h1k$e&%'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
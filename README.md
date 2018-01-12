# SETUP

### Installing with Homebrew (for OS X users)

You install pyenv with Homebrew:
```brew install --HEAD pyenv-virtualenv```

After installation, you'll still need to add

```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Using pyenv virtualenv with pyenv

```
pyenv virtualenv 3.6.3 test-pyenv
```
This will create a virtualenv based on Python 3.6.3 under $(pyenv root)/versions in a folder called test-pyenv.


You can activate your pyenv virtualenv now:
```
pyenv activate test-pyenv
```

### Install Django

Now that you're inside a virtualenv environment, you can install the package requirements:
```
pip install django
pip install djangorestframework
```

### Migrations

Run these commands:
```
python manage.py makemigrations orders
python manage.py migrate
```

### Install Swagger

With this command:
```
pip install django-rest-swagger
```

### Start the server

...and start up Django's development server.
```
python manage.py runserver
```

### Run tests

With the command:
```
python manage.py test
```

Everything works! Yeeeey! :)

## Suggestions for Improvement

- write more edge cases integration tests for API endpoint
- write unit tests for the model Order
- create a requirements.txt file that you install with a single command with all necessary packages
- convert the setup into Docker setup - this will enable the easier usage
- the additional field 'created' with the date was not necessary in models.py
- it would be great to have a field 'pizza_choice' in models.py, I think






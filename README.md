to setup, create a new folder and open it in vs code.

in your folder, run:
```python -m venv .```

then run:
```git clone https://github.com/LoL123413/sleep.git```

now you need to install the dependencies:
```cd sleep-app```
```pip install -r requirements.txt```

to setup the django database:

```
cd backend
python manage.py makemigrations
python manage.py migrate
```

(CAN SKIP THIS STEP AND ONLY THIS ONE)

to create a superuser (to access the admin panel during development):

```python manage.py createsuperuser```

(pls note that ur password won't be visible when u type it in ur terminal)

to use the admin account you just made, run:
```python manage.py runserver``` 
then go to:
```http://127.0.0.1:8000/admin```
and enter the username and password you just made

OR if you want to access the api, go to:
```http://127.0.0.1:8000/api```

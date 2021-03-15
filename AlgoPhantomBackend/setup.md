# Set Up


- Create a Branch- 
```
git checkout -b <branch_name>
```
- Create virtual environment- For Windows
```
python -m venv env
env\Scripts\activate
```
- Create virtual environment- For Linux
```
python3 -m venv env or virtualenv env
source env\bin\activate
```

- Install dependencies using-
```
pip install -r requirements.txt
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 -m pip install -r requirements.txt
```

- Headover to Project Directory- 
```
cd AlgoPhantomBackend
```
- Create ```local_settings.py``` , In this file add these fileds.
```
EMAIL_HOST_USER="Your email address"
EMAIL_HOST_PASSWORD="Your password"
```

- Make migrations using-
```
python manage.py makemigrations
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 manage.py makemigrations
```

- Migrate Database-
```
python manage.py migrate
```
- Create a superuser-
```
python manage.py createsuperuser
```
- Run server using-
```
python manage.py runserver
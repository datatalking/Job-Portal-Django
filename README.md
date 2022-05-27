# Job Portal
Django Job Portal.    


## Installation 

```
open terminal and type
https://github.com/Sany07/Job-Portal.git

or simply download using the url below
https://github.com/Sany07/Job-Portal.git
```

## Install requirements
```
pip install -r requirements.txt
# error try below per https://stackoverflow.com/questions/34304833/failed-building-wheel-for-psycopg2-macosx-using-virtualenv-and-pip
pip uninstall psycopg2
pip list --outdated
pip install --upgrade wheel
pip install --upgrade setuptools
pip install psycopg2
# error on psycopg2 try  install libpq-dev
nope
# error try brew install openssl
ok try adding openssl to path with export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
then try pip3 install psycopg2
yay!
Ok rerun pip install -r requirements.txt

```
## Database
```
Set the database from settings.py
```

## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
error ugettext_lazy error try
# this from django.utils.translation import gettext_lazy as _
python manage.py migrate
# pycharmprojects/Job-Portal-Django/job/settings ok so the postgres user error, # out post DATABASES is sqlite
that worked, rendered then error 'is_ajax' likely depreicated per SO
try
I did that and no much changed but it did change
# error on DEBUT = True changed to False, good
# error server 500.
# try comment out white noise nope
# try heroku run python manage.py migrate
# first try pip install heroku
# jobapp/views.py had an ajax error line 48.
    replaced with if request.headers.get('x-requested-with') == 'XMLHttpRequest': 

```

## Collects all static files in your apps
```
python manage.py collectstatic
```

## Run the server
```
python manage.py runserver
```

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-2020-05-08-17_03_46.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-jobs-2020-05-08-17_40_01.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-79-2020-05-08-16_59_55.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-job-create-2020-05-08-17_00_46.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-2020-05-08-17_01_07.png)

![Settings Window](https://raw.github.com/Sany07/Django-Job-Portal/master/screenshots/screencapture-127-0-0-1-8000-dashboard-employer-job-54-applicants-2020-05-08-17_01_34.png)

<div align="center">
    <h3>========Thank You=========</h3>
</div>


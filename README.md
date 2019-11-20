# DBX

------------------------------------------------------------------------------
-- django steps

-- Create an enviroment 
virtualenv.exe .env

-- Activate enviroment
. .\.env\Scripts\activate

-- Listing apps on an enviroment
pip list

-- Installing django
pip install django

python -m django --version

-- Creating a project
django-admin startproject mysite .

-- Testing a project
python manage.py runserver
http://127.0.0.1:8000/

-- Creatging an app
python manage.py startapp app_name

-- Migrating Database
python manage.py makemigrations
python manage.py migrate

-- Creating supperuser
python manage.py createsuperuser --username=admin --email=admin@site.local

-- Sorcing code
git init
git add --all
git commit -m 'Initial Commit'

-- Seting VSCode
File > Open Folder

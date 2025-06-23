## Elearning
Projet Django nommé **Elearning**, développé avec Python 3.12 et Django<br>
avec une base de données de MySQL (https://dev.mysql.com/downloads/installer/)
Nous allons donc procéder comme suit:
- Création du projet, de Django Administration et Installer des dépendances MySQL
- Configurer settings.py
- Configurer MySQL
- Ensuite developper notre programme avec l'ajout des fonctionnalité

## Description
Ce projet a pour but de développer une plateforme de formation en ligne.  
Il contient actuellement une application appelée `restaurant`.

## Création du projet
```bash
mkdir Elearning
cd Elearning
touch .gitignore
touch README.md
py -3.12 -m venv .venv
.venv\Scripts\activate
(.venv)python.exe -m pip install --upgrade pip
(.venv) pip3.12 install django
(.venv) pip3.12 install mysqlclient
(.venv) pip3.12 install pillow
(.venv) freeze > requirements.txt
(.venv)django-admin startproject mysite .
(.venv)django-admin startapp restaurant
(.venv)python manage.py runserver localhost:9000
```

###### Création de Django Administration dans notre Projet
```bash
(.venv)python manage.py migrate
(.venv)python manage.py createsuperuser
Username: ghostyrex
Email: ghostyrex@gmail.com
Password: Superuser2
Password(again): Superuser2
```

### Connecter le projet à Git
Voir le MODULE GIT

### Configurer settings.py #########################################################################
Allons dans settings.py pour ajouter l'application restaurant et configurer
 les paramètres de connexions à notre Base de données et supprimons db.sqlite3:
 ```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurant_db',
        'USER': 'ghostyrex',
        'PASSWORD': 'rootMysql@2210',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Faire ensuite migrer notre BD vers MySQL:
```bash
python manage.py makemigrations
python manage.py migrate
```


### Retour dans le code de notre application
Avant de commmencer faison ceci:
```bash
python manage.py migrate
```

*********************************************************************************************************************************
### Télecharger, installer et configurer MySQL
```bash
Télécharger MySql sur https://dev.mysql.com/downloads/
Chercher MySQL installer for Windows et télécharger
Mot de passe du serveur: rootMysql@2210
Ajout d`un nouvelle Utilisateur:
- User Name: ghostyrex
- Host: localhost
- Password: rootMysql@2210
- Confirm Password: rootMysql@2210
```
Configurons notre mot de passe root:
```bash
- User Name: root
- Password: rootMysql@2210
```
###### Après installation de MySQL
Il faut vérifier que MySQL est bien installer.
Ouvrons une INVITE DE COMMANDE et tapons:
```bash
mysql
reponse: ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)
```
###### Se connecter à MySQL
Ouvrons une INVITE DE COMMANDE et tapons:
```bash
mysql -u ghostyrex -p
Password: rootMysql@2210
...
mysql>create database restaurant_db;
mysql>show databases; (Dans la liste on verra restaurant_db)
mysql>use restaurant_db;
mysql>sow tables;
mysql>select * from restaurant_meal;
```
*********************************************************************************************************************************
### MODULE GIT: Création du dépôt Git
1. Aller sur ***https://github.com/dashboard*** et créer votre nouveau
repository nommé Elearning
2. Ouvrer l'invite de commande à la racine de votre projet Django
nommé Elearning
```bash
git init
git add .
git commit -m "Création de notre projet Django Elearning"
git branch -M main
git remote add origin https://github.com/ben2ci/Elearning.git
git push -u origin main
```
3. Après avoir travailler (modifier le projet) on enregistre les 
modifications sur Git Hub
```bash
git status
git add .
git commit -m "Modifications apportées au projet"
git branch -M main
git pull -u origin main
git push -u origin main
```

4. Cloner le projet depuis un autre ordinateur (<span style="color:green;">et utiliser le 3.en cas de modification</span>):
```bash
git clone https://github.com/votre-utilisateur/elearning.git
cd Elearning
```

*********************************************************************************************************************************
### ASTUCES
###### PourInsérons des données notre base de données MySQL

###### Avoir les informatons dans settings.py
Ouvrez une INVITE DE COMMANDE et si vous souhaitez avoir les informations
 sur les variable de votre settings.py voici comment procéder.
```bash
(.venv)python manage.py shell
>>> from django.conf import settings
>>> settings.BASE_DIR
```
###### PourInsérons des données notre base de données MySQL
Ouvrez une INVITE DE COMMANDE et saisissez les commandes suivantes:
```bash
python manage.py shell
>>>from restaurant.models import Meal
>>>Meal.objects.create(name="Meal One",description="This is our first meal", price="20")
>>>Meal.objects.all()
>>>meal = Meal.objects.create(name="Meal Two",description="This is our second meal", price="24")
>>>meal.save()
>>>Meal.objects.all()
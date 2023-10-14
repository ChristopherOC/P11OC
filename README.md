# P11OC

#GUDLIFT

Il s'agit d'un projet POC. Le but est de garder le application la plus légère possible.
Cette application permet à des clubs de sport de réserver des places pour certaines compétitions en respectans des restrictions.

## Recommandations :

Il vous faudra installer python 3.9 au minimum et un IDE de votre choix (PyCharm, VSCode...).
Ouvrez un terminal, clonez ce répertoire :
> git clone (https://github.com/ChristopherOC/P11OC.git)

Placez vous dans le dossier créé comme ceci :
> cd Python_Testing-master

Créez ensuite votre environnement virtuel :
> python -m venv env

Activez l'environnement virtuel comme ceci :
Sous Windows :
> env/Scripts/activate

Sous Linux :
> source env/bin/activate

Pour utiliser tout les packages nécessaires, utilisez la commande suivante :
> pip install -r requirements.txt


Ensuite il vous faudra installer Flask :
> pip install flask

Pour utiliser le serveur de développement Flask utilisez la commande suivante :
> $env:FLASK_APP = "server.py"

Ensuite, pour que celui-ci soit accessible il vous faudra utiliser la commande suivante :
> flask run



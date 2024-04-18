# 20200928

## RAPPORT :

Code :

En python, on crée la fonction get_weather qui appelle l'API openweathermap avec les variables longitude et latitude.
Ensuite, on crée la fonction main qui appelle cette fonction avec les variables et retourne la météo.


requirements.txt et .venv :

On crée le fichier requirements.txt avec les dépendences utilisées et l'environnement virtuel python.


Dockerfile :

On crée ensuite le dockerfile, en spécifiant la version de python, le pip install de environnement.txt et la commande à faire pour lancer.


Connexion à Docker :

docker login


Création de l'image docker :

docker build -t mordjane/image_tp1:tag .


Mettre à disposition l'image sur dockerhub :

docker push mordjane/image_tp1:tag  


Lancer l'image :

docker run --env LAT="31.2504" --env LONG="-99.2506" --env API_KEY="f56a6cc9d2d2762c923e663630dc6615" mordjane/image_tp1:tag

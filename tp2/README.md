#RAPPORT

On utilise le framework Flask en Python pour créer une API dans le fichier app.py.


requirements.txt et .venv :

On crée le fichier requirements.txt avec les dépendences utilisées et on utilise le même environnement virtuel python.


Dockerfile :

On crée ensuite le dockerfile, en spécifiant la version de python, le pip install de environnement.txt et la commande à faire pour lancer.


Connexion à Docker :

docker login


Création de l'image docker :

docker build -t mordjane/efrei-devops-tp2:1.0.0 .


Mettre à disposition l'image sur dockerhub :

docker push mordjane/efrei-devops-tp2:1.0.0


Lancer l'image :

docker run --network host --env API_KEY="f56a6cc9d2d2762c923e663630dc6615" --env LAT="0" --env LONG="0" mordjane/efrei-devops-tp2:1.0.0


Configurer un workflow Github Action :

On le configure le github action docker-image.yml pour qu'il build et push l'image à chaque nouveau commit.


Création des secrets :

On ajoute des secrets repository au projet qui permettent la connexion à Docker automatiquement et qui sont utilisés dans le Github Action.
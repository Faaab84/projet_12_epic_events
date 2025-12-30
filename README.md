# Architecture Back-End Sécurisée pour la Gestion CRM

## Description

Ce projet consiste en une application en ligne de commande sécurisée et modulaire.  
Il permet à une entreprise de gérer ses **collaborateurs**, **clients**, **contrats** et **événements**, tout en appliquant un système strict de permissions basé sur les rôles des utilisateurs (Management, Sales, Support).

**Technologies principales utilisées :**
- Base de données : **PostgreSQL**
- ORM : **SQLAlchemy**
- Authentification : **JWT** (JSON Web Tokens)
- Supervision des erreurs : **Sentry** (optionnel en production)

L'architecture suit les bonnes pratiques avec une séparation claire des responsabilités, une gestion centralisée des permissions et des composants réutilisables.


## Installation

1. Cloner le depot:

   ```bash
   git clone https://github.com/Faaab84/projet_12_epic_events.git

2. Créer l'environnement virtuel :

   >for Linux/macOS:
   >```bash
   >python3 -m venv venv
   >source venv/bin/activate
   >```

   >for Windows:
   >```shell
   >python -m venv venv
   >.\venv\Scripts\activate
   >```

3. Installer les dependances:

   ```bash
   pip install -r requirements.txt
   ```

4. Pour exécuter ce projet de manière sécurisée et garantir son bon fonctionnement dans différents environnements, il est indispensable de configurer les variables d’environnement suivantes :
Dans votre session de terminal, avant de lancer l’application :

   >For Linux/macOS:
   >```bash
   >export SENTRY_DSN="votre_dsn_ici"
   >export SECRET_KEY="votre_cle_secrete_ici"
   >export PEPPER="votre_pepper_ici"
   >
   >```

   >For Windows (Command Prompt):
   >```shell
   >$env:SENTRY_DSN="votre_dsn_ici"
   >$env:SECRET_KEY="votre_cle_secrete_ici"
   >$env:PEPPER="votre_pepper_ici"
   >```


## Configuration de la base de données 

Installation de postegreSQL driver avec :

```bach
pip install psycopg2-binary
```

Connexion a postegreSQL :
```bash
psql -U postgres
```

Créer un user (superuser): 
```sql
CREATE USER <user_name> WITH PASSWORD <motdepasse>;
```

### Créer la database

Créer, nommer votre base de données et désigner le nouvel utilisateur comme propriétaire :

```sql
CREATE DATABASE <database_name> OWNER <username>;
```

Accorde toutes les autorisations (cela se fait généralement automatiquement si l’utilisateur est le propriétaire, mais il est plus sûr de l’inclure).

```sql
GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <username>;
```

### Configuration de l'environnement.

Configurer la variable DATABASE_URL dans le fichier .env

>```bash
>DATABASE_URL=postgresql+psycopg2://<username>:<password>@localhost:5432/<database_name>

### Créer les tables

Placez vous dans le repertoire du projet 12 et ouvré une fenetre de commande :
```
psql -U "login" -d "database_name" -f SQL\seed.sql
```



## Usage and Features

Pour demarrer l'application : 
```bash
python main.py
```

Une fois lancé, vous verrez un menu proposant les options suivantes :

Se connecter :
Permet de s'identifier avec vos identifiants pour accéder aux fonctionnalités correspondant à votre département.
S'inscrire :
Inscription autonome.
Cette option permet au premier utilisateur de créer un compte dans le système. Elle est particulièrement utile lorsqu'aucun collaborateur n'existe encore dans la base de données, ou si tous les comptes ont été supprimés, afin de retrouver l'accès à l'application.
Se déconnecter :
Permet de quitter la session en cours de manière sécurisée.

### Après vous être connecté, l'application affichera un menu spécifique au département :

Management:
   - Create Collaborator
   - Modify Collaborator
   - Delete Collaborator
   - View customers
   - Read customer
   - View Contracts
   - Read contract
   - Create Contract
   - Modify contract
   - View events
   - Read event
   - Assign support collaborator to event
   - Log out

Support:
   - View customers
   - Read customer
   - View Contracts
   - Read contract
   - View events
   - Read event
   - Modify event
   - Display my events
   - Log out

Sales:
   - Create customer
   - View customers
   - Read customer
   - Modify customer
   - View Contracts
   - Read contract
   - Filter contracts by status
   - Filter contracts not fully paid
   - Modify contract
   - View events
   - Read event
   - Create event
   - Log out

## Connexion et mdp 


Le mot de passes des comptes est : Test123@4567

login commerciale : CBrunel ou CDelorme
login support : BRenard ou Kduran ou ALefebvre
login gestion : AMartinez

Vous pouvez naviguer dans le menu à l’aide du clavier. Chaque commande vous guidera pas à pas à travers les saisies nécessaires.

## Connexion et permissions

Ce projet utilise des JSON Web Tokens (JWT) pour gérer l’authentification et sécuriser l’accès aux fonctionnalités de l’interface en ligne de commande (CLI).

Lors de la connexion d’un utilisateur, un jeton JWT est généré et stocké localement dans le fichier .session.
Ce jeton contient les informations essentielles de l’utilisateur (identifiant, département, date d’expiration) et est signé à l’aide d’une clé secrète.
À chaque action, le jeton est décodé et vérifié afin de confirmer l’authentification de l’utilisateur.
L’accès aux fonctionnalités est contrôlé par une classe de permissions basée sur les rôles, qui vérifie à la fois l’état d’authentification de l’utilisateur et son département.
Toutes les permissions sont appliquées via une couche logique centralisée, garantissant un contrôle d’accès sécurisé, cohérent et maintenable.


## Error Monitoring avec Sentry

Ce projet intègre Sentry afin de surveiller les erreurs en production, d’améliorer la fiabilité de l’application et de faciliter le débogage.

## Securité

Les mesures de sécurité suivantes sont mises en œuvre dans le projet :

Les mots de passe sont hachés et salés à l’aide de bcrypt avant d’être stockés en base de données.
Les jetons JWT sont signés à l’aide d’une clé secrète stockée dans les variables d’environnement (SECRET_KEY) et intègrent une durée de validité (expiration).
Les jetons expirés ou absents entraînent le refus d’accès aux commandes protégées. Chaque action entraîne le décodage et la validation du jeton JWT.
Les données des utilisateurs sont anonymisées dans les journaux (logs) afin de préserver la confidentialité, grâce à une fonction de hachage combinée à un PEPPER stocké dans une variable d’environnement.
Les injections SQL sont empêchées par l’utilisation exclusive de l’ORM SQLAlchemy pour toutes les interactions avec la base de données.
Toutes les configurations sensibles sont gérées via des variables d’environnement — aucune donnée secrète n’est codée en dur dans le code source.
Lors des phases de test, des variables d’environnement fictives sont injectées et Sentry est désactivé afin de garantir l’absence de fuite de données vers l’extérieur.

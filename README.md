# Projet : Développer un programme logiciel en Python

## Objectif du projet : 

Ce projet est une application de gestion de tournoi d'échecs avec un système de round basé sur un système suisse. 

### Gestion des Rounds

Le Round 1 est basé uniquement sur l'aléatoire.
Les rounds suivant le premier round du tournoi prends en compte deux facteurs : 

-  Première condition : le nombre de points par joueur 
    Les joueurs ayant le même nombre de points se jouent entre eux

- Seconde condition : 
    Les matchs doublons sont évités. Si deux joueurs ayant le même nombre de points, mais se sont déjà joué dans les rounds précédent, alors l'un des deux joueurs jouera le joueur suivant dans la liste : 
        - En premier temps : un joueur ayant le même nombre de points et qui ne se sont pas joué avant.
        - En second temps : un joueur ayant moins de point que lui. 

## Fonctionnalités de l'application

- Fonctionne hors ligne
- Ajout de joueurs
- Création et configuration de tournois
- Sélection des participants
- Génération automatique des matchs par round :
  - Round 1 : appariement aléatoire
  - Rounds suivants : appariement par nombre de points + évitement des doublons
- Saisie des résultats de matchs
- Suivi du classement
- Sauvegarde et chargement des données via fichiers JSON

## 🧩 Structure du projet

```bash
.
├── controllers/
│   └── menus.py               # Contrôle des menus et de la logique
│   └── managers.py            # Contrôle les entrés de l'utilisateur
├── models/
│   └── models.py              # Définition des classes Player, Tournament, Round
├── views/
│   └── menu_views.py          # Affichage en ligne de commande (IHM CLI)
├── data/
│   ├── players/               # Données des joueurs
│   └── tournaments/           # Données des tournois
├── chess_tournament.py        # Point d’entrée principal du programme
└── README.md                  # Ce fichier
```
## Dépendance du projet 

Aucune dépendance. 

## Utilisation de l'application 

Il est nécessaire de lancer chess_tournament.py (Dans un terminal ou dans un IDE)

Ensuite, vous pourrez naviguer dans le menu en sélectionnant les options indiquées dans le terminal 

- Paramètre joueur : ouvrira un sous-menu regroupants des options telles que : 

    - Ajouter un joueur 
    - Liste des joueurs 
    - Retour au menu Principal

- Paramètre tournoi : ouvrira un sous-menu regroupant des options telles que : 

    - Créer un tournoi 
    - Liste des tournois
    - Commencer un tournoi (Ici, vous aurez la liste des tournois existants. Dans le cas où aucun tournoi n'existerait, un message vous indiquera qu'aucun tournoi n'est enregistré et vous renverra dans le menu du tournoi.)
    - Retour au menu Principal
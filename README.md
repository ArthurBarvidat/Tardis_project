# Tardis — Prédiction des Retards SNCF

Projet de data science pour analyser les données historiques de retards des trains SNCF, construire un modèle de prédiction par machine learning et présenter les résultats via un dashboard interactif Streamlit.

## Fonctionnalités

- **Nettoyage des données & EDA** — chargement, nettoyage et exploration du dataset SNCF
- **Modèle de prédiction** — modèle de régression pour estimer la durée des retards (en minutes) à partir des caractéristiques du trajet
- **Dashboard interactif** — application Streamlit pour explorer les données et obtenir des prédictions en temps réel

## Structure du projet

```
├── tardis_eda.ipynb        # Nettoyage, exploration et feature engineering
├── tardis_model.ipynb      # Entraînement et évaluation du modèle
├── tardis_dashboard.py     # Dashboard interactif Streamlit
├── project_dataset.csv     # Dataset brut
├── cleaned_dataset.csv     # Dataset traité (sortie du notebook EDA)
└── model.pkl               # Modèle entraîné (sauvegardé pour le dashboard)
```

## Installation

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

## Lancer le dashboard

```bash
streamlit run tardis_dashboard.py
```

## Fonctionnalités du dashboard

- Visualisation de la distribution des retards
- Statistiques résumées (retard moyen, nombre total de trajets, taux de ponctualité)
- Interface de prédiction : saisir les paramètres du trajet → obtenir le retard estimé
- Filtres interactifs par gare, ligne ou période

## Modèle

Le modèle prédit la durée du retard (valeur continue en minutes) à partir de :
- Gare de départ
- Gare d'arrivée
- Jour de la semaine
- Type de train

Métriques d'évaluation : RMSE, MAE, R²

## Stack technique

- Python
- pandas, numpy, matplotlib, seaborn
- scikit-learn
- Streamlit
- Formatage du code avec `ruff`

## Contexte du projet

Réalisé dans le cadre d'un projet data science Epitech. L'objectif était de nettoyer des données réelles, construire et justifier un modèle ML, puis le rendre accessible via un dashboard interactif.

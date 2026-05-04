# Tardis — SNCF Train Delay Prediction

A data science project for analyzing historical SNCF train delay data, building a predictive ML model, and presenting insights through an interactive Streamlit dashboard.

## What it does

- **Data cleaning & EDA** — loads, cleans, and explores the SNCF delay dataset
- **Prediction model** — regression model to estimate delay duration (in minutes) from journey characteristics
- **Interactive dashboard** — Streamlit app to explore data and get delay predictions in real time

## Project structure

```
├── tardis_eda.ipynb        # Data cleaning, exploration, and feature engineering
├── tardis_model.ipynb      # Model training and evaluation
├── tardis_dashboard.py     # Interactive Streamlit dashboard
├── project_dataset.csv     # Raw dataset
├── cleaned_dataset.csv     # Processed dataset (output of EDA notebook)
├── model.pkl               # Trained model (saved for dashboard integration)
└── readme.md               # This file
```

## Setup

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

## Run the dashboard

```bash
streamlit run tardis_dashboard.py
```

## Dashboard features

- Delay distribution visualization
- Summary statistics (average delay, total trips, punctuality rate)
- Prediction interface: input journey parameters → get estimated delay
- Interactive filters by station, route, or time period

## Model

The model predicts delay duration (continuous value in minutes) using features like:
- Departure station
- Arrival station
- Day of week
- Train type

Evaluation metrics: RMSE, MAE, R²

## Tech stack

- Python
- pandas, numpy, matplotlib, seaborn
- scikit-learn
- Streamlit
- Code formatted with `ruff`

## Project context

Built as part of an Epitech data science project. The goal was to clean real-world data, build and justify a ML model, and make it accessible through a clean interactive dashboard.

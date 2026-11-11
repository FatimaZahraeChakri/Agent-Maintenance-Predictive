# Agent de Maintenance Prédictive basé sur l'IA

Projet d'ingénierie en Intelligence Artificielle et Data Science visant à concevoir une solution complète de surveillance industrielle, de détection d'anomalies, de prédiction de pannes et de recommandation d'interventions assistée par un agent IA.

## Objectifs du projet

- Surveiller les paramètres physiques des machines industrielles (température, vitesse de rotation, couple, usure, etc.).
- Détecter les comportements anormaux (détection d'anomalies).
- Prédire les risques de panne par Machine Learning (et estimer la RUL lorsque les données le permettent).
- Interpréter les résultats prédictifs grâce à un agent IA (LangGraph + LLM) pour proposer des recommandations de maintenance.
- Simuler la création d'ordres de travail, exposer les services via une API (FastAPI) et une base PostgreSQL, et visualiser les indicateurs dans un dashboard.

## Architecture du projet

```text
Agent-Maintenance-Predictive/
├── data/
│   ├── raw/            # Jeux de données bruts (non modifiés)
│   └── processed/      # Jeux de données nettoyés et préparés
├── notebooks/          # Notebooks d'exploration et d'analyse visuelle
├── src/                # Code source modulaire
│   ├── ml/             # Prétraitement, modèles ML et détection d'anomalies
│   ├── agent/          # Agent intelligent (LangGraph), outils et prompts
│   ├── api/            # API backend (FastAPI)
│   ├── db/             # Modèles et connexion à PostgreSQL
│   └── dashboard/      # Interface de visualisation
├── models/             # Modèles entraînés sauvegardés
├── tests/              # Tests automatisés
└── docs/               # Documentation et diagrammes d'architecture
```

## Installation (environnement local Windows)

1. Créer l'environnement virtuel Python 3.12 :
   ```powershell
   python -m venv .venv
   ```
2. Installer les dépendances via le module `pip` de l'environnement virtuel :
   ```powershell
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   ```
3. Copier `.env.example` vers `.env` (lors des phases ultérieures) et renseigner vos variables locales.


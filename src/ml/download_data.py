"""Script de téléchargement reproductible du dataset AI4I 2020 depuis l'UCI."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo

AI4I_DATASET_ID = 601
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "ai4i2020.csv"


def fetch_ai4i_dataframe(dataset_id: int = AI4I_DATASET_ID) -> pd.DataFrame:
    """Télécharge le dataset AI4I 2020 officiel depuis le dépôt UCI.

    Retourne le DataFrame complet (identifiants, variables capteurs et cibles)
    afin de conserver une copie brute fidèle à la source officielle.
    """
    dataset = fetch_ucirepo(id=dataset_id)
    raw_df = dataset.data.original

    if raw_df is None or raw_df.empty:
        raise ValueError(
            f"Le dataset UCI id={dataset_id} n'a retourné aucune donnée exploitable."
        )

    return raw_df.copy()


def download_ai4i_dataset(
    output_path: Path = DEFAULT_OUTPUT_PATH,
    overwrite: bool = False,
) -> Path:
    """Sauvegarde le dataset brut au format CSV dans ``data/raw/``.

    Évite un nouveau téléchargement si le fichier local existe déjà,
    sauf si ``overwrite=True`` est demandé.
    """
    if output_path.exists() and not overwrite:
        print(f"Fichier déjà présent localement : {output_path}")
        return output_path

    df = fetch_ai4i_dataframe()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dataset téléchargé et enregistré dans : {output_path}")
    print(f"Dimensions : {df.shape[0]} lignes × {df.shape[1]} colonnes")
    return output_path


def parse_args() -> argparse.Namespace:
    """Analyse les arguments en ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Télécharge le dataset AI4I 2020 (UCI ID 601) vers data/raw/."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Chemin de sauvegarde du fichier CSV brut.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Force le re-téléchargement même si le fichier existe déjà.",
    )
    return parser.parse_args()


def main() -> None:
    """Point d'entrée principal du script."""
    args = parse_args()
    saved_path = download_ai4i_dataset(
        output_path=args.output,
        overwrite=args.overwrite,
    )
    df = pd.read_csv(saved_path)
    print("Colonnes :", list(df.columns))


if __name__ == "__main__":
    main()


from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "application_train.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "baseline_model.joblib"


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Missing dataset file: {DATA_PATH}\n"
            "Download the Kaggle dataset and place application_train.csv in data/."
        )

    print("Dataset found. Training code will go here in the next step.")
    print(f"Input:  {DATA_PATH}")
    print(f"Output: {MODEL_PATH}")


if __name__ == "__main__":
    main()

"""Automated tests for the Iris project (Tester role).

Run with:  pytest -v
"""
import sys
from pathlib import Path

import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from iris_demo import train_and_evaluate, save_model  # noqa: E402

TARGET_ACCURACY = 0.95  # Product Owner requirement


def test_clean_data_has_no_missing_or_duplicates():
    df = pd.read_csv(ROOT / "data" / "iris_clean.csv")
    assert df.isnull().sum().sum() == 0
    assert df.duplicated().sum() == 0
    assert set(df["species"]) == {"setosa", "versicolor", "virginica"}


def test_model_meets_accuracy_target():
    _, accuracy, *_ = train_and_evaluate()
    assert accuracy >= TARGET_ACCURACY, f"Accuracy {accuracy:.2f} is below {TARGET_ACCURACY}"


def test_saved_model_loads_and_predicts(tmp_path):
    model, *_ = train_and_evaluate()
    path = save_model(model, tmp_path / "model.joblib")
    loaded = joblib.load(path)
    # A typical setosa flower should be predicted as class 0 (setosa)
    assert loaded.predict([[5.1, 3.5, 1.4, 0.2]])[0] == 0

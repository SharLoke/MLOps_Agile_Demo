"""US1 + US2: download the Iris dataset and clean it (Data Engineer)."""
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

# US1: Download Iris dataset
iris = load_iris(as_frame=True)
df = iris.frame.copy()
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
df.to_csv(DATA / "iris_raw.csv", index=False)
print("Raw dataset saved:", df.shape)

# US2: Clean dataset
missing = int(df.isnull().sum().sum())
duplicates = int(df.duplicated().sum())
print("Missing values:", missing)
print("Duplicate rows:", duplicates)

clean = df.dropna().drop_duplicates().reset_index(drop=True)
clean.to_csv(DATA / "iris_clean.csv", index=False)
print("Clean dataset saved:", clean.shape)
print("Class counts:")
print(clean["species"].value_counts().to_string())

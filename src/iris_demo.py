"""US3, US4, US5: train, evaluate and save the Iris model (ML Engineer + Tester).

The training code is the code given in the lab handout.
It is wrapped in a function so the automated tests can call it.
"""
from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "iris_decision_tree.joblib"
REPORT_PATH = ROOT / "docs" / "Accuracy_Report.txt"


def train_and_evaluate():
    # ---- Code from the lab handout ----
    iris = load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    return model, accuracy, iris, X_train, y_test, prediction


def save_model(model, path=MODEL_PATH):
    path.parent.mkdir(exist_ok=True)
    joblib.dump(model, path)
    return path


def write_report(accuracy, iris, X_train, y_test, prediction, path=REPORT_PATH):
    path.parent.mkdir(exist_ok=True)
    report = classification_report(y_test, prediction, target_names=iris.target_names)
    cm = confusion_matrix(y_test, prediction)
    with open(path, "w") as f:
        f.write("Iris Decision Tree - Accuracy Report (Sprint 1)\n")
        f.write("=" * 48 + "\n")
        f.write(f"Train samples: {len(X_train)}\n")
        f.write(f"Test samples:  {len(y_test)}\n")
        f.write(f"Accuracy:      {accuracy:.4f}\n\n")
        f.write("Classification report:\n")
        f.write(report + "\n")
        f.write("Confusion matrix (rows = actual, cols = predicted):\n")
        f.write(", ".join(iris.target_names) + f"\n{cm}\n")
    return report, cm


if __name__ == "__main__":
    model, accuracy, iris, X_train, y_test, prediction = train_and_evaluate()
    print("Accuracy:", accuracy)

    report, cm = write_report(accuracy, iris, X_train, y_test, prediction)
    print("\nClassification report:\n", report)
    print("Confusion matrix:\n", cm)

    save_model(model)
    print("\nModel saved to models/iris_decision_tree.joblib")

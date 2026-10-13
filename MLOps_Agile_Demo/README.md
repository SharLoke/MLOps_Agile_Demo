# MLOps Agile Demo: Iris Flower Classification

![CI/CD](https://github.com/Vaibhavi1707/MLOps_Agile_Demo/actions/workflows/ci.yml/badge.svg)

Experiment 1: Agile and Scrum Demo. One Scrum Sprint that builds a Decision Tree model for the Iris dataset, with automated tests and a GitHub Actions CI/CD pipeline.

## Project structure

```
MLOps_Agile_Demo
├── .github/workflows/ci.yml   CI/CD pipeline (GitHub Actions)
├── data/                      iris_raw.csv, iris_clean.csv
├── src/                       data_prep.py, iris_demo.py
├── models/                    iris_decision_tree.joblib
├── tests/                     test_iris.py (automated tests)
├── docs/                      Product_Backlog.md, Sprint_1.md,
│                              Accuracy_Report.txt, Git_GitHub_Steps.md
├── requirements.txt
└── README.md
```

## How to run

```
pip install -r requirements.txt
python src/data_prep.py
python src/iris_demo.py
pytest -v
```

Expected output: `Accuracy: 1.0` and `3 passed`.

## Automated tests

`tests/test_iris.py` checks that:

1. The clean dataset has no missing values or duplicates.
2. The model meets the Product Owner target of at least 95% accuracy.
3. The saved model loads and predicts correctly.

## CI/CD

Every push to `main` runs `.github/workflows/ci.yml` on GitHub Actions. It installs dependencies, prepares data, runs the tests, trains the model and uploads the model and accuracy report as an artifact. If a test fails, nothing is delivered.

## Documents

- `docs/Product_Backlog.md`: user stories and priorities
- `docs/Sprint_1.md`: team, planning, Daily Scrum, review, retrospective, increment, result
- `docs/Accuracy_Report.txt`: accuracy, classification report and confusion matrix
- `docs/Git_GitHub_Steps.md`: Git commands and the CI/CD demo steps

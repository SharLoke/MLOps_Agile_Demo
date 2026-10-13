# Git, GitHub and CI/CD Steps

Run these in Terminal (or the VS Code terminal) on your Mac.

## 1. Go to the project

```
cd ~/Documents/MLOps_Agile_Demo
```

## 2. Create the Git repository

```
git init -b main
git status
```

If Git asks who you are, run these once:

```
git config --global user.name "Vaibhavi"
git config --global user.email "vlokegao@umd.edu"
```

## 3. Save the work in small commits (one per user story)

```
git add README.md requirements.txt .gitignore
git commit -m "Set up project structure and requirements"

git add src/data_prep.py data/
git commit -m "US1, US2: download and clean Iris dataset"

git add src/iris_demo.py models/
git commit -m "US3, US5: train Decision Tree model and save it"

git add tests/
git commit -m "US4: add automated tests for data, accuracy and saved model"

git add docs/
git commit -m "US6: add Scrum documents and accuracy report"

git add .github/
git commit -m "Add GitHub Actions CI/CD pipeline"
```

## 4. View history

```
git log --oneline
git show --stat HEAD
```

## 5. Run the tests locally

```
pip install -r requirements.txt
pytest -v
```

Expected: `3 passed`

## 6. Share the work on GitHub

1. Go to https://github.com/new
2. Repository name: `MLOps_Agile_Demo`. Keep it Public. Do not add a README, .gitignore or license.
3. Click Create repository.

Then run:

```
git remote add origin https://github.com/Vaibhavi1707/MLOps_Agile_Demo.git
git push -u origin main
```

Open https://github.com/Vaibhavi1707/MLOps_Agile_Demo/actions. The pipeline runs by itself and turns green.

## 7. CI/CD demonstration (code change, test, delivery)

### a. Make a bad change

In `src/iris_demo.py`, change

```
model = DecisionTreeClassifier(random_state=42)
```

to

```
model = DecisionTreeClassifier(max_depth=1, random_state=42)
```

Then:

```
git diff
git commit -am "Try a smaller tree with max_depth=1"
git push
```

On the Actions page the run fails (red X). The test `test_model_meets_accuracy_target` fails because accuracy drops below 95%. Nothing is delivered.

### b. Fix it

```
git revert HEAD --no-edit
git push
```

The new run passes (green tick). Open the run and scroll to Artifacts. Download `iris-model`. It contains the trained model and the accuracy report. This is the delivery step.

## What the pipeline does (`.github/workflows/ci.yml`)

1. Checks out the code on every push or pull request to `main`.
2. Sets up Python 3.11 and installs `requirements.txt`.
3. Prepares the data (`src/data_prep.py`).
4. Runs the automated tests (`pytest -v`).
5. Trains the model and writes the accuracy report (`src/iris_demo.py`).
6. Delivers the model and report as a downloadable artifact.

If any step fails, the later steps do not run, so a bad model is never delivered.

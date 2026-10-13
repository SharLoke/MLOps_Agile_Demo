# Sprint 1 Record

## Scrum Team (Step 2)

| Student   | Scrum Role    | Main responsibilities                                      |
|-----------|---------------|------------------------------------------------------------|
| Student 1 | Product Owner | Defines requirements, prioritizes and maintains the backlog, accepts work |
| Student 2 | Scrum Master  | Runs Sprint Planning and Daily Scrum, removes blockers     |
| Student 3 | ML Engineer   | Selects algorithm, trains, improves and saves the model    |
| Student 4 | Data Engineer | Collects, cleans and splits the dataset, prepares features |
| Student 5 | Tester        | Tests the model, verifies accuracy, reports bugs           |

Product Owner requirement: "Develop an Iris Flower Classification model with at least 95% accuracy."

## Sprint Planning (Step 4)

- Sprint duration: 1 week
- Sprint goal: Build the first working ML model.
- Scrum Master: "Today's Sprint Goal is to prepare the dataset and train the model."

### Sprint Backlog

| Task              | Story | Owner         | Estimate | Actual |
|-------------------|-------|---------------|----------|--------|
| Download Dataset  | US1   | Data Engineer | 20 min   | 10 min |
| Data Cleaning     | US2   | Data Engineer | 30 min   | 15 min |
| Train Model       | US3   | ML Engineer   | 30 min   | 15 min |
| Evaluate Accuracy | US4   | Tester        | 20 min   | 10 min |
| Total             |       |               | 100 min  | 50 min |

US5 (Save Model) and US6 (Documentation) were pulled into the Sprint because the team finished early.

## Daily Scrum (Step 5)

| Role          | Yesterday                  | Today                  | Blockers                 |
|---------------|----------------------------|------------------------|--------------------------|
| Product Owner | Requirements finalized.    | Review Sprint progress.| None.                    |
| Scrum Master  | Sprint planned.            | Conduct Daily Scrum.   | Git installation issue.  |
| ML Engineer   | Selected Decision Tree.    | Train model.           | Dataset unavailable.     |
| Data Engineer | Downloaded Iris dataset.   | Split dataset.         | Missing library.         |
| Tester        | Prepared test cases.       | Evaluate accuracy.     | None.                    |

### How the blockers were removed

- Git installation issue: Scrum Master installed Git and initialised the repository.
- Dataset unavailable: Data Engineer saved the dataset to `data/iris_raw.csv` and shared the path.
- Missing library: team installed the missing library and added it to `requirements.txt` before continuing.

## Development work (Step 6)

Data preparation (`python src/data_prep.py`):

- Raw dataset: 150 rows, 4 features, 3 classes.
- Missing values: 0.
- Duplicate rows: 1 (removed in `data/iris_clean.csv`, 149 rows).

Model training (`python src/iris_demo.py`):

- Algorithm: Decision Tree Classifier.
- Split: 80% train (120 rows), 20% test (30 rows), random_state = 42.
- Output: `Accuracy: 1.0`
- Every test sample was classified correctly (see `docs/Accuracy_Report.txt`).
- Model saved to `models/iris_decision_tree.joblib`.

Note: the handout expects about 0.96. This split gives 1.0. The test set has only 30 samples and Iris is an easy dataset, so 1.0 here does not mean the model is perfect on new data.

## Sprint Review (Step 7)

| Checklist item     | Status |
|--------------------|--------|
| Dataset downloaded | Done   |
| Data cleaned       | Done   |
| Model trained      | Done   |
| Accuracy generated | Done   |

- Was the Sprint Goal achieved? Yes. A working model was built and tested.
- Was the Product Owner target met? Yes. Accuracy is 100%, above the 95% target. The Product Owner accepted the work.
- What was delivered? Clean dataset, trained and saved model, source code, accuracy report and documentation.

## Sprint Retrospective (Step 8)

What went well?
- Good communication. Blockers were raised in the Daily Scrum and fixed the same day.
- Tasks were small, so progress was easy to track.
- The model passed the accuracy target on the first try.

What problems occurred?
- Python packages were missing at the start.
- Git was not installed on one machine.
- The dataset location was not shared at first, so the ML Engineer was blocked.

Improvements for Sprint 2
- Install required libraries before the Sprint starts (use `requirements.txt`).
- Agree on the project structure and data paths during Sprint Planning.
- Use cross-validation instead of one 30 sample test set, so the accuracy number is more reliable.
- Try other models (for example Random Forest) and compare.

## Sprint Increment (Step 9)

| Deliverable        | Location                               |
|--------------------|----------------------------------------|
| Working ML Model   | `models/iris_decision_tree.joblib`     |
| Python Source Code | `src/data_prep.py`, `src/iris_demo.py` |
| Automated Tests    | `tests/test_iris.py`                   |
| CI/CD Pipeline     | `.github/workflows/ci.yml`             |
| Documentation      | `README.md`, `docs/`                   |
| Accuracy Report    | `docs/Accuracy_Report.txt`             |

## Result

The Agile and Scrum methodology was successfully demonstrated by simulating an MLOps project. Scrum roles, Product Backlog, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, and the development of a simple Machine Learning model were successfully performed. The Decision Tree model reached an accuracy of 1.0 on the test set, which meets the Product Owner's target of 95%.

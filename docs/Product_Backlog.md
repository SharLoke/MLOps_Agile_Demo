# Product Backlog: Iris Flower Classification

Product Owner: Student 1
Product goal: Develop an Iris Flower Classification model with at least 95% accuracy.

| ID  | User Story                | Priority | Owner         | Status (end of Sprint 1) |
|-----|---------------------------|----------|---------------|--------------------------|
| US1 | Download Iris Dataset     | High     | Data Engineer | Done                     |
| US2 | Clean Dataset             | High     | Data Engineer | Done                     |
| US3 | Train Decision Tree Model | High     | ML Engineer   | Done                     |
| US4 | Evaluate Accuracy         | Medium   | Tester        | Done                     |
| US5 | Save Model                | Medium   | ML Engineer   | Done                     |
| US6 | Prepare Documentation     | Low      | Scrum Master  | Done                     |

## User stories in full

- US1: As a Data Engineer, I want the Iris dataset saved locally, so that the team works from one copy of the data.
- US2: As a Data Engineer, I want the dataset checked for missing values and duplicates, so that the model trains on clean data.
- US3: As an ML Engineer, I want to train a Decision Tree classifier, so that we have a first working model.
- US4: As a Tester, I want to measure accuracy on held-out data, so that we know if the 95% target is met.
- US5: As an ML Engineer, I want to save the trained model, so that it can be reused without retraining.
- US6: As the Product Owner, I want the work documented, so that others can understand and repeat it.

## Why High Priority tasks are selected first

1. Every other story depends on them. We cannot evaluate or save a model before we have data and a trained model.
2. They deliver the most value. A working model is the core of the product. Documentation adds value only after the model exists.
3. They carry the most risk. Problems with data or training are found early, when they are cheap to fix.
4. Scrum delivers a usable increment every Sprint. Doing High Priority work first makes sure the Sprint ends with something that works, even if low priority items slip.

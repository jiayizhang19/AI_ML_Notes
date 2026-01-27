### Evaluation
- Confusion Matrix 
- Accuracy
- Precision
- Recall / Sensitive (True possitive rate)
    - How many of the positive predictions made by the model are actually correct
- F1 Score
    - Harmonic mean of precision and recall
![Model Evaluation](../Images/Model_Evaluation.png)

- Receiver Operating Characteristic Curves 
(ROC Curves)
    - A graph used to check how well a binary classification model works
    - Area Under Curve (AUC)
Summarizes the ROC Curve into a single number
        - Close to top-left corner --> AUC is near 1.
        - A diagonal from (0,0) to (1,1) --> AUC is 0.5, random guessing
        - Below the diagonal --> AUC < 0.5

### Ethics
- Bias: Refers to systematic, repeatable error that leads to consistently unfair predictions for a particular group of people
- Fairness: ML systems that make equitable decisions for all individuals and groups.
- Major themes that make prediction difficult:
    - The distribution associated with data can shift over time, e.g. sales forecasting in seasons and pandamic.
    - The relationship between inputs and outputs can change over time.
    - Hidden factors that are not in the dataset.
    - Data available in the real world is fundamentally finite and limited.
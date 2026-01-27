### Regression
Activation Function: Linear or ReLU  
Loss Function: MSE (Mean Squared Error)
Types:
- Linear Regression: A way to predict future outcomes based on a linear relationship between independent variable(s) X and dependent variable y.
    - Intercept / Bias
    - Coefficients / Weights
- Lasso Regression
- Polynomial Regression

### Classification
Activation Function: 
- Sigmoid (Binary Classification) 
- Softmax (Multi-Classification)  
Loss Function: Cross-entropy
Types:
- Logistic Regression: Statistical model for binary classification.
    - Linear combination of features then apply Sigmoid to map it to [0,1]
- Decision Trees: Each node performs a Boolean test on an input feature.
    - Nodes: Root node, Internal / Decision node, Leaf / Terminal node
    - Terminology:
        - Entropy: Quantified uncertainty or impurity of the dataset.
            - The entropy of a pure set is 0.
            - The entropy of a impure/mixed set, say 50% yes and 50% no, is 1. --> maximum uncertainty
        - Information Gain: Quantified reudction in uncertainty following a split.
            - For continuous features: 
                - Sort all examples
                - Take midpoint values to check information gain
    - Algorithm (ID3):
        - Calculates entropy and information gain for each feature.
        - Select the feature with the highest information gain for splitting.
    - Avoid Overfitting:
        - Stop splitting: 
            - Below a certain threshold.
            - A maximum depth is reached.
        - Pruning
- Random Forests
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)

### Regularization
Add the features you want to penalize with a large magnitude to the cost function, so that the model will be forced to make them small.
- If the magnitude is too big, the model is prone to underfitting.
- If the magnitude is too small, the model is prone to overfitting.
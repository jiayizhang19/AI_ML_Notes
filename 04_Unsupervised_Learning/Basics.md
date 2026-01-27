### Definition:
Unsupervised learning is the process of building a desriptive model on unlabelled data. Model learns from **unlabeled data** to find **hidden structures and patterns**.

### Clustering
#### K-Means Clustering (Centroid-based Clustering)
- Definition: Clusters are represented by a central vector or point, known as a centroid, goal is to minimize distance to centroid
- Algorithm
    1. Randomly pick K number clusters.
    2. Randomly choose initial centroids for each cluster.
    3. Assign each observation to nearest cluster by computing Euclidean distance.
    4. Compute new centroids by averaging all points in each cluster.
    5. Reassign observations to the nearest cluster with the new centroids.
    6. Repeat last two steps until: Centroids stop moving significantly (converge) or you reach the maximum number of iterations.
- Optimisation:
    - WCSS (Within-Cluster Sum of Squares) / Distortion Cost Function
    - Elbow Method:
        - As it is unsupervised learning, so no "right" answer for the correct value for K.
        - Iterate over a range of K values from 1 to n. Plot a graph with k on the X-axis and WCSS on the y-axis.
        - As K increases, the WCSS typically decreases. However, there comes a point where adding more clusters results in a marginal decrease in WCSS. --> The best value for K
#### Anomaly Detection
- Definition: An anomaly is a data point or observation that derivates significantly from the "normal" or expected pattern of a dataset. (rare events that are different from the majority of the data)
- Techniques:
    - Statistical Approaches (Probability of Distributions)
        - Gaussian (Normal) Distribution
        - Normal data: High probability under the curve (near the center)
        - Anomalous data: Low probability under the curve (in the tails)
        - If the probability of a certain point is lower than a threshold, then this point is considered as an anomaly
    - Proximity-based 
    - Clustering-based
- Considerations:
    - Anomaly detection is likely to be useful in scenarios where there is a very small number of positive scenarios
    - Feature selection is very important because it replies on unlabelled data, unhelpful features make it harder to detect anomaly.
- Applications:
    - Fraud Detection
    - Cybersecurity

### Recommenders / Recommendation Systems
#### Content-based
- Foundations: Suggests items similar to what a user has liked before. (**Supervised Learning**)
- Advantages
    - No need for data on other users.
    - Able to recommend to users with unique tastes.
    - Able to recommend new & unpopular items.
- Disadvantages
    - Finding the appropriate features is hard.
    - Recommendations for new users, how to build a user profile.
    - Overspecialization, never recommends items outside user's content profile.
#### Collaborative filtering
- Foundations:
    - We only have labels (rating of user for item), we learn features. (**Unsupervised Learning**)
    - Operates by evaluating user interactions, and determining similarities between people (user-based) and things (item-based).
    - E.g. If User A and User B like the same movies, then User A may love other movies that User B enjoys
- Techniques:
    - Item-based collaborative filtering
    - User-based collaborative filtering
#### Hybrid
Combine content-based and collaborative filter methods. It often starts with content-based filtering to study new users and gradually integrate collaborative filtering.

### Advantages and Challenges
- Advantages:
    - Search for unknown similarities and differences in data and create corresponding groups.
    - Unlabelled data is much easier and faster to get.
    - Reduces the time spent on manual labelling process and reduces the chance of human error and bias.
- Challenges:
    - Goal is not always clearly defined.
    - Difficult to assess performance.
    - Work with high-dimensional data, difficult to interpret.
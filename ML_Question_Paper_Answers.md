## **Paper 1:**

### **Q1)**
#### a) Compare Machine Learning vs Artificial Intelligence. [5 marks]

**Answer:**
Machine Learning (ML) and Artificial Intelligence (AI) are closely related fields but have distinct differences. AI is a broader concept that involves creating machines capable of performing tasks that typically require human intelligence, such as problem-solving, understanding natural language, and recognizing patterns. AI encompasses various techniques, including ML, which is a subset of AI focused on developing algorithms that allow machines to learn from and make predictions based on data.

In contrast, ML specifically refers to the method of training algorithms on a dataset so they can make predictions or decisions without explicit programming. While AI may involve rule-based systems, ML relies on statistical models and data to improve performance over time. An example of AI is a rule-based chess-playing system, whereas ML would involve training a model on historical game data to predict the best moves.

#### b) Describe parametric and non-parametric machine learning models. [5 marks]

**Answer:**
**Parametric models** are types of machine learning models characterized by a fixed number of parameters that are learned from the training data. These models make assumptions about the underlying data distribution and are generally simpler and faster to train. Examples include Linear Regression, Logistic Regression, and Naive Bayes. They work well when the assumption about data distribution holds but may underperform when it does not.

**Non-parametric models**, on the other hand, do not assume a specific form for the underlying data distribution and can have a variable number of parameters that grow with the size of the training dataset. These models are more flexible and can adapt to more complex patterns in the data. Examples include Decision Trees, k-Nearest Neighbors (k-NN), and Support Vector Machines (SVMs). Non-parametric models are more powerful but require more data to perform effectively and may be computationally expensive.

#### c) Explain various Data formats that conform ML elements. [5 marks]

**Answer:**
Machine Learning models require data to be in specific formats for effective training and prediction. Some common data formats used in ML include:

1. **Structured Data**: Highly organized data that fits into traditional relational databases, such as tables with rows and columns. Examples include CSV files, SQL databases, and Excel spreadsheets.

2. **Unstructured Data**: Data that does not have a predefined format or structure, making it more challenging to analyze. Examples include text, images, audio, and video files.

3. **Semi-Structured Data**: Data that does not fit neatly into tables but contains tags or markers to separate semantic elements. Examples include XML and JSON files.

4. **Time-Series Data**: Data points indexed or listed in time order. Examples include stock prices, weather data, and sensor readings.

5. **Graph-Based Data**: Data represented as nodes and edges, used in graph-based models. Examples include social networks, recommendation systems, and biological networks.

Understanding these data formats is crucial because different ML algorithms are designed to work with different types of data, and pre-processing techniques vary depending on the format.

---

### **Q2)**
#### a) Explain supervised, unsupervised, and semi-supervised learning. [7 marks]

**Answer:**
**Supervised Learning** involves training a model on a labeled dataset, where each training example is paired with an output label. The model learns to map inputs to the correct output, allowing it to make predictions on unseen data. Examples of supervised learning algorithms include Linear Regression, Logistic Regression, Decision Trees, and Neural Networks. It is commonly used for tasks like classification and regression.

**Unsupervised Learning** involves training a model on data that does not have labeled outputs. The goal is to infer the natural structure present in the data. Common algorithms for unsupervised learning include K-Means Clustering, Hierarchical Clustering, and Principal Component Analysis (PCA). It is used for tasks like clustering, anomaly detection, and dimensionality reduction.

**Semi-Supervised Learning** is a combination of supervised and unsupervised learning. It uses a small amount of labeled data and a large amount of unlabeled data for training. This approach can improve learning accuracy when obtaining a fully labeled dataset is costly or time-consuming. An example application is web content classification.

#### b) Describe various statistical learning approaches. [8 marks]

**Answer:**
**Statistical learning approaches** involve using statistical methods and models to identify patterns and make inferences from data. Key approaches include:

1. **Regression Analysis**: Used for predicting continuous outcomes. Linear regression, polynomial regression, and logistic regression are common types of regression analysis.

2. **Classification Algorithms**: Used for predicting categorical outcomes. Examples include Naive Bayes, Decision Trees, and Support Vector Machines (SVM).

3. **Bayesian Inference**: A statistical approach that uses Bayes' theorem to update the probability of a hypothesis as more evidence or data becomes available. This method is particularly useful for models that incorporate prior knowledge.

4. **Maximum Likelihood Estimation (MLE)**: A method for estimating the parameters of a statistical model that makes the observed data most probable. It's widely used in machine learning to fit models to data.

5. **Dimensionality Reduction Techniques**: Techniques such as Principal Component Analysis (PCA) and Singular Value Decomposition (SVD) reduce the number of random variables under consideration to uncover the underlying structure of the data.

6. **Regularization Methods**: Techniques like Lasso and Ridge regression add a penalty to the model complexity to prevent overfitting, balancing model fit and complexity.

---

### **Q3)**
#### a) Consider a vector x = (23, 29, 52, 31, 45, 19, 18, 27). Apply feature scaling and find out min-max scaled values as well as z-score values. [8 marks]

**Answer:**
**Feature Scaling**: 
- **Min-Max Scaling**: Min-Max scaling, also known as normalization, transforms features to a fixed range, usually between 0 and 1. It preserves the relationships between the original data points.

**Formula**:   `X_scaled = (X - X_min) / (X_max - X_min)`

**Given**:  
`X = [23, 29, 52, 31, 45, 19, 18, 27]`, `X_min = 18`, `X_max = 52`.

For `x = 23`:  
`X_scaled = (23 - 18) / (52 - 18) = 5 / 34 ≈ 0.147`

Repeating for each value:  
**Scaled values**: `[0.147, 0.324, 1.0, 0.382, 0.794, 0.029, 0.0, 0.265]`


- **Z-score Normalization**: Z-score normalization standardizes the data to have a mean of 0 and a standard deviation of 1.

**Formula**:  `Z = (X - μ) / σ`

Where:  
- `X` is the data point.  
- `μ` is the mean of the data.  
- `σ` is the standard deviation.

**Given Vector**: `X = [23, 29, 52, 31, 45, 19, 18, 27]`

**Calculations**:  
1. **Mean (μ)**:  
   `μ = (23 + 29 + 52 + 31 + 45 + 19 + 18 + 27) / 8 = 30.5`

2. **Standard Deviation (σ)**:  
   `σ = sqrt((Σ(X - μ)²) / n) = 11.59`

For `x = 23`:  
`Z = (23 - 30.5) / 11.59 ≈ -0.647`

Repeating for each value:  
**Z-scores**: `[-0.647, -0.13, 1.85, 0.043, 1.249, -0.472, -1.038, -0.302]`

#### b) Explain the process of Principal Component Analysis (PCA) in brief. [7 marks]

**Answer:**
Principal Component Analysis (PCA) is a dimensionality reduction technique used to transform a large set of variables into a smaller one that still contains most of the information in the large set. The main steps in PCA are:

1. **Standardization**: Standardize the dataset to have a mean of 0 and a standard deviation of 1.

2. **Covariance Matrix Computation**: Compute the covariance matrix to understand the relationships between variables.

3. **Eigen Decomposition**: Calculate the eigenvalues and eigenvectors of the covariance matrix to identify principal components.

4. **Sort Eigenvalues and Eigenvectors**: Sort the eigenvalues in descending order and choose the top k eigenvectors that correspond to the k largest eigenvalues, where k is the number of dimensions to be retained.

5. **Transform the Original Data**: Use the selected eigenvectors to transform the original data onto a new subspace.

PCA reduces the dimensionality of the data by projecting it onto the directions (principal components) that maximize variance, thus retaining the most critical features of the dataset.

---

### **Q4)**
#### a) How to handle missing values in a dataset that will be used for training the ML model? [5 marks]

**Answer:**
Handling missing values is a crucial preprocessing step in machine learning. Several strategies exist to handle missing data:

1. **Deletion**:
   - **Listwise Deletion**: Remove rows with any missing values. This approach is simple but can lead to a significant loss of data.
   - **Pairwise Deletion**: Use all cases with available data for each analysis, preserving more data than listwise deletion.

2. **Imputation**:
   - **Mean/Median Imputation**: Replace missing values with the mean or median of the column. This method is easy to implement but can distort data variance.
   - **Mode Imputation**: Replace missing categorical data with the most frequent category.

3. **Advanced Imputation**:
   - **K-Nearest Neighbors (KNN)**: Use the values from k-nearest neighbors to impute missing data. This method considers the similarity of cases and works well for non-linear relationships.
   - **Multiple Imputation**: Use statistical models to generate multiple imputations, combining results to create a single dataset. This method accounts for uncertainty in the missing data.

4. **Model-Based Imputation**:
   - **Regression Imputation**: Use regression models to predict missing values based on other variables in the dataset.

5. **Using Algorithms that Support Missing Values**:
   - Some algorithms like Decision Trees, Random Forests, and XGBoost can handle missing values internally by splitting data based on available features.

#### b) Explain the types of wrapper methods for feature selection. [5 marks]

**Answer:**
Wrapper methods are feature selection techniques that evaluate the usefulness of a subset of features by actually training and evaluating a model using those features. Types of wrapper methods include:

1. **Forward Selection**: Starts with an empty set of features and adds features one by one based on the model performance improvement. At each step, the feature that provides the best performance improvement is added.

2. **Backward Elimination**: Starts with the complete set of features and removes the least significant feature at each step. The process is repeated until no further performance improvement is observed.

3. **Recursive Feature Elimination (RFE)**: A variant of backward elimination where the model is trained, and features are recursively removed. Features are ranked by importance, and the least important ones are removed first.

4. **Exhaustive Feature Selection**: Evaluates all possible combinations of features to find the best subset. This method is computationally expensive and impractical for large datasets with many features.

Wrapper methods are generally more computationally intensive than filter methods but often yield better feature subsets tailored to a specific model.

#### c) Explain Local Binary Pattern (LBP) feature extraction technique with a suitable example. [5 marks]

**Answer:**
**Local Binary Pattern (LBP)** is a simple yet powerful texture descriptor used in image processing for classification. The LBP operator works by labeling the pixels of an image with decimal numbers, which are derived from a binary pattern computed by comparing each pixel with its neighborhood.

The LBP value of a pixel is computed as follows:

1. For each pixel in a grayscale image, compare its value with those of its 8 neighbors.
2. Assign a binary value (1 or 0) based on whether the neighbor's value is greater than or equal to the center pixel's value.
3. Concatenate the binary values in a clockwise direction to form a binary number.
4. Convert the binary number to a decimal value. This value is the LBP of the pixel.

**Example**: Consider a 3x3 matrix with a center pixel value of 9 and its 8 neighbors:

\[
\begin{matrix}
10 & 12 & 18 \\
7 & 9 & 6 \\
9 & 2 & 4 \\
\end{matrix}
\]

For the center pixel value of 9:
- Pixels greater than or equal to 9: 10 (1), 12 (1), 18 (1), 7 (0), 6 (0), 9 (1), 2 (0), 4 (0)

The LBP binary pattern is `11100100`, which converts to a decimal value of 228.

LBP is widely used in facial recognition and image texture classification because of its computational simplicity and rotation-invariant properties.

---

## **Paper 2:**

### **Q1)**
#### a) Compare Machine Learning with traditional programming. Discuss types of Machine Learning with suitable examples. [5 marks]

**Answer:**
Traditional programming involves explicitly coding rules and logic for a task based on domain knowledge. The computer follows these rules to perform a task. This approach is static and inflexible, requiring manual updates when new scenarios arise.

Machine Learning, in contrast, involves training algorithms on data so they can learn patterns and make decisions. Instead of explicitly programming the rules, the algorithm learns from examples. This approach is dynamic and adaptable to new data.

**Types of Machine Learning**:
1. **Supervised Learning**: Learns from labeled data. Example: Email spam detection.
2. **Unsupervised Learning**: Learns from unlabeled data to find hidden patterns. Example: Customer segmentation using clustering.
3. **Reinforcement Learning**: Learns by interacting with the environment and receiving rewards or penalties. Example: AlphaGo, a game-playing AI.

Machine Learning is preferred for tasks where rules are not easily defined or are too complex for manual coding.

#### b) What are various Statistical Learning Approaches? [5 marks]

**Answer:**
(Refer to the answer provided for **Q2 b** in Paper 1 for a detailed explanation.)

#### c) Explain different data formats used in Machine Learning. [5 marks]

**Answer:**
(Refer to the answer provided for **Q1 c** in Paper 1 for a detailed explanation.)

---

### **Q2)**
#### a) What is Machine Learning? Explain applications of Machine Learning in data science. [5 marks]

**Answer:**
Machine Learning (ML) is a subset of Artificial Intelligence that enables computers to learn from data without explicit programming. It involves developing algorithms that allow systems to identify patterns, learn from experience, and make decisions.

**Applications in Data Science**:
1. **Predictive Analytics**: ML models predict future trends based on historical data, such as sales forecasting.
2. **Customer Segmentation**: Clustering algorithms group customers with similar behavior, aiding targeted marketing.
3. **Anomaly Detection**: Identifies unusual patterns or outliers in data, useful in fraud detection.
4. **Natural Language Processing (NLP)**: Processes and analyzes large volumes of textual data, such as sentiment analysis.
5. **Image and Speech Recognition**: Identifies objects in images or transcribes spoken words into text, used in facial recognition and virtual assistants.

ML's ability to handle large datasets and identify complex patterns makes it invaluable in data science for building data-driven solutions.

#### b) Explain Geometric Model and Probabilistic Model with suitable examples. [5 marks]

**Answer:**
**Geometric Models** use geometric shapes and decision boundaries to make predictions. They represent data in a multidimensional space and use geometric relationships to classify or predict outcomes.

- **Example**: The Support Vector Machine (SVM) algorithm is a geometric model that finds the hyperplane separating data points of different classes with the maximum margin.

**Probabilistic Models** rely on probability theory to model the uncertainty in predictions. They represent data in terms of probability distributions and make predictions based on likelihoods.

- **Example**: The Naive Bayes classifier is a probabilistic model that applies Bayes' theorem, assuming independence between features to classify data points based on the probability of their belonging to a particular class.

Geometric models work well with well-separated classes, while probabilistic models handle uncertainty and variance in the data effectively.

#### c) How does a machine learning model work? Explain various steps involved. [5 marks]

**Answer:**
A machine learning model works by learning patterns from data to make predictions or decisions. The steps involved in developing a machine learning model are:

1. **Data Collection**: Gathering relevant data from various sources.
2. **Data Preprocessing**: Cleaning the data by handling missing values, encoding categorical variables, and scaling features.
3. **Feature Engineering**: Selecting or creating relevant features that improve model performance.
4. **Model Selection**: Choosing a suitable algorithm based on the problem type (e.g., classification, regression).
5. **Training**: Feeding the preprocessed data into the model to learn patterns by adjusting parameters to minimize the error.
6. **Evaluation**: Assessing the model's performance using metrics such as accuracy, precision, recall, and F1-score on a validation dataset.
7. **Hyperparameter Tuning**: Fine-tuning model parameters to optimize performance.
8. **Deployment**: Deploying the model to a production environment where it can make predictions on new data.
9. **Monitoring and Maintenance**: Continuously monitoring the model's performance and retraining it as needed with new data.

These steps ensure that the model generalizes well to unseen data and performs effectively in real-world scenarios.

---

### **Q3)**
#### a) What is feature selection? Explain filtering technique. [5 marks]

**Answer:**
Feature selection is the process of selecting a subset of relevant features for use in model construction. It aims to improve model performance by reducing overfitting, enhancing generalization, and reducing computational cost.

**Filtering Technique**:
Filtering methods rank features based on statistical measures and select the most significant ones. These methods are model-independent and use criteria such as:

- **Correlation Coefficients**: Measures the linear relationship between features and the target variable.
- **Chi-Square Test**: Evaluates the independence between categorical features and the target.
- **Mutual Information**: Measures the mutual dependence between the features and the target.

Filtering techniques are fast and simple but may not always result in the best subset of features since they do not consider feature dependencies.

#### b) Explain kernel PCA in detail. [5 marks]

**Answer:**
**Kernel Principal Component Analysis (Kernel PCA)** is a nonlinear extension of PCA that uses kernel methods to map data into a higher-dimensional space, where linear separation is possible. It then performs PCA in this higher-dimensional space.

**Steps of Kernel PCA**:
1. **Mapping Data to Higher-Dimensional Space**: The kernel function maps input data to a higher-dimensional space to make complex patterns linearly separable.
2. **Computing the Kernel Matrix**: Calculate the kernel matrix (similarity matrix) representing the inner products of data points in the new space.
3. **Eigen Decomposition**: Perform eigen decomposition on the kernel matrix to obtain eigenvalues and eigenvectors.
4. **Selecting Principal Components**: Choose the top-k eigenvectors corresponding to the largest eigenvalues to represent the data in the reduced space.

**Applications**:
Kernel PCA is used in face recognition, image processing, and any domain where data is not linearly separable in its original space.

#### c) Calculate LBP code generated value for the central point in the neighborhood of 8 pixels (given in a 3x3 matrix). [5 marks]

**Answer:**
Given the 3x3 matrix:
\[
\begin{matrix}
10 & 12 & 18 \\
7 & 9 & 6 \\
9 & 2 & 4 \\
\end{matrix}
\]

**Steps to Calculate LBP Code**:
1. The central pixel is `9`.
2. Compare each neighboring pixel with the central pixel (9):
   - If the neighbor pixel >= 9, assign 1; otherwise, assign 0.
3. Binary Pattern: 
   - 10 >= 9 -> 1, 12 >= 9 -> 1, 18 >= 9 -> 1, 7 < 9 -> 0, 6 < 9 -> 0, 4 < 9 -> 0, 2 < 9 -> 0, 9 >= 9 -> 1
4. Binary Code: `11100001`
5. Convert binary to decimal: `1*2^7 + 1*2^6 + 1*2^5 + 0*2^4 + 0*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 225`

The LBP code generated value for the central pixel is **225**.

---

### **Q4)**
#### a) Explain Min-Max scaling with a suitable example. [5 marks]

**Answer:**
Min-Max scaling, also known as normalization, transforms features to a fixed range, usually between 0 and 1. It preserves the relationships between the original data points.

**Formula**:  `X_scaled = (X - X_min) / (X_max - X_min)`

**Example**:
Consider a feature vector: `X = [1, 2, 3, 4, 5]`

- Minimum value (`X_min`) = 1  
- Maximum value (`X_max`) = 5

**Scaled values**:`X_scaled = (X - 1) / (5 - 1) = (X - 1) / 4`

Resulting in: `[0, 0.25, 0.5, 0.75, 1]`.

Min-Max scaling is particularly useful in algorithms that use distance metrics like k-NN or neural networks.


#### b) What is Matrix factorization? Explain content-based filtering with an example. [5 marks]

**Answer:**
Matrix factorization is a technique used in recommender systems to decompose a user-item interaction matrix into the product of two lower-dimensional matrices, representing latent features of users and items.

**Content-Based Filtering**:
This technique recommends items based on the similarity between items and a user's past preferences. It uses item features (content) to create user profiles and recommends items that match the profile.

**Example**:
In a movie recommendation system, if a user likes action movies, content-based filtering will recommend other action movies by analyzing the movie's genre, director, and actors.

**Matrix Factorization Example**:
For a user-movie matrix, it decomposes the matrix into a user-feature matrix and a movie-feature matrix. The dot product of these matrices predicts the user's preference for unseen movies.

#### c) Given data for the attribute "AGE" {18, 22, 25, 42, 28, 43, 33, 35, 56, 28}, calculate Z-score normalization. [5 marks]

**Answer:**
**Z-score normalization** standardizes the data to have a mean of 0 and a standard deviation of 1.

**Formula**:   `Z = (X - μ) / σ`

Where:  
- `X` is the data point.  
- `μ` is the mean of the data.  
- `σ` is the standard deviation.

**Calculation**:  
1. **Mean (μ)**:  
   `(18 + 22 + 25 + 42 + 28 + 43 + 33 + 35 + 56 + 28) / 10 = 33`

2. **Standard Deviation (σ)**:  
   - **Variance (σ²)**: `[(18 - 33)² + (22 - 33)² + (25 - 33)² + (42 - 33)² + (28 - 33)² + (43 - 33)² + (33 - 33)² + (35 - 33)² + (56 - 33)² + (28 - 33)²] / 10`  
   - **Variance (σ²)**: `[(-15)² + (-11)² + (-8)² + (9)² + (-5)² + (10)² + (0)² + (2)² + (23)² + (-5)²] / 10`  
   - **Variance (σ²)**: `(225 + 121 + 64 + 81 + 25 + 100 + 0 + 4 + 529 + 25) / 10 = 1174 / 10 = 117.4`  
   - `σ = √117.4 ≈ 10.83`

**Z-scores**:  
- `Z(18) = (18 - 33) / 10.83 ≈ -1.39`  
- `Z(22) = (22 - 33) / 10.83 ≈ -1.02`  
- `Z(25) = (25 - 33) / 10.83 ≈ -0.74`  
- `Z(42) = (42 - 33) / 10.83 ≈ 0.83`  
- `Z(28) = (28 - 33) / 10.83 ≈ -0.46`  
- `Z(43) = (43 - 33) / 10.83 ≈ 0.92`  
- `Z(33) = (33 - 33) / 10.83 ≈ 0`  
- `Z(35) = (35 - 33) / 10.83 ≈ 0.18`  
- `Z(56) = (56 - 33) / 10.83 ≈ 2.12`  
- `Z(28) = (28 - 33) / 10.83 ≈ -0.46`


Normalized data using Z-scores helps in reducing skewness and allows features with different scales to contribute equally in model training.
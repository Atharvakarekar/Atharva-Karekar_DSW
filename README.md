# Atharva-Karekar_DSW

Given the comprehensive nature of your task, including Exploratory Data Analysis (EDA), model preparation, model selection, and ensuring adherence to coding standards, it would be best to provide you with an outline of how to approach each aspect of the project. Here's a structured plan:
Exploratory Data Analysis (EDA):

    Loading Data: Load the historic and prediction input datasets.
    Data Exploration:
        Explore basic statistics of the datasets (mean, median, min, max, etc.).
        Visualize distributions of numeric features (e.g., stars) and categorical features (e.g., category, color).
        Explore relationships between features and the target variable (success_indicator).
    Data Preprocessing Insights:
        Handle missing values, if any.
        Encode categorical variables (e.g., one-hot encoding).
        Scale numerical variables if required (e.g., using StandardScaler).
        Investigate potential outliers or anomalies.

Modeling:

    Prepare Training Pipeline:
        Create classes for data loading, preprocessing, model training, testing, and prediction.
        Implement methods for each class to perform respective tasks.
        Develop separate scripts for each model type (e.g., logistic regression, random forest, ANN).
    Model Implementation:
        Build at least two different models, such as logistic regression, random forest, and ANN.
        For the ANN model, define the architecture including the number of layers, neurons per layer, activation functions, and optimizer.
        Train each model using the training pipeline.
        Evaluate model performance using appropriate metrics (accuracy, precision, recall, F1-score, ROC-AUC, etc.).
        Save the trained models for future use.

Model Selection:

    Model Selection Pipeline:
        Create a script for model selection where different models are trained and evaluated.
        Implement hyperparameter tuning if necessary (e.g., using GridSearchCV or RandomizedSearchCV).
        Evaluate models using cross-validation to ensure robustness of results.
        Compare performance metrics across different models.
        Select the most suitable model based on evaluation metrics and reasoning.

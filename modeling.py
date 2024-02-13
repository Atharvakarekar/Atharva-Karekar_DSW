# -*- coding: utf-8 -*-
"""Modeling

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ycKBlepxz2ABW0gvWxOVF4-jvuIUCw0c

Atharva Karekar

## ***Modeling:***

Prepare Training Pipeline:
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class DataLoader:
    def __init__(self, historic_file_path, prediction_file_path):
        self.historic_file_path = historic_file_path
        self.prediction_file_path = prediction_file_path

    def load_data(self):
        try:
            historic_data = pd.read_csv(self.historic_file_path)
            prediction_data = pd.read_csv(self.prediction_file_path)
            return historic_data, prediction_data
        except FileNotFoundError as e:
            print("File not found error:", e)
            return None, None
        except Exception as e:
            print("An error occurred while loading data:", e)
            return None, None

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        if data is not None:
            X = data.drop(columns=['success_indicator'], errors='ignore')  # Drop 'success_indicator' if present
            X_encoded = pd.get_dummies(X)  # Perform one-hot encoding for categorical variables
            X_scaled = self.scaler.fit_transform(X_encoded)  # Scale numeric features
            return X_scaled
        else:
            return None

class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train_model(self, X_train, y_train):
        try:
            self.model.fit(X_train, y_train)
            print("Model training completed.")
        except Exception as e:
            print("An error occurred during model training:", e)

class ModelTester:
    def __init__(self, model):
        self.model = model

    def test_model(self, X_test, y_test):
        try:
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print("Model testing completed.")
            print("Accuracy:", accuracy)
        except Exception as e:
            print("An error occurred during model testing:", e)

class ModelPredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, X_pred):
        try:
            predictions = self.model.predict(X_pred)
            return predictions
        except Exception as e:
            print("An error occurred during model prediction:", e)


# Example usage:
historic_file_path = "historic.csv"
prediction_file_path = "prediction_input.csv"

data_loader = DataLoader(historic_file_path, prediction_file_path)
historic_data, prediction_data = data_loader.load_data()

if historic_data is not None and prediction_data is not None:
    preprocessor = DataPreprocessor()
    X_historic = preprocessor.preprocess_data(historic_data)
    X_prediction = preprocessor.preprocess_data(prediction_data)

    X_train, X_test, y_train, y_test = train_test_split(X_historic, historic_data['success_indicator'], test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    trainer = ModelTrainer(model)
    trainer.train_model(X_train, y_train)

    tester = ModelTester(model)
    tester.test_model(X_test, y_test)

    predictor = ModelPredictor(model)
    predictions = predictor.predict(X_prediction)
    print("Predictions:", predictions)
else:
    print("Data loading failed. Please check file paths.")

"""**Implement methods for each class to perform respective tasks.**"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class DataLoader:
    def __init__(self, historic_file_path, prediction_file_path):
        self.historic_file_path = historic_file_path
        self.prediction_file_path = prediction_file_path

    def load_data(self):
        try:
            historic_data = pd.read_csv(self.historic_file_path)
            prediction_data = pd.read_csv(self.prediction_file_path)
            return historic_data, prediction_data
        except FileNotFoundError as e:
            print("File not found error:", e)
            return None, None
        except Exception as e:
            print("An error occurred while loading data:", e)
            return None, None

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        if data is not None:
            X = data.drop(columns=['success_indicator'], errors='ignore')  # Drop 'success_indicator' if present
            X_encoded = pd.get_dummies(X)  # Perform one-hot encoding for categorical variables
            X_scaled = self.scaler.fit_transform(X_encoded)  # Scale numeric features
            return X_scaled
        else:
            return None

class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train_model(self, X_train, y_train):
        try:
            self.model.fit(X_train, y_train)
            print("Model training completed.")
        except Exception as e:
            print("An error occurred during model training:", e)

class ModelTester:
    def __init__(self, model):
        self.model = model

    def test_model(self, X_test, y_test):
        try:
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print("Model testing completed.")
            print("Accuracy:", accuracy)
        except Exception as e:
            print("An error occurred during model testing:", e)

class ModelPredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, X_pred):
        try:
            predictions = self.model.predict(X_pred)
            return predictions
        except Exception as e:
            print("An error occurred during model prediction:", e)


# Example usage:
historic_file_path = "historic.csv"
prediction_file_path = "prediction_input.csv"

# Instantiate DataLoader and load data
data_loader = DataLoader(historic_file_path, prediction_file_path)
historic_data, prediction_data = data_loader.load_data()

# Instantiate DataPreprocessor and preprocess data
preprocessor = DataPreprocessor()
X_historic = preprocessor.preprocess_data(historic_data)
X_prediction = preprocessor.preprocess_data(prediction_data)

# Split the historic data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_historic, historic_data['success_indicator'], test_size=0.2, random_state=42)

# Instantiate RandomForestClassifier model
model = RandomForestClassifier(random_state=42)

# Train the model
trainer = ModelTrainer(model)
trainer.train_model(X_train, y_train)

# Test the model
tester = ModelTester(model)
tester.test_model(X_test, y_test)

# Make predictions using the model
predictor = ModelPredictor(model)
predictions = predictor.predict(X_prediction)
print("Predictions:", predictions)

"""# **Develop separate scripts for each model type**

**Logistic Regression:**
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class LogisticRegressionModel:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Logistic Regression Model Accuracy:", accuracy)

    def predict(self, X_pred):
        return self.model.predict(X_pred)

# Example usage:
# Assuming X_train, y_train, X_test, y_test are available
logistic_model = LogisticRegressionModel()
logistic_model.train(X_train, y_train)
logistic_model.test(X_test, y_test)

"""**Random Forest model:**"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class RandomForestModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Random Forest Model Accuracy:", accuracy)

    def predict(self, X_pred):
        return self.model.predict(X_pred)

# Example usage:
# Assuming X_train, y_train, X_test, y_test are available
random_forest_model = RandomForestModel()
random_forest_model.train(X_train, y_train)
random_forest_model.test(X_test, y_test)

"""**Artificial Neural Network (ANN) model using TensorFlow/Keras:**"""

import tensorflow as tf
from sklearn.metrics import accuracy_score

class ANNModel:
    def __init__(self, input_shape):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)

    def test(self, X_test, y_test):
        loss, accuracy = self.model.evaluate(X_test, y_test, verbose=0)
        print("ANN Model Accuracy:", accuracy)

    def predict(self, X_pred):
        return (self.model.predict(X_pred) > 0.5).astype("int32").flatten()

"""# **Model Implementation:**"""

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Assuming X_train, X_test, y_train, y_test are available

# Logistic Regression Model
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_predictions = logistic_model.predict(X_test)
logistic_accuracy = accuracy_score(y_test, logistic_predictions)
print("Logistic Regression Model Accuracy:", logistic_accuracy)

# Random Forest Model
random_forest_model = RandomForestClassifier()
random_forest_model.fit(X_train, y_train)
random_forest_predictions = random_forest_model.predict(X_test)
random_forest_accuracy = accuracy_score(y_test, random_forest_predictions)
print("Random Forest Model Accuracy:", random_forest_accuracy)

"""We import the necessary classes from scikit-learn, including LogisticRegression, RandomForestClassifier, accuracy_score, and train_test_split.
    We instantiate Logistic Regression and Random Forest models.
    We train each model using the fit method with the training data.
    We make predictions on the test data using the predict method.
    We calculate the accuracy of each model using the accuracy_score function.
    Finally, we print the accuracy of each model.

**ANN model, define the architecture including the number of layers, neurons per layer, activation functions, and optimizer.**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# DataLoader class to load data from CSV files
class DataLoader:
    def __init__(self, historic_file_path, prediction_file_path):
        self.historic_file_path = historic_file_path
        self.prediction_file_path = prediction_file_path

    def load_data(self):
        try:
            historic_data = pd.read_csv(self.historic_file_path)
            prediction_data = pd.read_csv(self.prediction_file_path)
            return historic_data, prediction_data
        except FileNotFoundError as e:
            print("File not found error:", e)
            return None, None
        except Exception as e:
            print("An error occurred while loading data:", e)
            return None, None

# DataPreprocessor class to preprocess the loaded data
class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        if data is not None:
            X = data.drop(columns=['success_indicator'], errors='ignore')  # Drop 'success_indicator' if present
            X_encoded = pd.get_dummies(X)  # Perform one-hot encoding for categorical variables
            X_scaled = self.scaler.fit_transform(X_encoded)  # Scale numeric features
            return X_scaled
        else:
            return None

# ModelTrainer class to train the machine learning model
class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train_model(self, X_train, y_train):
        try:
            self.model.fit(X_train, y_train)
            print("Model training completed.")
        except Exception as e:
            print("An error occurred during model training:", e)

# ModelTester class to evaluate the performance of the trained model
class ModelTester:
    def __init__(self, model):
        self.model = model

    def test_model(self, X_test, y_test):
        try:
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print("Model testing completed.")
            print("Accuracy:", accuracy)
        except Exception as e:
            print("An error occurred during model testing:", e)

# ModelPredictor class to make predictions using the trained model
class ModelPredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, X_pred):
        try:
            predictions = self.model.predict(X_pred)
            return predictions
        except Exception as e:
            print("An error occurred during model prediction:", e)

# Example usage:
historic_file_path = "historic.csv"
prediction_file_path = "prediction_input.csv"

# Instantiate DataLoader and load data
data_loader = DataLoader(historic_file_path, prediction_file_path)
historic_data, prediction_data = data_loader.load_data()

# Instantiate DataPreprocessor and preprocess data
preprocessor = DataPreprocessor()
X_historic = preprocessor.preprocess_data(historic_data)
X_prediction = preprocessor.preprocess_data(prediction_data)

# Split the historic data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_historic, historic_data['success_indicator'], test_size=0.2, random_state=42)

# Instantiate RandomForestClassifier model
model = RandomForestClassifier(random_state=42)

# Train the model
trainer = ModelTrainer(model)
trainer.train_model(X_train, y_train)

# Test the model
tester = ModelTester(model)
tester.test_model(X_test, y_test)

# Make predictions using the model
predictor = ModelPredictor(model)
predictions = predictor.predict(X_prediction)
print("Predictions:", predictions)

import tensorflow as tf

class ANNModel:
    def __init__(self, input_shape):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def get_model_summary(self):
        return self.model.summary()

# Example usage:
# Assuming input_shape is available
input_shape = (10,)  # Example input shape, replace with your actual input shape
ann_model = ANNModel(input_shape=input_shape)
model_summary = ann_model.get_model_summary()
print(model_summary)

"""*   Evaluate model performance using appropriate metrics (accuracy, precision, recall, F1-score, ROC-AUC, etc.).
*   Save the trained models for future use.
"""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def teach_ai_to_recognize_digits():
    # Load the MNIST digits dataset
    digits = load_digits()
    X, y = digits.data, digits.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train an artificial neural network (MLP classifier) on the training data
    classifier = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
    classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = classifier.predict(X_test)

    # Evaluate the AI's performance
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

if __name__ == "__main__":
    teach_ai_to_recognize_digits()


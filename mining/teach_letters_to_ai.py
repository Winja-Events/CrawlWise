import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def generate_letter_data(digits_data):
    letter_data = digits_data.copy()

    # Let's create synthetic handwritten letters (A-Z) by modifying the MNIST digits
    for i in range(10, 36):  # 10 to 35 corresponds to A to Z (in ASCII)
        letter_digit = digits_data[i - 10].reshape(8, 8)  # Convert digit to 8x8 image
        letter_digit[0] = 0  # Set the top row to 0 to create space for the letter
        letter_data = np.append(letter_data, letter_digit.flatten().reshape(1, -1), axis=0)

    return letter_data

def teach_ai_to_recognize_letters():
    # Load the MNIST digits dataset
    digits = load_digits()
    X_digits, y_digits = digits.data, digits.target

    # Generate synthetic letter data
    X_letters = generate_letter_data(X_digits)
    y_letters = np.array(list(map(lambda x: chr(x + 55), range(10, 36))))  # Convert 10-35 to 'A'-'Z'

    # Combine digits and letters data
    X_combined = np.concatenate((X_digits, X_letters), axis=0)
    y_combined = np.concatenate((y_digits, y_letters), axis=0)

    # Split the combined dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_combined, y_combined, test_size=0.2, random_state=42)

    # Train an artificial neural network (MLP classifier) on the training data
    classifier = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
    classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = classifier.predict(X_test)

    # Evaluate the AI's performance
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)



import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

def perform_text_classification():
    # Load the 20 Newsgroups dataset
    newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
    X = newsgroups.data
    y = newsgroups.target

    # Convert the text data into numerical feature vectors using CountVectorizer
    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    # Split the dataset into training and testing sets
    split_point = int(0.8 * len(X))
    X_train, X_test = X_vectorized[:split_point], X_vectorized[split_point:]
    y_train, y_test = y[:split_point],


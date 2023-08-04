import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

def perform_kmeans_clustering():
    # Generate synthetic data for demonstration (you can use your own dataset)
    n_samples = 300
    centers = 4
    X, y = make_blobs(n_samples=n_samples, centers=centers, random_state=42)

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=centers, random_state=42)
    predicted_labels = kmeans.fit_predict(X)

    # Plot the data points and the cluster centers
    plt.scatter(X[:, 0], X[:, 1], c=predicted_labels, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X')
    plt.title('K-means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

if __name__ == "__main__":
    perform_kmeans_clustering()


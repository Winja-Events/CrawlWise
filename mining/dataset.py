import numpy as np

# Sample dataset for recognizing handwritten letters (A-Z)
# Each row represents an image of a letter, and each column represents the pixel intensity value
# Values range from 0 (white) to 255 (black)

# Create a random seed for reproducibility
np.random.seed(42)

# Sample dataset dimensions (26 classes, 100 samples per class, 64 pixels for an 8x8 image)
num_classes = 26
num_samples_per_class = 100
num_pixels = 64

# Generate random pixel intensity values for each letter
sample_dataset = np.random.randint(0, 256, size=(num_classes * num_samples_per_class, num_pixels))

# Example: Let's set the first 8x8 block to form the letter 'A'
sample_dataset[0, :8] = 0  # Set top row to 0
sample_dataset[1, :8] = 0  # Set second row to 0
sample_dataset[2, :8] = 0  # Set third row to 0
sample_dataset[3, :8] = 0  # Set fourth row to 0
sample_dataset[4, :8] = 0  # Set fifth row to 0
sample_dataset[5, :8] = 0  # Set sixth row to 0

# The rest of the dataset would contain random pixel intensity values

# Labels for each image (A:0, B:1, ..., Z:25)
labels = np.repeat(np.arange(num_classes), num_samples_per_class)

print("Sample Dataset:")
print(sample_dataset)
print("Labels:")
print(labels)


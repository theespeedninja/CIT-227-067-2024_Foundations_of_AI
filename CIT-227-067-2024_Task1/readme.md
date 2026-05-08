# Task 1 - MNIST Dataset Digit Recognition

## Overview
This Task demonstrates how to download and load the MNIST dataset, preprocess it, build a neural network model, and train it to recognize handwritten digits (0-9).

## What Was Done

### 1. **Dataset Loading**
   - Downloaded the MNIST dataset using TensorFlow/Keras
   - Loaded training and testing data (60,000 training images, 10,000 test images)
   - Images are 28x28 pixel grayscale handwritten digits

### 2. **Data Preprocessing**
   - Normalized pixel values from [0, 255] to [0, 1] by dividing by 255.0
   - Converted data type to float32 for better performance

### 3. **Data Visualization**
   - Displayed sample digits from the training dataset using matplotlib
   - Used grayscale colormap to visualize handwritten digits

### 4. **Neural Network Model Building**
   - **Flatten Layer**: Converts 28x28 images into 1D arrays (784 pixels)
   - **Hidden Dense Layer**: 128 units with ReLU activation for pattern learning
   - **Output Layer**: 10 units with softmax activation for digit classification (0-9)

### 5. **Model Compilation**
   - Optimizer: Adam (adaptive learning rate optimization)
   - Loss Function: Sparse Categorical Crossentropy (for multi-class classification)
   - Metrics: Accuracy

### 6. **Model Training**
   - Trained the model on the entire training dataset
   - 5 epochs (passes through the full training data)
   - Model learns to minimize loss and improve accuracy

### 7. **Model Evaluation**
   - Tested the trained model on unseen test data
   - Calculated test accuracy and test loss metrics
   - Demonstrated the model's generalization capability

### 8. **Predictions & Visualization**
   - Made predictions on test images using the trained model
   - Visualized predicted vs actual digits
   - Used argmax to get the highest probability digit prediction

## Key Technologies
- **TensorFlow/Keras**: Deep learning framework
- **NumPy**: Numerical operations
- **Matplotlib**: Data visualization

## Files
- `Task1.py`: Main Python script containing all implementation steps
- `readme.md`: This file

---

**Copyright © 2024 @Danny Ngatia - CIT-227-067/2024 #theespeedninja**
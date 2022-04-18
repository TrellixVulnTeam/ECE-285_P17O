"""
Logistic regression model
"""

import numpy as np
import math


class Logistic(object):
    def __init__(self, n_class: int, lr: float, epochs: int, weight_decay: float):
        """Initialize a new classifier.

        Parameters:
            lr: the learning rate
            epochs: the number of epochs to train for
        """
        self.w = None
        self.lr = lr
        self.epochs = epochs
        self.n_class = n_class
        self.threshold = 0.5  # To threshold the sigmoid
        self.weight_decay = weight_decay

    def sigmoid(self, z: np.ndarray) -> np.ndarray:
        """Sigmoid function.

        Parameters:
            z: the input

        Returns:
            the sigmoid of the input
        """
        # TODO: implement me
        sigmoid = 1/(1 + np.exp(z))
        return sigmoid

    def train(self, X_train: np.ndarray, y_train: np.ndarray, weights: np.ndarray) -> np.ndarray:
        """Train the classifier.

        Use the logistic regression update rule as introduced in lecture.
        Train a logistic regression classifier for each class i to predict the probability that y=i

        Parameters:
            X_train: a numpy array of shape (N, D) containing training data;
                N examples with D dimensions
            y_train: a numpy array of shape (N,) containing training labels
        """

        N, D = X_train.shape
        self.w = weights

        # TODO: implement me
        N, D = X_train.shape
        num_class = self.n_class
        y_train_2class = np.zeros((N,num_class))
        
        for i in range(N):
            y_train_2class[i,y_train[i]] = 1
        
        for i in range(self.epochs):
            y_hat = np.dot(X_train,weights.T)
            y_sigmoid = self.sigmoid(y_hat)
            loss = y_train_2class - y_sigmoid
            gradient = np.dot(loss.T,X_train)/N
            weights = weights - self.lr*gradient - self.weight_decay*weights
            
        self.w = weights
        return self.w

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        """Use the trained weights to predict labels for test data points.

        Parameters:
            X_test: a numpy array of shape (N, D) containing testing data;
                N examples with D dimensions

        Returns:
            predicted labels for the data in X_test; a 1-dimensional array of
                length N, where each element is an integer giving the predicted
                class.
        """
        # TODO: implement me
        y_prediction = np.dot(X_test,self.w.T)
        y_pred_sigmoid = self.sigmoid(y_prediction)
        y_test_pred = np.argmax(y_pred_sigmoid,axis = 1)
        
        return y_test_pred

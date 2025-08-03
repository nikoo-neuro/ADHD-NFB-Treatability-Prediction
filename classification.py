"""
classification.py

This script defines a classification pipeline using ensemble models (SVM, KNN, Decision Tree)
to predict whether a patient is treatable or not based on EEG features.
"""

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np


def create_ensemble_classifier():
    """
    Create a soft-voting ensemble classifier using SVM, KNN, and Decision Tree.

    Returns:
        model : sklearn VotingClassifier
    """
    clf1 = SVC(probability=True, kernel='rbf', C=1.0)
    clf2 = KNeighborsClassifier(n_neighbors=5)
    clf3 = DecisionTreeClassifier(max_depth=5)

    model = VotingClassifier(
        estimators=[('svm', clf1), ('knn', clf2), ('dt', clf3)],
        voting='soft'
    )
    return model


def evaluate_model(X, y, n_splits=5):
    """
    Evaluate the classifier using K-Fold cross-validation.

    Parameters:
        X : numpy array (samples × features)
        y : numpy array (samples,)
        n_splits : number of folds (default=5)

    Returns:
        accuracy_scores : list of accuracy per fold
    """
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    scores = []

    for train_idx, test_idx in kf.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        model = create_ensemble_classifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        scores.append(acc)

    return scores

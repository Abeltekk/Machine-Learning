# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:56:45 2021

"""

"""
Logistic Regression
"""
#Importing the libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


#Visualising training or test data
def plot_decision_boundary(classifier, X, y, title):
    plt.figure(figsize=(10,10))
    from matplotlib.colors import ListedColormap
    X_set, y_set = X, y
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ['red', 'green'][i], label = j)
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()

#Importing the dataset
dataset = pd.read_csv(r'D:\Jacobs\Lecture\PTM\Sources\2021\Classification\Datasets\Action_of_offer.csv')

# Delete gender and user ID
del dataset['Gender']
del dataset['User ID']

# Get X (independent variables) and y (dependent variable)
X = dataset.iloc[:, 0:2]
y = dataset.iloc[:, -1]


#Splitting into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)
X_train.describe()

#Feature standardizing of X
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fit the model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

#Predicting test set result
y_pred = classifier.predict(X_test)


# create model quality dataframe
quality_df = pd.DataFrame(columns = ['Accuracy', 'Precision', 'Recall', 'F1 score', 'ROC AUC'], index = ['Logistic Regression', 'KNN', 'Linear SVM', 'Kernel SVM', 'Naive Bayes', 'Decision Tree', 'Random Forest'])


# Evaluate the model
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, annot_kws={"size": 16})
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
quality_df.loc['Logistic Regression'] = [accuracy, precision, recall, f1, auc]


# Visualize the decision boundary, training set, and test set
plot_decision_boundary(classifier, X_train, y_train, 'Logistic Regression (Training Set)')
plot_decision_boundary(classifier, X_test, y_test, 'Logistic Regression (Test Set)')



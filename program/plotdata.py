import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import pylab as pl
import serial


from sklearn import neighbors, datasets
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.metrics import accuracy_score

dataset = pd.read_csv(r"datasetR.csv")
datatest = pd.read_csv(r"datatestR.csv")

X_train = dataset[['value']].values
Y_train = dataset["label"].values

X_test = datatest[['value']].values
Y_test = datatest["label"].values

k = 5
kNN = neighbors.KNeighborsClassifier(n_neighbors = k, weights='distance')
kNN.fit(X_train, Y_train)
prediksi_kNN = kNN.predict(X_test)
acc_kNN = accuracy_score(Y_test, prediksi_kNN)
print('Accuracy k-NN:', acc_kNN)

gnb = GaussianNB()
prediksi_NB = gnb.fit(X_train, Y_train).predict(X_test)
acc_NB = accuracy_score(Y_test, prediksi_NB)
print('Accuracy Naive Bayes:', acc_NB)

DT = tree.DecisionTreeClassifier()
DT = DT.fit(X_train, Y_train)
prediksi_DT = DT.predict(X_test)
acc_DT = accuracy_score(Y_test, prediksi_DT)
print('Accuracy DT:', acc_DT)

dSVM = svm.SVC(gamma='auto') # one versus one SVM
dSVM.fit(X_train, Y_train)
prediksi_SVM = dSVM.predict(X_test)
acc_SVM = accuracy_score(Y_test, prediksi_SVM)
print('Accuracy SVM:', acc_SVM)

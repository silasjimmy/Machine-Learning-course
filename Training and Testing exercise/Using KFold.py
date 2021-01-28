#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:13:14 2021

@author: silasjimmy
"""

from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
# features = iris.data
# labels = iris.target

from sklearn.model_selection import KFold

k = KFold(3, shuffle=True, random_state=0)

scores = []
clf = SVC(kernel="linear", C=1.)

for train, test in k.split(iris):
    print('Train: {} Test: {}'.format(train, test))
    
    x_train, x_test, y_train, y_test = iris.data[train], iris.data[test], iris.target[train], iris.target[test]
    clf.fit(x_train, y_train)
    scores.append(clf.score(x_test, y_test))

print(scores)
#!/usr/bin/python

""" this example borrows heavily from the example
    shown on the sklearn documentation:

    http://scikit-learn.org/stable/modules/cross_validation.html

"""

from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
features = iris.data
labels = iris.target

###############################################################
### YOUR CODE HERE
###############################################################

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.4, random_state=0)

###############################################################

clf = SVC(kernel="linear", C=1.)
clf.fit(features_train, labels_train)

print(clf.score(features_test, labels_test))


##############################################################
def submitAcc():
    return clf.score(features_test, labels_test)
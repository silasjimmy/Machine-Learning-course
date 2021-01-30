from sklearn.naive_bayes import GaussianNB

def classify(features_train, labels_train):
    clf = GaussianNB()
    return clf.fit(features_train, labels_train)
    

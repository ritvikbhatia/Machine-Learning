import sklearn
import sklearn.ensemble
import sklearn.linear_model
import sklearn.tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
d=pd.read_csv("C:\\Users\\Ritvik\\Documents\\train.csv")
d=d.drop(['Ticket'],axis=1)
d=d.drop(['Name'],axis=1)
d=d.drop(['PassengerId'],axis=1)
d=d.drop(['Cabin'],axis=1)
d=d.drop(['Fare'],axis=1)
d=d.join(pd.get_dummies(d['Sex']))
d=d.join(pd.get_dummies(d['Embarked']))
d=d.drop(['Sex'],axis=1)
d=d.drop(['Embarked'],axis=1)
d=d.dropna()
y=d['Survived']
d=d.drop(['Survived'],axis=1)
x=d
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)
clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))
print(clf.feature_importances_)
print(d.head())

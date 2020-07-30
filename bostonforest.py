import sklearn
import numpy as np
import sklearn.ensemble
import matplotlib.pyplot as plt
import sklearn.linear_model
import sklearn.datasets
boston=sklearn.datasets.load_boston()
x=boston.data
y=boston.target
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.4)
clf=sklearn.ensemble.RandomForestRegressor(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))
print(clf.feature_importances_)
print(boston)

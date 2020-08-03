import sklearn
import sklearn.ensemble
import sklearn.linear_model
import sklearn.tree
import pandas as pd
import numpy as np
import pylab as pl
import pickle
from PIL import Image
import scipy.ndimage
import scipy.misc as smp
import matplotlib.pyplot as plt
with open("C:\\Users\\Ritvik\\Documents\\datasets\\cifar-100-python\\train","rb") as fo:
    dict=pickle.load(fo,encoding='latin-1')
x=np.array(dict['data'])
with open("C:\\Users\\Ritvik\\Documents\\datasets\\cifar-100-python/meta",'rb') as fo:
    meta=pickle.load(fo)
y=dict['coarse_labels']
for i in range(len(x)):
    img=np.transpose(np.reshape(x[i],(3,32,32)))
    img=smp.toimage(img)
    img=img.convert('L')
    img=np.array(img)
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)
clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))

import tensorflow as tf
import sklearn.naive_bayes
import sklearn.linear_model
import nltk.stem.porter
import nltk.corpus
import sklearn
import numpy as np
import os
import collections
import pandas as pd
import sklearn.feature_extraction.text
import sklearn.feature_extraction
import sklearn.model_selection
d=pd.read_csv("C:\\Users\\Ritvik\\Documents\\datasets\\New folder\\train.csv")
d=d.loc[:100]
k=[]
for i in range(2022):
    k.append(str(i))
x=d['comment_text']
x=list(x)
porter_stemmer=nltk.stem.porter.PorterStemmer()
stop_words=set(nltk.corpus.stopwords.words('english'))
for sentence in x:
    sentence=sentence.lower()
    words=sentence.split(" ")
    final_sentence=[]
    for word in words:
        if word not in stop_words:
            word_stem=porter_stemmer.stem(word)
            final_sentence.append(word_stem)
    new_sentence=" ".join(final_sentence)
sum=0
vect=sklearn.feature_extraction.text.CountVectorizer()
tf_train=vect.fit_transform(x)
print(tf_train.shape)
d=pd.DataFrame(tf_train,columns=k)
feature_columns=[]

for key in d.keys():
    feature_columns.append(tf.contrib.layers.feature_column.real_valued_column(key))
estimator=tf.estimator.DNNClassifier(feature_columns=feature_columns,hidden_units=[10],n_classes=3)
def my_input_fn():
    df=pd.read_csv("C:\\Users\\Ritvik\\Documents\\datasets\\iris.csv")
    df=df.drop(['Id'],axis=1)
    #y=df['Species']
    y=pd.Categorical(df['Species']).codes
    y=np.array(y,dtype=np.int32)
    df.drop(["Species"],axis=1)
    x=df

    return x,y
x,y=my_input_fn()
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)
def train():
    return dict(x_train),y_train
def test():
    return dict(x_test),y_test
estimator.train(input_fn=train,steps=200)
r=estimator.evaluate(input_fn=test,steps=1)
print(r)

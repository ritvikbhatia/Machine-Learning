import sklearn.model_selection
import sklearn.naive_bayes
import sklearn
import numpy as np
import os
import collections
#root_dir="C:\\Users\\Ritvik\\Documents\\datasets\\lingspam_public\\lemm_stop\\part1"
def makeDictionary(root_dir):
    all_words=[]
    emails=[os.path.join(root_dir,f) for f in os.listdir(root_dir)]
    for mail in emails:
        with open(mail) as m:
            for line in m:
                words=line.split()
                all_words+=words
    dictionary=collections.Counter(all_words)
    all_keys=list(dictionary.keys())
    times_removed=0
    for item in all_keys:
        if item.isalpha()==False:
            del dictionary[item]
            times_removed+=1
        elif len(item)==1:
            del dictionary[item]
            times_removed+=1
    dictionary=dictionary.most_common(3000)
    return dictionary

d=makeDictionary("C:\\Users\\Ritvik\\Documents\\datasets\\lingspam_public\\lemm_stop\\part1")
def extract_features(mail_dir):
    file_paths=[os.path.join(mail_dir,f) for f in os.listdir(mail_dir)]
    features_matrix=np.zeros((len(file_paths),3000))
    train_labels=np.zeros((len(file_paths)))
    count=0
    docID=0
    for file in file_paths:
        with open(file) as f1:
            for i,line in enumerate(f1):
                if i==2:
                    words=line.split()
                    for word in words:
                        wordID=0
                        for i,t in enumerate(d):
                            if(t[0])==word:
                                wordID=i
                                features_matrix[docID,wordID]=words.count(word)
    train_labels[docID]=0
    filepathTokens=file.split('/')
    lastToken=filepathTokens[len(filepathTokens)-1]
    if lastToken.startswith("spmsg"):
        train_labels[docID]=1
        count=count+1
    docID=docID+1
    return features_matrix,train_labels
x,y=extract_features("C:\\Users\\Ritvik\\Documents\\datasets\\lingspam_public\\lemm_stop\\part1")
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)
model=sklearn.naive_bayes.GaussianNB()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))

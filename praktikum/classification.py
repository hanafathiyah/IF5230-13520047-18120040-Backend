# -*- coding: utf-8 -*-
"""Classification - 13520047 - 18120040.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13TGDBYUiFY8df_-YuiArLn_Epzu31EYa

# Praktikum 2 IF5230 Aplikasi Inteligensi Buatan untuk Enterprise
13520047 - Hana Fathiyah
18120040 - Iftitah Naura Azzahra

Data yang digunakan untuk praktikum bagian klasifikasi ini adalah data [telecom_churn.csv]
https://www.kaggle.com/datasets/barun2104/telecom-churn?resource=download

Pada praktikum ini, digunakan 3 modeling, yaitu Logistic Regression, KNN, dan SVM.
Alasan penggunaannya karena data pada kolom Churn merupakan binary classification, sehingga ketiga model tersebut cocok digunakan.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
# %matplotlib inline
import matplotlib.pyplot as plt

"""## Load Data"""

!gdown 1gf3SD3VI1fQyZQjaIQHwdWiuQYRIOGkX
df = pd.read_csv("telecom_churn.csv")
df.head()

"""## Data Pre-processing and Selection"""

df = df[['Churn', 'AccountWeeks', 'ContractRenewal', 'DataPlan', 'DataUsage', 'CustServCalls', 'DayMins', 'DayCalls', 'MonthlyCharge', 'OverageFee', 'RoamMins']]
df['Churn'] = df['Churn'].astype('int')
df.head()

"""## Define X and Y"""

X = np.asarray(df[['AccountWeeks', 'ContractRenewal', 'DataPlan', 'DataUsage', 'CustServCalls', 'DayMins', 'DayCalls', 'MonthlyCharge', 'OverageFee', 'RoamMins']])
X[0:5]

y = np.asarray(df['Churn'])
y[0:5]

"""## Train or Test Dataset"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
print('Train set:', X_train.shape,  y_train.shape)
print('Test set:', X_test.shape,  y_test.shape)

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
X_train[0:5]

"""## Modeling

### Logistic Regression with Scikit-learn
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train,y_train)
LR

# predict using test data

yhat_LR = LR.predict(X_test)
yhat_LR

# predict probability using test data

yhat_prob_LR = LR.predict_proba(X_test)
yhat_prob_LR

"""Evaluation"""

# jaccard index
from sklearn.metrics import jaccard_score
jaccard_score(y_test, yhat_LR)

# confusion matrix

from sklearn.metrics import classification_report, confusion_matrix
import itertools
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
print(confusion_matrix(y_test, yhat_LR, labels=[1,0]))

from sklearn.metrics import confusion_matrix
cnf_matrix = confusion_matrix(y_test, yhat_LR, labels=[1,0])
np.set_printoptions(precision=2)

plt.figure()
plot_confusion_matrix(cnf_matrix,classes=['churn=1','churn=0'],normalize=False,title='Confusion matrix')

print(classification_report(y_test, yhat_LR))

"""Log loss"""

from sklearn.metrics import log_loss
log_loss(y_test, yhat_prob_LR)

"""### SVM"""

from sklearn import svm
from sklearn.metrics import confusion_matrix
SVM = svm.SVC(kernel='rbf',gamma='scale',probability=True).fit(X_train, y_train)
SVM

# predict using test data

yhat_SVM = SVM.predict(X_test)
yhat_SVM

# predict probability using test data

yhat_prob_SVM = SVM.predict_proba(X_test)
yhat_prob_SVM

"""Evaluation"""

# jaccard index
from sklearn.metrics import jaccard_score
jaccard_score(y_test, yhat_SVM)

# confusion matrix

from sklearn.metrics import classification_report, confusion_matrix
import itertools
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
print(confusion_matrix(y_test, yhat_SVM, labels=[1,0]))

from sklearn.metrics import confusion_matrix
cnf_matrix = confusion_matrix(y_test, yhat_SVM, labels=[1,0])
np.set_printoptions(precision=2)

plt.figure()
plot_confusion_matrix(cnf_matrix,classes=['churn=1','churn=0'],normalize=False,title='Confusion matrix')

print(classification_report(y_test, yhat_SVM))

"""Log Loss"""

from sklearn.metrics import log_loss
log_loss(y_test, yhat_prob_SVM)

"""### KNN"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
KNN = KNeighborsClassifier(n_neighbors = 4).fit(X_train, y_train)
KNN

# predict using test data

yhat_KNN = KNN.predict(X_test)
yhat_KNN

# predict probability using test data

yhat_prob_KNN = KNN.predict_proba(X_test)
yhat_prob_KNN

"""Evaluation"""

# jaccard index
from sklearn.metrics import jaccard_score
jaccard_score(y_test, yhat_KNN)

# confusion matrix

from sklearn.metrics import classification_report, confusion_matrix
import itertools
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
print(confusion_matrix(y_test, yhat_KNN, labels=[1,0]))

from sklearn.metrics import confusion_matrix
cnf_matrix = confusion_matrix(y_test, yhat_KNN, labels=[1,0])
np.set_printoptions(precision=2)

plt.figure()
plot_confusion_matrix(cnf_matrix,classes=['churn=1','churn=0'],normalize=False,title='Confusion matrix')

print(classification_report(y_test, yhat_KNN))

"""Log Loss"""

from sklearn.metrics import log_loss
log_loss(y_test, yhat_prob_KNN)
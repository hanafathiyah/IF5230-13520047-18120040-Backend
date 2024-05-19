# -*- coding: utf-8 -*-
"""Regression - 13520047 - 18120040.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wNoJ_KPBxAHeo9Eq9PunUv0ZF9tf-sZ4

# Praktikum 2 IF5230 Aplikasi Inteligensi Buatan untuk Enterprise
13520047 - Hana Fathiyah
18120040 - Iftitah Naura Azzahra

Data yang digunakan untuk praktikum ini adalah data [vmCloud_data.csv]
https://www.kaggle.com/datasets/abdurraziq01/cloud-computing-performance-metrics

Pada praktikum ini, digunakan 3 modeling, yaitu Linear Regression, Polynomial Regression, dan Multiple Regression
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# !gdown 1cVz-CMEnOA2unkV4Jmmh_2H1DtbV12X2
df = pd.read_csv("used_device_data.csv")
df.head()

df.shape

df['weight'].unique()

df.replace("?", np.nan, inplace = True)

print(df['screen_size'].isnull().sum())
print(df['weight'].isnull().sum())

df[['screen_size']] = df[['screen_size']].astype('float')
df[['weight']] = df[['weight']].astype('float')

df.dtypes

df.head()

import numpy as np

# pre-processing
df.replace("?", np.nan, inplace = True)
# drop row with NaN in latency and resource allocation column
df.dropna(subset = ["weight"], axis = 0, inplace = True)

# reset index
df.reset_index(drop = True, inplace = True)
print(df.shape)

df[['screen_size']] = df[['screen_size']].astype('float')
df[['weight']] = df[['weight']].astype('float')

df.dtypes

df[['screen_size', 'weight']].head()

"""## Linear Regression"""

from sklearn.linear_model import LinearRegression

X = df[['screen_size']]
y = df['weight']

lm = LinearRegression()
lm.fit(X,y)
print('Dataset lengkap: ',df.shape)
print('Training data: ',X.shape)
print('Koefisien: ',lm.coef_)
print('Intercept: ',lm.intercept_)

import seaborn as sns
sns.scatterplot(data=df, x="screen_size", y="weight")

plt.figure(figsize=(8,5))
sns.regplot(x="screen_size", y="weight", data=df)
plt.ylim(0,)

plt.figure(figsize=(8,5))
sns.residplot(x=df['screen_size'], y=df['weight'])
plt.show()

Y_hat = lm.predict(X)

plt.figure(figsize=(8,5))
ax1 = sns.distplot(df['weight'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)

plt.title('Actual vs Fitted Values')
plt.xlabel('weight')
plt.ylabel('Proportion')

plt.show()
plt.close()

from sklearn.metrics import r2_score
import numpy as np

test_x = np.asanyarray(df[['screen_size']])
test_y = np.asanyarray(df[['weight']])
test_y_ = lm.predict(df[['screen_size']])

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_, test_y) )

"""## Polynomial Regression


"""

X = df['screen_size']
y = df['weight']

f = np.polyfit(X, y, 3)
p = np.poly1d(f)
print(p)

def PlotPolly(model, independent_variable, dependent_variable, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit : Weight ~ Screen Size')
    ax = plt.gca()
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('weight')

    plt.show()
    plt.close()

PlotPolly(p, X, y, 'screen_size')

plt.figure(figsize=(8, 5))

ax1 = sns.distplot(df['weight'], hist=False, color="r", label="Actual Value")
sns.distplot(p(X), hist=False, color="b", label="Fitted Values" , ax=ax1)

plt.title('Actual vs Fitted Values for Weight')
plt.xlabel('Weight')
plt.ylabel('Proportion')

plt.show()
plt.close()

from sklearn.metrics import r2_score

test_x = np.asanyarray(X)
test_y = np.asanyarray(y)
test_y_ = p(X)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_ , test_y) )

"""## Multiple Linear Regression"""

df.head()

Z = df[['screen_size', 'internal_memory', 'ram', 'battery', 'rear_camera_mp', 'front_camera_mp', 'normalized_new_price']]
Y = df['normalized_used_price']

df.dropna(subset = ["internal_memory"], axis = 0, inplace = True)
df.dropna(subset = ["ram"], axis = 0, inplace = True)
df.dropna(subset = ["battery"], axis = 0, inplace = True)
df.dropna(subset = ["rear_camera_mp"], axis = 0, inplace = True)
df.dropna(subset = ["front_camera_mp"], axis = 0, inplace = True)
df.dropna(subset = ["normalized_new_price"], axis = 0, inplace = True)
df.dropna(subset = ["normalized_used_price"], axis = 0, inplace = True)

# reset index
df.reset_index(drop = True, inplace = True)

lm_mv = LinearRegression()
lm_mv.fit(Z,Y)
print('Dataset lengkap: ',df.shape)
print('Training data: ',X.shape)
print('Koefisien: ',lm_mv.coef_)
print('Intercept: ',lm_mv.intercept_)

Y_hat_mv = lm_mv.predict(Z)

plt.figure(figsize=(8,5))
ax1 = sns.distplot(df['normalized_used_price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat_mv, hist=False, color="b", label="Fitted Values" , ax=ax1)

plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Normalized Used Price')
plt.ylabel('Proportion')

plt.show()
plt.close()

from sklearn.metrics import r2_score

test_x = np.asanyarray(Z)
test_y = np.asanyarray(Y)
test_y_ = lm_mv.predict(Z)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_ , test_y) )


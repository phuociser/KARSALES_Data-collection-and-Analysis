# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:08:05 2022

@author: Phuoc Phe Phon

"""
import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv(r'C:\Users\Phuoc Phe Phon\Desktop\pYTHON\data final\dataxeMODEL.csv')
df.drop('Links',inplace=True,axis = 1 )
df_dum=pd.get_dummies(df)
X=df_dum.drop(['Giá'],axis =1 )
y=df_dum['Giá'].values
#train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
lm = LinearRegression()
lm.fit(X_train,y_train)
print(np.mean(cross_val_score(lm, X_train,y_train,scoring='neg_mean_absolute_error',cv=3)))

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))

# tune models GridsearchCV 








## xây dựng bảng sumary thống kê
# import statsmodels.api as sm
# X_sm = sm.add_constant(X)
# model=sm.OLS(y,X_sm)
# print(model.fit().summary())

# Linear regression


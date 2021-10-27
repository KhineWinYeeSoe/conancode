import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import utils
stock_data=pd.read_csv('https://raw.githubusercontent.com/iambharathvaj/Stock-Price-Prediction/master/AAPL.csv')
stock_data
stock_data.shape
stock_data.drop('Date',axis=1,inplace=True)
X=stock_data.iloc[:,:-1]
X
y=stock_data.iloc[:,-3]
y
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.25,random_state=0)
X_train
X_test.shape
model=LinearRegression()
lab_enc = preprocessing.LabelEncoder()
training_scores_encoded = lab_enc.fit_transform(Y_train)
print(training_scores_encoded)
print(utils.multiclass.type_of_target(Y_train))
print(utils.multiclass.type_of_target(Y_train.astype('int')))
print(utils.multiclass.type_of_target(training_scores_encoded))
model.fit(X_train, training_scores_encoded)
print("LinearRegression")
print(model.predict(X_test))
y_pred=model.predict(X_test)
y_pred
summation=sum([((y-y_predict)**2) for y,y_predict in zip(Y_test,y_pred)])
summation
mse_error=summation/len(Y_test)
mse_error
for y,y_predict in zip(Y_test,y_pred):
  print(y,',',y_predict)
  

import pickle
with open('model.pkl', 'wb') as file:
pickle.dump(classifier, file)
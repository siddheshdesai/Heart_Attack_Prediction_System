import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


heart_data = pd.read_csv('heart.csv')

# print last 5 rows of the dataset
# heart_data.tail()

# number of rows and columns in the dataset
# heart_data.shape

# checking for missing values
heart_data.isnull().sum()

# statistical measures about the data
heart_data.describe()

# checking the distribution of Target Variable
heart_data['target'].value_counts()


X = heart_data.drop(columns='target', axis=1)# 'target' is 1 = high risk, 0 = low risk
Y = heart_data['target']

# Split for training
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train model
model = LogisticRegression()

model.fit(X_train, Y_train)


# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# print('Accuracy on Training data : ', training_data_accuracy)
# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# print('Accuracy on Test data : ', test_data_accuracy)

#input_data = (63,1,3,145,233,1,0,150,0,2.3,0,0,1)

# #change the input data to a numpy array
#input_data_as_numpy_array= np.asarray(input_data) #@pabact 

# # reshape the numpy array as we are predicting for only on instance YouTube Content Creator
#input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#prediction = model.predict(input_data_reshaped)
#print(prediction) #parvatcomputertechnology@gmail.com

#if (prediction[0]== 0): 
#   print('The Person does not have a Heart Disease')
#else:
#  print('The Person has Heart Disease')





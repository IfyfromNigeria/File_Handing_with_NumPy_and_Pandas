# Importing the important libraries
import numpy as np
import pandas as pd

#declaring variables
d = open('Loan_prediction_dataset.csv', 'r')
with d as file:
    info = np.genfromtxt(file, delimiter = ',')
    file.close()

operand = info[:,8]
mean = np.mean(operand[1:])
print(mean)


file_path = 'Loan_prediction_dataset.csv'
data = pd.read_csv(file_path)
print(data['LoanAmount'].describe())
# poi = df['LoanAmount'].values
# poi_array = np.array(poi)
# mean1 = np.mean(poi)
# print(mean1)
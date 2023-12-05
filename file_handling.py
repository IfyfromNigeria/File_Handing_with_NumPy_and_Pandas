# word = input('Enter any word:')
# for i in range(20):
#     print(word)

import numpy as np
# Load the dataset from CSV file
dataset = np.genfromtxt('Loan_prediction_dataset.csv', delimiter=',')

# Extract the 9th column (index 8) from the dataset
loan_amount = dataset[:, 8]
to_use = []
# Loop through each element in the loan_amount column
for i in loan_amount:
    # Convert the element to a float
    try:
        float_value = float(i)
        if not np.isnan(float_value):
            to_use.append(float_value)
    except ValueError:
        print(f"Unable to convert {i} to float")

to_use_array = np.array(to_use)
mean = np.mean(to_use_array)
median = np.median(to_use_array)
st_dev = np.std(to_use_array)
count = np.count_nonzero(to_use_array)
print(mean)
print(median)
print(st_dev)
print(to_use_array.shape)
print(count)
print(to_use_array)


# Alternatively, you can use NumPy's vectorized operations to convert the entire array to float
# loan_amount_float = np.asarray(loan_amount, dtype=float)
# print(loan_amount_float)

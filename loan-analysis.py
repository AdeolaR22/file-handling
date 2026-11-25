# This ➡️ dataset contains loan information, including loan ID, customer gender, location, region, total price for each loan etc.

# Begin by importing the necessary libraries, numpy.
# Use the open() function to open csv file and assign the result to a variable.
# Use the numpy array to perform some basic statistical analysis on the data, such as finding the mean, median, and standard deviation of the loan amounts.
# Note:

# Be sure to close the file after you have finished reading it in with the open() function.
# Use the delimiter parameter in the genfromtxt() function to specify that the values in the file are separated by commas.
# You can use the numpy functions mean(), median(), and std() to find the mean, median, and standard deviation of the loan amounts.



 
# Step 1: Import NumPy
import numpy as np

# Step 2: Open the CSV file
file = open("Loan_prediction_dataset.csv", "r", encoding="utf-8")

# Step 3: Read the CSV file using NumPy
data = np.genfromtxt(
    file,
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8",
    filling_values=np.nan
)

# Step 4: Close the file
file.close()

# Step 5: Extract the loan amounts
loan_amounts = np.array(data["LoanAmount"], dtype=float)

# Step 6: Remove missing values
loan_amounts = loan_amounts[~np.isnan(loan_amounts)]

# Step 7: Calculate statistics
mean = np.mean(loan_amounts)
median = np.median(loan_amounts)
standard_deviation = np.std(loan_amounts)

# Step 8: Display the results
print("Loan Analysis Results")
print("---------------------")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", standard_deviation)


 

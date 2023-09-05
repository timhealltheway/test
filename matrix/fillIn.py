import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, stdev
import cmath
from fancyimpute import SoftImpute, KNN,NuclearNormMinimization,BiScaler


def fillIn(matrix):
    # Reshaping magnitudes into a matrix
    # matrix = np.array([matrix[:3], matrix[-3:]])
    first_row = matrix[0:5]
    first_row.append(np.nan)

    second_row = matrix[5:11]
    third_row = matrix[11:]

    x = np.array([first_row,second_row,third_row])

    # Append nan to the end of the first row
    # modified_first_row = np.append(matrix[0], np.nan)
    # modified_second_row = np.append(matrix[1], matrix[1][-1])

    # Construct the modified matrix
    # modified_matrix = np.array([modified_first_row, modified_second_row])
    # print(modified_matrix)

    # # Apply SoftImpute for matrix completion
    # completed_matrix = SoftImpute().fit_transform(modified_matrix)
    # completed_matrix = KNN(k=3).fit_transform(modified_matrix)
    completed_matrix = NuclearNormMinimization().fit_transform(x)


    # Get indices of missing values
    missing_indices = np.where(np.isnan(x))

    # Extract imputed values using missing_indices
    imputed_values = completed_matrix[missing_indices]

    return imputed_values


# array_1d = np.array([24801.54545, 24801.65656, 24801.62656,24774.6565, 24774.56565,24774.5624552])
#
# x = fillIn(array_1d)
# print(x)

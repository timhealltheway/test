import json
import os
import csv
from statistics import mean, stdev

# Define lists to store the extracted data from each JSON file
data_array_1pct = []
data_array_2pct = []
data_array_5pct = []
data_array_10pct = []
data_array_20pct = []


# Directory where your JSON files are located
json_directory = 'matrixevaluation/1k'

# Loop through the files in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        # Construct the full path to the JSON file
        file_path = os.path.join(json_directory, filename)

        # Open and read the JSON file
        with open(file_path, 'r') as json_file:
            try:
                # Parse the JSON data and add it to the appropriate array
                data = json.load(json_file)
                if "missing-1k-1pct" in filename:
                    data_array_1pct.append(data)
                elif "missing-1k-2pct" in filename:
                    data_array_2pct.append(data)
                elif "missing-1k-5pct" in filename:
                    data_array_5pct.append(data)
                elif "missing-1k-10pct" in filename:
                    data_array_10pct.append(data)
                elif "missing-1k-20pct" in filename:
                    data_array_20pct.append(data)
            except json.JSONDecodeError as e:
                print(f"Error parsing {filename}: {e}")

print("index",data_array_2pct)
# print(data_array_2pct)

csv_file = "pmu8_1000.csv"
mag1pct_Values = []
ang1pct_Values = []

mag2pct_Values = []
ang2pct_Values = []

mag5pct_Values = []
ang5pct_Values = []

mag10pct_Values = []
ang10pct_Values = []

mag20pct_Values = []
ang20pct_Values = []


with open(csv_file,'r') as file:
    reader = csv.DictReader(file)

    for row_index, row in enumerate(reader):
        if row_index in data_array_1pct[0]:
            magnitude_value = float(row["Magnitude01"])
            angle_value = float(row["Angle01"])
            mag1pct_Values.append(magnitude_value)
            ang1pct_Values.append(angle_value)
        if row_index in data_array_2pct[0]:
            magnitude_value = float(row["Magnitude01"])
            angle_value = float(row["Angle01"])
            mag2pct_Values.append(magnitude_value)
            ang2pct_Values.append(angle_value)
        if row_index in data_array_5pct[0]:
            magnitude_value = float(row["Magnitude01"])
            angle_value = float(row["Angle01"])
            mag5pct_Values.append(magnitude_value)
            ang5pct_Values.append(angle_value)
        if row_index in data_array_10pct[0]:
            magnitude_value = float(row["Magnitude01"])
            angle_value = float(row["Angle01"])
            mag10pct_Values.append(magnitude_value)
            ang10pct_Values.append(angle_value)
        if row_index in data_array_20pct[0]:
            magnitude_value = float(row["Magnitude01"])
            angle_value = float(row["Angle01"])
            mag20pct_Values.append(magnitude_value)
            ang20pct_Values.append(angle_value)

# print("mag:", mag2pct_Values)
# print("mag20:", mag20pct_Values)
# print("ang:", ang20pct_Values)


#get results from text
result_file_path = "matrixevaluation/1k"
mag1pct_resValue = []
mag2pct_resValue = []
mag5pct_resValue = []
mag10pct_resValue = []
mag20pct_resValue = []

ang1pct_resValue = []
ang2pct_resValue = []
ang5pct_resValue = []
ang10pct_resValue = []
ang20pct_resValue = []

for filename in os.listdir(result_file_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(result_file_path,filename)

        with open(file_path,'r') as file:
            if "1pct" in filename:
            #skip header
                next(file)

                for line in file:
                    fields = line.strip().split(',')
                    magnitude = float(fields[1])
                    mag1pct_resValue.append(magnitude)
                    ang1pct_resValue.append(float(fields[2]))
            elif "2pct" in filename:
            #skip header
                next(file)

                for line in file:
                    fields = line.strip().split(',')
                    magnitude = float(fields[1])
                    mag2pct_resValue.append(magnitude)
                    ang2pct_resValue.append(float(fields[2]))
            elif "5pct" in filename:
            #skip header
                next(file)

                for line in file:
                    fields = line.strip().split(',')
                    magnitude = float(fields[1])
                    mag5pct_resValue.append(magnitude)
                    ang5pct_resValue.append(float(fields[2]))
            elif "10pct" in filename:
            #skip header
                next(file)

                for line in file:
                    fields = line.strip().split(',')
                    magnitude = float(fields[1])
                    mag10pct_resValue.append(magnitude)
                    ang10pct_resValue.append(float(fields[2]))
            elif "20pct" in filename:
            #skip header
                next(file)

                for line in file:
                    fields = line.strip().split(',')
                    magnitude = float(fields[1])
                    mag20pct_resValue.append(magnitude)
                    ang20pct_resValue.append(float(fields[2]))

# print("res1", mag2pct_resValue)
# print("res20", mag20pct_resValue)
# print("ang",ang1pct_resValue)


def calculate_approximation_error(exact, approximate):
    x = abs(exact - approximate) / exact * 100
    # print("exact",exact,"approx",approximate,"abs error", x )
    return abs(exact - approximate) / exact * 100

#calculate the average, std deviation, and range of approximation errors
def calculate_approximation_error_statistics(exact_measurements, approximate_measurements, generated_indexes = None):
    approximation_errors = []
    min_length = min(len(exact_measurements), len(approximate_measurements))
    for i in range(min_length):
        approximation_errors.append(calculate_approximation_error(exact_measurements[i], approximate_measurements[i]))
        # print(calculate_approximation_error(exact_measurements[i], approximate_measurements[i]))

    return mean(approximation_errors), stdev(approximation_errors), max(approximation_errors)

# resultx = [mag20pct_Values[i] - mag20pct_resValue[i] for i in range(200)]
# print("10",len(mag10pct_Values), len(mag10pct_resValue))
print("res",calculate_approximation_error_statistics(mag1pct_Values,mag1pct_resValue))
# print("res20", calculate_approximation_error_statistics(mag20pct_Values,mag20pct_resValue))
# print("another res1",len(mag20pct_resValue))

meanRes =[]

m, std, c = calculate_approximation_error_statistics(mag1pct_Values,mag1pct_resValue)
meanRes.append(m)

m, std, c = calculate_approximation_error_statistics(mag2pct_Values,mag2pct_resValue)
meanRes.append(m)

m, std, c = calculate_approximation_error_statistics(mag5pct_Values,mag5pct_resValue)
meanRes.append(m)

m, std, c = calculate_approximation_error_statistics(mag10pct_Values,mag10pct_resValue)
meanRes.append(m)

# m, std, c = calculate_approximation_error_statistics(mag20pct_Values,mag20pct_resValue)
# meanRes.append(m)

print(meanRes)

import matplotlib.pyplot as plt

def plot_graph(array1, array2, x_label="X-axis", y_label="Y-axis", title="Graph Title"):
    """
    Plot a graph with two arrays.

    Parameters:
        array1 (list or numpy.ndarray): The first array to be plotted on the x-axis.
        array2 (list or numpy.ndarray): The second array to be plotted on the y-axis.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the graph.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))  # Set the figure size (optional)

    # Plot the data
    plt.plot(array1, array2, marker='o', linestyle='-', color='b', label="Data")

    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Add a legend (optional)
    plt.legend()

    # Display the plot
    plt.grid(True)  # Add grid lines (optional)
    plt.show()

# Example usage:
# Assuming you have two arrays, array_x and array_y
# plot_graph(array_x, array_y, x_label="X-axis", y_label="Y-axis", title="My Plot")



x = [1,2,5,10]

# Example usage:
# Assuming you have two arrays, array_x and array_y
plot_graph(x, meanRes, x_label="Missing Rate, %", y_label="Mean Error", title="My Plot")

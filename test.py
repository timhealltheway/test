import os
import json
import csv
from statistics import mean, stdev
import matplotlib.pyplot as plt
import numpy as np
from jpt_algo_evaluation.jpt_algo import calculate_complex_voltage, calculate_angle_statistics, calculate_approximation_error_statistics


def plot_graph(array1, array2, array3, x_label="X-axis", y_label="Y-axis", title="Graph Title"):
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

    plt.errorbar(array1, array2, yerr=array3, fmt='o', label="td Dev")

    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Add a legend (optional)
    plt.legend()

    # Display the plot
    plt.grid(True)  # Add grid lines (optional)
    plt.show()

def load_data_by_percentage(directory, percentage_range):
    data_arrays = {}

    for percent in percentage_range:
        filename_pattern = f"missing-5k-{percent}-pct"
        data_arrays[percent] = []

        for filename in os.listdir(directory):
            if filename.startswith(filename_pattern) and filename.endswith('.json'):
                file_path = os.path.join(directory, filename)

                try:
                    with open(file_path, 'r') as json_file:
                        data = json.load(json_file)
                        data_arrays[percent].append(data)
                except json.JSONDecodeError as e:
                    print(f"Error parsing {filename}: {e}")

    return data_arrays

def process_csv_data(csv_file, data_array, mag_values, ang_values):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row_index, row in enumerate(reader):
            for pct, index in data_array.items():
                if row_index in index:
                    magnitude_value = float(row["Magnitude01"])
                    angle_value = float(row["Angle01"])
                    mag_values[pct].append(magnitude_value)
                    ang_values[pct].append(angle_value)

def parse_results(result_file_path):
    magnitude_resValues = {}
    angle_resValues = {}

    for percentage in range(1, 11):
        percentage_str = str(percentage) + "pct"
        magnitude_resValues[f"mag{percentage}pct"] = []
        angle_resValues[f"ang{percentage}pct"] = []

        for filename in os.listdir(result_file_path):
            if filename.endswith('.txt') and percentage_str in filename:
                file_path = os.path.join(result_file_path, filename)

                with open(file_path, 'r') as file:
                    # Skip header
                    next(file)

                    for line in file:
                        fields = line.strip().split(',')
                        magnitude = float(fields[1])
                        angle = float(fields[2])
                        magnitude_resValues[f"mag{percentage}pct"].append(magnitude)
                        angle_resValues[f"ang{percentage}pct"].append(angle)

    return magnitude_resValues, angle_resValues

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

def calculate_angle_difference(original_angle,pred_angle):
    diffs =[]
    min_length = min(len(original_angle), len(pred_angle))
    print("length",min_length)

    for i in range(min_length-1):
        next_pred = pred_angle[i+1]
        # diff1 = abs(original_angle[i] - pred_angle[i])
        diff2 = abs(original_angle[i] - next_pred)
        for j in range (i+1):
            pred_value = pred_angle[j]
            diff1 = abs(original_angle[i] - pred_value)
            if diff1 > 2.5:
                continue
            diffs.append(diff1)

        # if diff1 > 180 or diff2 > 180:
        #     diff1 = 360 - diff1
        #     diff2 = 360 - diff2
        #
        # if abs(diff1 - diff2) >5 :
        #     diffs.append(diff1)
        #
        # diffs.append(diff2)
        print("origin",original_angle[i], "pred:", pred_angle[i] ,"diff",diff1)

    total_diff = sum(diffs)
    avg_diff = total_diff / min_length
    print(avg_diff)
    return avg_diff




# Directory where your JSON files are located
json_directory = 'matrixevaluation/5k'

# Define the range of percentages you have files for
percentage_range = range(1, 11)

# Call the function to load the data
data_arrays = load_data_by_percentage(json_directory, percentage_range)

# Access the data arrays as needed
data_array_1pct = data_arrays[1]
data_array_2pct = data_arrays[2]
data_array_3pct = data_arrays[3]
data_array_4pct = data_arrays[4]
data_array_5pct = data_arrays[5]
data_array_6pct = data_arrays[6]
data_array_7pct = data_arrays[7]
data_array_8pct = data_arrays[8]
data_array_9pct = data_arrays[9]
data_array_10pct = data_arrays[10]
# print("index", data_array_1pct[0], "length",len(data_array_1pct[0]))

# Usage example:
csv_file = "pmu2_5k.csv"

data_array = {
    1: data_array_1pct[0],
    2: data_array_2pct[0],
    3: data_array_3pct[0],
    4: data_array_4pct[0],
    5: data_array_5pct[0],
    6: data_array_6pct[0],
    7: data_array_7pct[0],
    8: data_array_8pct[0],
    9: data_array_9pct[0],
    10: data_array_10pct[0],
}

mag_values = {pct: [] for pct in range(1, 11)}
ang_values = {pct: [] for pct in range(1, 11)}

process_csv_data(csv_file, data_array, mag_values, ang_values)
# print((mag_values[1]))

result_file_path = "matrixevaluation/5k"
magnitude_values, angle_values = parse_results(result_file_path)
# print(magnitude_values["mag1pct"], "length", len(magnitude_values["mag1pct"]))

meanRes = []
stands =[]
for percentage in range(1, 11):
    # Calculate the statistics for each percentage
    m, std, c = calculate_approximation_error_statistics(mag_values[percentage], magnitude_values[f"mag{percentage}pct"])
    meanRes.append(m)
    stands.append(std)
    print(f"For {percentage}%: m = {m}, std = {std}, c = {c}")


print("Averge error:", meanRes)

error_x = [x for x in range(1,11)]
print("Standard dev:", stands)
plot_graph(error_x, meanRes, stands,x_label="Missing Data Rate, %", y_label="Magnitude MAPE, %", title="Magnitude Mean absolute percentage Error vs Missing Data Rate")


angRes= []
for percentage in range(1,11):
    # Calculate the statistics for each percentage
    m = calculate_angle_difference(ang_values[percentage], angle_values[f"ang{percentage}pct"])
    # average_ang_error, std_dev_ang, max_error_ang = calculate_angle_statistics(exact_measurements=ang_values[percentage], approximate_measurements=angle_values[f"ang{percentage}pct"])

    angRes.append(m)

print("angle difference:", angRes)
# plot_graph(error_x, angRes, x_label="Missing Data Rate, %", y_label="Angle difference, degree", title="Phase Angle difference vs Missing Data Rate")
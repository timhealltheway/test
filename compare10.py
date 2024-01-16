import csv
import matplotlib.pyplot as plt
import numpy as np


def plot_graph(array1, array2,array3,x_label="X-axis", y_label="Y-axis", title="Graph Title", file_name="plot.pdf"):
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
    plt.plot(array3, array1, 'o-',label="Recovered value")
    plt.plot(array3, array2, 'x-',label="Original Data")

    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)


    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Add a legend (optional)
    plt.legend()

    # Display the plot
    plt.grid(True)  # Add grid lines (optional)
    # plt.show()

    # Save the plot as a PDF
    plt.savefig(file_name, format='pdf')
    plt.close()  # Close the figure



csv_file_path = "10per-ang.csv"  # Change the file extension to .tsv if it is indeed tab-separated

# Initialize empty lists to hold the column data
magnitude = []
orig = []

# Open the CSV file and read each row
with open(csv_file_path, newline='') as csvfile:
    # Specify the delimiter as a tab character
    csvreader = csv.reader(csvfile, delimiter='\t')
    next(csvreader)  # Skip the header row if there is one
    for row in csvreader:
        # Append data from each row into the lists
        magnitude.append(float(row[0]))  # Assuming the first column is 'magnitude'
        orig.append(float(row[1]))  # Assuming the second column is 'orig'

# magnitude and orig are now lists containing the data from each column
print("length:", len(magnitude))
print("length of origin leng:", len(orig))
plot_graph(magnitude,orig,np.arange(len(magnitude)),x_label = "Number of packet missing",y_label = "Phase Angle(Degree)",
title = "",file_name= '10-ang.pdf')

#"Number of packet missing"   Magnitude(Volts)

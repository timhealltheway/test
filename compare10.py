import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib as mpl

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
    # Set the font to Times New Roman for all elements
    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.figure(figsize=(10, 4))  # Set the figure size (optional)

    # Plot the data

    plt.plot(array3, array1,label="Recovered Value",color='#FF0000')
    plt.plot(array3, array2,label="Original Data",color='#0072BD')
    # Setting the y-axis range
    # plt.ylim([-180, 180])  # Sets the y-axis to range from 0 to 12
    # Add labels and title
    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)
    plt.title(title)

    # Set the font size of the axis tick labels
    plt.tick_params(axis='both', which='major', labelsize=25)  # Set the font size here

    # Add a legend with increased font size
    plt.legend(loc='upper left',fontsize=20)  # You can specify a numeric value or 'small', 'medium', 'large', 'x-large', etc.

    # Display the plot
    plt.grid(True)  # Add grid lines (optional)
    plt.tight_layout()
    # plt.show()

    # Save the plot as a PDF
    plt.savefig(file_name, format='pdf')
    plt.close()  # Close the figure



csv_file_path = "10per-mag.csv"  # Change the file extension to .tsv if it is indeed tab-separated

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
# print("length:", len(magnitude))
# print("length of origin leng:", len(orig))
plot_graph(magnitude,orig,np.arange(len(magnitude)),x_label = "Missing packet index",y_label = "Magnitude (V)",
title = "",file_name= '10-mag.pdf')

#"Number of packet missing"   Magnitude(Volts) Phase Angle (Degrees)

# plot_graph(magnitude,orig,np.arange(len(magnitude)),x_label = "Missing packet index",y_label = "Phase Angle (Degrees)",
# title = "",file_name= '10-ang.pdf')

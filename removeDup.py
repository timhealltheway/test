# Define the path to your input text file and output text file
input_file_path = 'matrixevaluation/5k/1pct_result1.txt'
output_file_path = 'matrixevaluation/5k/1pct_result2.txt'

header = 1
# Open the input file for reading
with open(input_file_path, 'r') as input_file:
    for _ in range(header):
        next(input_file)  # Read and discard the header lines

    lines = input_file.readlines()

# Open the output file for writing
with open(output_file_path, 'w') as output_file:
    for i in range(len(lines)):
        # Split the current line into its components
        current_parts = lines[i].strip().split(',')
        current_magnitude = current_parts[1]
        current_phase = current_parts[2]
        print(current_magnitude)

        # Check if the current magnitude is unique within the current group of three lines
        is_unique_magnitude = True
        for j in range(i + 1, min(i + 3, len(lines))):
            next_parts = lines[j].strip().split(',')
            next_magnitude = next_parts[1]
            next_phase = next_parts[2]
            # print(float(next_phase))
            if (current_magnitude == next_magnitude) & (abs(float(current_phase) - float(next_phase)) <0.3 ):
                is_unique_magnitude = False
                break

        # If the magnitude is unique, write the current line to the output file
        if is_unique_magnitude:
            output_file.write(lines[i])

print(f"Lines with duplicate magnitudes within groups of three removed. Output written to {output_file_path}")

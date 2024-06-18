import csv

# Define the input and output file paths
input_file_path = 'files/input/query3.txt'
output_file_path = 'files/output/output3.csv'

# Initialize variables to hold the data and control flags
data_started = False
data_lines = []
delimiter_count = 0

# Function to clean the timestamp
def clean_timestamp(timestamp):
    return timestamp.replace('.000', '').replace("T"," ").replace(':00','')

# Open and read the input file
with open(input_file_path, 'r') as file:
    for line in file:
        # Check for the start of data after the second line containing "+-------"
        if '+-------' in line:
            delimiter_count += 1
            if delimiter_count == 2:
                data_started = True
            continue  # Skip this line

        if data_started:
            if 'Query terminated' in line:
                break  # Stop if we reach the "Query terminated" line
            data_lines.append(line.strip())  # Collect data lines

# Remove the headers line if it exists
if data_lines and 'WINDOW_START' in data_lines[0]:
    data_lines.pop(0)

# Write the parsed data to a CSV file
with open(output_file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for line in data_lines:
        # Split the line by '|' and strip any extra spaces
        row = [item.strip() for item in line.split('|') if item.strip()]
        row[0] = clean_timestamp(row[0])
        row[1] = clean_timestamp(row[1])
        csvwriter.writerow(row)

print(f"Data successfully written to {output_file_path}")
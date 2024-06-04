import csv

# Define the input and output file paths
input_file_path = 'files/input/query6.txt'
output_file_path = 'files/output/query6.csv'

# Function to clean the timestamp
def clean_timestamp(timestamp):
    return timestamp.replace('.000', '').replace("T"," ")

# Open the input file for reading
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Find the starting and ending lines
start_line = 15  # line index starts from 0, so line 16 is index 15
end_line = None

# Find the end line index
for i, line in enumerate(lines):
    if "Query terminated" in line:
        end_line = i
        break

# Extract the relevant lines
data_lines = lines[start_line:end_line]

# Open the output file for writing
with open(output_file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the data rows
    for line in data_lines:
        if line.startswith('|'):
            # Split the line by '|' and strip the whitespace
            row = [item.strip() for item in line.split('|') if item.strip()]
            # Clean the timestamps
            row[0] = clean_timestamp(row[0])
            row[1] = clean_timestamp(row[1])
            csvwriter.writerow(row)

print(f"Data has been successfully written to {output_file_path}")

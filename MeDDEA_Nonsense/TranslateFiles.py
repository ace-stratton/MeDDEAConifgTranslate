import os
import csv
import datetime

def process_csvs(input_folder="csvs", output_folder="text_output"):
    # Create the output folder if it doesn't already exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over every file in the input folder
    for filename in os.listdir(input_folder):
        # Only process CSV files
        if filename.lower().endswith(".csv"):
            csv_path = os.path.join(input_folder, filename)
            
            # Prepare lists to hold column data
            first_col_values = []
            second_col_values = []
            
            # Read the CSV file
            with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                # Skip the header row
                next(reader, None)
                 # Iterate through rows
                for row in reader:
                    if len(row) > 1:
                        # Convert both columns from hex string to decimal
                        first_col_values.append(hex_to_decimal(row[0]))
                        second_col_values.append(hex_to_decimal(row[1]))
                    elif len(row) == 1:
                        first_col_values.append(hex_to_decimal(row[0]))

            # Create comma-delimited strings
            first_col_str = ",".join(first_col_values)
            second_col_str = ",".join(second_col_values)
            
            # Build timestamp for the output files
            timestamp = datetime.datetime.now().strftime("%y_%m_%d")
            
            # Strip off the .csv extension to name your output files
            base_name = filename[:-4] if filename.lower().endswith(".csv") else filename
            
            # Create output file names
            first_col_output_file = os.path.join(
                output_folder, f"{base_name}_regAdd_{timestamp}.txt"
            )
            second_col_output_file = os.path.join(
                output_folder, f"{base_name}_regValues_{timestamp}.txt"
            )
            
            # Write the first column data to file
            with open(first_col_output_file, mode="w", encoding="utf-8") as out_file:
                out_file.write(first_col_str)
            
            # Write the second column data to file
            with open(second_col_output_file, mode="w", encoding="utf-8") as out_file:
                out_file.write(second_col_str)

        print('Translating...')
    print('Done')


def hex_to_decimal(hex_str):
    """
    Takes a string like '0x0001' or '0001'
    and returns the decimal representation as a string, e.g. '1'.
    """
    # Strip whitespace and lowercase
    h = hex_str.strip().lower()
    
    # Remove '0x' if present
    if h.startswith('0x'):
        h = h[2:]
    
    # Convert hex to int, then back to string for final output
    return str(int(h, 16))


if __name__ == "__main__":
    process_csvs()

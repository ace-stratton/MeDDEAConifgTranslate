import csv
import os

# Suppose MeDDEATranslator.py is in the same directory, or is otherwise
# importable. Then you'd do:
import MeDDEATranslator

def main():
    # CHANGE THIS to the name of your .csv file
    filename = "PADRE-ThermalBalance_Log.csv"
    
    # Build input and output paths
    in_path = os.path.join("logs", filename)
    base, ext = os.path.splitext(filename)
    out_path = os.path.join("calibrated", f"{base}_calibrated{ext}")
    
    # A lookup table mapping COLUMN-INDEX -> NAME to use for translation
    # Example: we only translate column 4 using "fp_temp"
    translate_map = {
        4: "fp_temp",
        5: "dib_temp",
        6: "hvps_temp",
        7: "hvps_vsense",
        8: "hvps_csense",
        9: "csense_15v",
        10: "csense_33vd",
        11: "csense_33va",
        15: "heater_pwm_duty_cycle"
    }
    
    with open(in_path, mode="r", newline="") as infile, \
         open(out_path, mode="w", newline="") as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read and write headers directly (the first row in the CSV)
        headers = next(reader, None)
        if headers:
            writer.writerow(headers)
        
        # Now process each row
        for row in reader:
            # Make a copy of the row so we can update translated columns
            new_row = list(row)
            
            # Go through each column that needs translation
            for col_idx, name in translate_map.items():
                # Safely try to convert to float and translate
                try:
                    original_val = float(row[col_idx])
                    new_val = MeDDEATranslator.Translate(original_val, name)
                    # Write translated value back into new_row
                    new_row[col_idx] = new_val
                except (ValueError, IndexError):
                    # If we can't parse as float or index is out of range,
                    # skip or handle differently as needed
                    pass
            
            # Write the updated row
            writer.writerow(new_row)
    
    print(f"Created calibrated CSV: {out_path}")

if __name__ == "__main__":
    main()

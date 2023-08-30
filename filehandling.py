import pandas as pd
import os

# Directory containing CSV files
directory = 'sales-customerid'

# Directory to check for subdirectories
check_directory = 'sales-customerid/specfictimesofvisits/sexageofvisitor/uniqueidofproductbought'

# Get all subdirectories and subsubdirectories in check_directory
subdirs = [x[0] for x in os.walk(check_directory)]

# Column to check (0 for df.column[0], 3 for df.column[3])
column_to_check = 0

# List all files in the directory
for filename in os.listdir(directory):
    # Check if file is a CSV file
    if filename.endswith('.csv'):
        # Full path of the file
        file_path = os.path.join(directory, filename)
        
        # Read CSV file
        df = pd.read_csv(file_path)
        
        # Check if column_to_check is valid
        if column_to_check < len(df.columns):
            # Get the specified column name
            column_name = df.columns[column_to_check]
            
            # Check if specified column in CSV file matches with any subdirectory name
            for index, value in df[column_name].iteritems():
                if value in subdirs:
                    print(f"The value {value} in {filename} matches with a subdirectory in {check_directory}")
        else:
            print(f"Invalid column_to_check: {column_to_check}. The CSV file {filename} has only {len(df.columns)} columns.")

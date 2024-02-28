import pandas as pd
import glob

# Define the pattern for CSV files
pattern = "output_responses_*.csv"

# List all CSV files matching the pattern in the directory
csv_files = glob.glob(pattern)

# Initialize an empty DataFrame to store the concatenated data
concatenated_df = pd.DataFrame()

# Iterate through each CSV file
for file in csv_files:
    # Read the CSV file skipping the header row for all files except the first one
    if concatenated_df.empty:
        concatenated_df = pd.read_csv(file)
    else:
        df = pd.read_csv(file, header=0)
        concatenated_df = pd.concat([concatenated_df, df])

# Reset index of the concatenated DataFrame
concatenated_df.reset_index(drop=True, inplace=True)

# Write the concatenated DataFrame to a new CSV file
concatenated_df.to_csv("output_responses_C.csv", index=False)
#!/usr/bin/env python

import pandas as pd

def find_overlapping_libs(excel_file1, excel_file2):
    # Read Excel files into pandas DataFrames
    df1 = pd.read_excel(excel_file1)
    df2 = pd.read_excel(excel_file2)

    # Extract columns 1 and 3 from respective DataFrames
    column11_df1 = df1.iloc[:, 10]
    column3_df2 = df2.iloc[:, 2]

    # Convert both columns to sets for efficient comparison
    column11_set = set(column11_df1)
    column3_set = set(column3_df2)

    # Find common values
    common_values = column11_set.intersection(column3_set)

    # Get the values from column 1 of the first file
    values_from_col1_file1 = column11_df1.tolist()

    # Get the values from column 3 of the second file
    values_from_col3_file2 = column3_df2.tolist()

    return common_values, values_from_col1_file1, values_from_col3_file2

def main():
    excel_file1 = input("Enter the path to the GTDrift(.xlsx) file: ")
    excel_file2 = input("Enter the path to the BgeeDB(.xlsx) file: ")

    common_values, values_from_col1_file1, values_from_col3_file2 = find_overlapping_libs(excel_file1, excel_file2)

    if common_values:
        print("Overlapping libraries between GTDrift and BgeeDB:")
        for value in common_values:
            print(value)
    else:
        print("No overlapping libraries")

    print("\nValues from 'Experiment' column of the GTDrift file:")
    print(values_from_col1_file1)

    print("\nValues from 'Library ID' column of the Bgee file:")
    print(values_from_col3_file2)

if __name__ == "__main__":
    main()


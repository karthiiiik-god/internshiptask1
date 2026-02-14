Task 1 – Data Cleaning and Preprocessing

Dataset Name:
Employee Sample Dataset (Custom Raw Dataset for Internship Task)

Tools Used:
Python, Pandas

1. Original Dataset Details

Original Shape: (7, 5)

Total Missing Values: 2

1 missing value in Name

1 missing value in Salary

2. Data Cleaning Steps Performed

Removed rows with missing Name

Filled missing Salary values using median

Removed duplicate records

Standardized text values (Name formatted properly, Gender converted to lowercase and trimmed)

Converted Join Date to proper datetime format

Removed unrealistic outlier values (Age > 100)

Renamed column headers to lowercase with underscores

3. Duplicates Removed

Total Duplicates Removed: 1

4. Datatypes Fixed

Join Date converted from object to datetime

Numeric columns validated and retained as integers/floats

Column names standardized for consistency

5. Final Dataset Details

Final Shape: (4, 5)

Dataset is now clean, structured, and ready for analysis.

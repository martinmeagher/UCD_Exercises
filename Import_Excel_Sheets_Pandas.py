# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = pd.ExcelFile('battledeath.xlsx')

# Load spreadsheet: xls
xls = file.sheet_names

# Print sheet names
print(xls)

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0,], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
#import modules
import pandas as pd
import glob

# path of the folder
path = r'H:\每月事项\2022'

# reading all the excel files
filenames = glob.glob(path + "\*.xls")
print('File names:', filenames)

# initializing empty data frame
finalexcelsheet = pd.DataFrame()

# to iterate excel file one by one
# inside the folder
for file in filenames:

	# combining multiple excel worksheets
	# into single data frames
	df = pd.concat(pd.read_excel(
	file, sheet_name=None), ignore_index=True, sort=False)

	# appending excel files one by one
	finalexcelsheet = finalexcelsheet.append(
	df, ignore_index=True)

# to print the combined data
print('Final Sheet:')
#display(finalexcelsheet)

finalexcelsheet.to_excel(r'Final.xlsx', index=False)

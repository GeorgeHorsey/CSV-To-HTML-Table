import pandas

# Program to convert a CSV file into an HTML table for easy sharing
# with people that don't have spreadsheet software. 

#################
## HOW TO USE: ##
#################
# Place the csv file in the same directory as the .py 
# program. 
#
# Change the below variables to match the name of your csv
# and the desired output file name. 
#
# Run csv_to_html_table.py from the same directory as your csv
# 
# A New html file will then be created with your table. 

ReadFile = ("read_file.csv")
OutputFileName = ("TableOutput.html")

# NO NEED TO CHANGE LINES BELOW THIS COMMENT
ReadExistingCsv = pandas.read_csv(ReadFile)
ReadExistingCsv.to_html(OutputFileName)
html_file = ReadExistingCsv.to_html()

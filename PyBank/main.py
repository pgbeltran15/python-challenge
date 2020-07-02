import os
# Module for reading CSV files
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

# Create empty lists
date = []
data = []

# Define average
def Average(lst): 
    x = sum(lst)/len(lst)
    return '${:,.2f}'.format(x)

# Define get_key
def get_key(val): 
    for key, value in budget.items(): 
         if val == value: 
             return key 

# Currency Conversion
##'${:,.2f}'.format(Number)

# Open csv file
with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Create header
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #Convert rows into lists
        date.append(row[0])
        data.append(row[1])

# Convert data list from string to int
data =[int(i) for i in data]
#print(data)

# Convert csv into dict
budget = dict(zip(date,data))
# print(budget)

# Total number of months
Total_Months = len(budget)

# Net Total of "Profit/Losses" over entire period
Net_Total = round(sum(data),2)
Net_Total ='${:,.2f}'.format(Net_Total)

# The average of the changes in "Profit/Losses" over the entire period
Avg_Changes = Average(data)

# The greatest increase in profits (date and amount) over the entire period
Greatest_Increase = max(data)

# Get Month for Greastest Increase
Month_Inc = get_key(Greatest_Increase)

# # Convert Greatest Increase to Currency 
Greatest_Increase = '${:,.2f}'.format(Greatest_Increase)

# The greatest decrease in losses (date and amount) over the entire period
Greatest_Decrease = min(data)

# Get Month for Greatest Decrease
Month_Dec = get_key(Greatest_Decrease)

# # Convert Greatest Decrease to Currency
Greatest_Decrease = '${:,.2f}'.format(Greatest_Decrease)



Financial_Analysis = {
    "Total Months": Total_Months,
    "Total": Net_Total,
    "Average Changes" : Avg_Changes,
    "Greatest Increase in Profits" : Month_Inc + " " + Greatest_Increase,
    "Greatest Decrease in Profits": Month_Dec + " " + Greatest_Decrease}

print(Financial_Analysis)

# Write into text file Analysis Folder
import sys

output_path = os.path.join('Analysis','bank_analysis.txt')

with open(output_path, 'w') as f:
    print("Financial Analysis", file=f)
    print("----------------------", file=f)
    for key, value in Financial_Analysis.items():
        print(key, ' : ', value, file=f)


#Import Data
import os
import csv 

#Create the path to the file
csvpath=os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Variables
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []

#Count Months
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])

#Profit/Losses
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))

#Average Monthly Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    res = "{:.2f}".format(monthly_change)

#Greatest Increase
    profit_increase = max(revenue_change)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]

#Analysis
print(f'----------------------------'+'\n')

print(f'Financial Analysis'+'\n')

print(f'----------------------------'+'\n')

print("Total number of months included in the dataset is: " + str(len(month)) + " months")

print("The net total amount of 'Profit/Losses' is: $ " + str(total_revenue))
      
print("The average of the changes in 'Profit/Losses' is: $" + str(res))

print(f"The greatest Increase in Profits is: {month_increase} (${profit_increase})")

print(f"The greatest Decrease in Losses is: {month_decrease} (${profit_decrease})")

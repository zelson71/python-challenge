#import libraries
import csv
import os
import pandas as pd
# empty list variables
dates = []
revenue = []


# Dataset to write data accumulated to
file_to_write = "analysis/budget_summary.txt"
# Dataset to evaluate
with open("Resources/budget_data.csv") as file:
    reader = csv.reader(file)

    # skip the header row
    next(reader)
    # collect the data
    for row in reader:
        dates.append(row[0])
        # read as string and convert to integer
        revenue.append(int(row[1]))
print("Financial Analysis ")
print("------------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total Revenue: ${sum(revenue)}")
# revenue change starts with 2nd value.
# Loop through all the rows of data we collected

revenue_Change = []
for i in range(1, len(revenue)):
    revenue_Change.append(revenue[i] - revenue[i-1])
# "date" list has 1 more value than "revCh" list.
print(
    f"Average Revenue Change: ${round(sum(revenue_Change)/len(revenue_Change), 2)}")
print(
    f"Greatest Increase in Revenue: {dates[revenue_Change.index(max(revenue_Change))+1]} (${max(revenue_Change)})")
print(
    f"Greatest Decrease in Revenue: {dates[revenue_Change.index(min(revenue_Change))+1]}(${min(revenue_Change)})")
# export to text file for further review
with open(file_to_write, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("__________________________________")
    txt_file.write("\n")
    txt_file.write(f"Total Months: {len(dates)}")
    txt_file.write("\n")
    txt_file.write(f"Total Revenue: ${sum(revenue)}")
    txt_file.write("\n")
    txt_file.write(
        f"Average Revenue Change: ${round(sum(revenue_Change)/len(revenue_Change),2)}")
    txt_file.write("\n")
    txt_file.write(
        f"Greatest Increase in Revenue: {dates[revenue_Change.index(max(revenue_Change))+1]} (${max(revenue_Change)})")
    txt_file.write("\n")
    txt_file.write(
        f"Greatest Decrease in Revenue: {dates[revenue_Change.index(min(revenue_Change))+1]} (${min(revenue_Change)})\n")

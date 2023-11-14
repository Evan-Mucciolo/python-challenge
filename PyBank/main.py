# Import the os module to create filepaths across operating systems
import os

# Import the CSV module so we can work with and handle CSV Files
import csv

# Import the sys module to write the output of my code to a text file

import sys

# Initialize the variable total rows to 0 so it can be used to count the rows in our loop below.
Total_Rows = 0

# Intiialize the Variable profits and losses total to start at 0 so it can be tallied below. 

Profits_Losses_Total = 0

# Initialize the profits for monthly change 

Profit_change = 0

# Set the list below to store the change in the profit/loss from each month.

monthly_change = []

# Set list below to store the current month

month = []

# create a new dictionary

monthly_change_dictionary = {}

# Use the line below to show the filepath to the csv that we're going to use called 'budget_data.csv'
csv_path = os.path.join('Resources', 'budget_data.csv')


# The below line tells use to open the filepath to our csv, which we could name anything, and then store it as the variable called 'csv_file', which could also be named anything. 
with open(csv_path) as csv_file:
    
    # The below line uses a method csv.reader which takes the arguments of a csv file and a delimiter value and returns an iterable object
    read_csv = csv.reader(csv_file,delimiter=',')
    
    # The next() method moves to the next row of the CSV. We do this here to skip the header row. 
    next(read_csv)

    # For each row in the CSV file do this:
    for x in read_csv:
            
        # set the variable first column to equal the first column of the csv row that is returned. Denoted by the [0]
        first_column = x[0]
       
        # set the variable second column equal to the second column of the csv row that is returned. Denoted by the [1].  
        second_column = x[1]
        
        # Find the monthly change in profit 
        Profit_change = int(second_column) - int(Profit_change)
        
        # Append the monthly change in profit to our list
        monthly_change.append(Profit_change)
        
        # append the current month to the month list.
        
        month.append(first_column)
        
        # add a value to our dictionary
        
        monthly_change_dictionary[first_column] = Profit_change
        
        # Assign the current value of the profit for that month to profit change, to be used as the profit change for the next iteration to correctly find the difference between months.
        Profit_change = second_column       
    
        
        # Set the profits running total equal to the total from the last iteration plus the value from the current row/column we are on in our loop. 
        Profits_Losses_Total = Profits_Losses_Total + int(second_column) 
          
        # Counts the number of total rows and updates it each time in the loop. 
        Total_Rows = Total_Rows + 1
        
        
        
       # print(f"CSV Row: {x}")
        #print(Profits_Losses_Total)


# Remove the first value in profit change to correctly calculate the average monthly profit. (Found .pop method by searching chatgpt)

monthly_change.pop(0)

# Remove the first value in the month list because we do not need it. 

month.pop(0)

# Calculate the Average of Monthly Change and round to 2 decimal places. The round method was found using chatgpt.

Average_monthly_change = round(sum(monthly_change)/len(monthly_change),2)

# find the maximum and minimum values that are stored in my dictionary and their respective keys. The code for these functions was found usng chatgpt. 

greatest_profit = max(monthly_change_dictionary.values())
key_for_greatest = max(monthly_change_dictionary, key=monthly_change_dictionary.get)


greatest_loss = min(monthly_change_dictionary.values())
key_for_least = min(monthly_change_dictionary, key=monthly_change_dictionary.get)


# Print the text above our analysis and print to the terminal

print("Financial Analysis")
print("----------------------------")

# Print the total months in our CSV File
print(f"Total Months: {Total_Rows}")
# Print the total profit/losses in our CSV File
print(f"Total: ${Profits_Losses_Total}")
# Print the average monthly change
print(f"Average Change: ${Average_monthly_change}")

# Print the greatest increase in monthy profits
print(f"Greatest Increase in Profits: {key_for_greatest} (${greatest_profit})")

# Print the greatest decrease in monthy profits
print(f"Greatest Decrease in Profits: {key_for_least} (${greatest_loss})")


# Print the output of this analysis to a text file

with open("PyBank_Text_Output.txt", 'w') as file:
    
    sys.stdout = file
    
    print("Financial Analysis")
    print("----------------------------")

    # Print the total months in our CSV File
    print(f"Total Months: {Total_Rows}")
    # Print the total profit/losses in our CSV File
    print(f"Total: ${Profits_Losses_Total}")
    # Print the average monthly change
    print(f"Average Change: ${Average_monthly_change}")

    # Print the greatest increase in monthy profits
    print(f"Greatest Increase in Profits: {key_for_greatest} (${greatest_profit})")

    # Print the greatest decrease in monthy profits
    print(f"Greatest Decrease in Profits: {key_for_least} (${greatest_loss})")
    
sys.stdout = sys.__stdout__
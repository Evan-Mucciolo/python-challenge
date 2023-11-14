# Import the OS module eto create filepaths across operating systems
import os

# Import the CSV module so we can work with and handle CSV Files
import csv

# Import the sys module to write the output of my code to a text file
import sys

# Initialize the variable total votes to 0 so it can be used to sum the votes from each row of our CSV File.
Total_votes = 0

# Set a variable called candidates_dup equal to a list so the candidates can be filled in there including duplicates

candidates_dup = []

# Use the line below to show the filepath to the CSV that we're going to use called 'election_data.csv'
csv_path = os.path.join('Resources', 'election_data.csv')

# The line below tells us to open the filepath to our csv and then store it as the variable called 'csv_file'.
with open(csv_path) as csv_file:
    
    # Use csv.reader method to read the opened csv file that is stored in the variable csv file 
    read_csv = csv.reader(csv_file,delimiter=',')
    
    # The next() method tells the script to move to the next csv line in the read_csv variable that stores the opened, read, and iterable csv file so we can move past the header row.
    next(read_csv)
    
    # For each row in the CSV file do this:
    for x in read_csv:
        
        # set the variable first column to equal the first colunn of the csv row that is returned. Denoted by the [0]
        first_column = x[0]
        
        # tally the row of the csv to count towards a total vote count each time the 
        Total_votes = Total_votes + 1
        
        # Append the candidate that received the vote to a list
        candidates_dup.append(x[2])
        
        
        
# create a set of unqiue candidate names        
candidates_unique = set(candidates_dup)

# store the set as a list to get a list of candidates who received a vote
candidates_final = [candidates_unique]

# sort that list in alphabetical order
#candidates_final.sort()        
        
        
print(f"Total Votes: {Total_votes}")
print(f"The candidates are {candidates_final}")


for x in candidates_final:
    print(x)
    
        
        
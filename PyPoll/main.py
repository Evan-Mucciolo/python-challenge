# Import the OS module to create filepaths across operating systems
import os

# Import the CSV module so we can work with and handle CSV Files
import csv

# Import the sys module to write the output of my code to a text file
import sys 

# Initialize the variable total votes to 0 so it can be used to sum the votes from each row of our CSV File.
Total_votes = 0

# Set a variable called candidates_dup equal to a list so the candidates can be filled in there including duplicates

candidates_dup = []

# set a dictionary to store the candidate votes along with their names

candidate_votes = {}

# Initialize the total Number of votes value for each candidate so it can be used to count each vote as needed.

candidate_votes_value = 0

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
        
        # tally the row of the csv to count towards a total vote count each time the 
        Total_votes = Total_votes + 1
        
        # Append the candidate that received the vote to a list
        candidates_dup.append(x[2])
        
        # append the candidates that received votes to a dictionary so that I can store the number of votes each candidate gets
        # Since a dictionary can't have duplicate keys, I can use this to get a unique dictionary of keys where the key is the candidate name
        # I set the default value to 0 for each person to start. If they exist already, they will not be updated. 
        candidate_votes.setdefault(x[2], 0)
        
        # This is where I get cheeky, setting a current vote tally for a given candidate equal to the current tally, by calling on the key in my candidate_votes dictionary
        # I then add one to that value, to count the current vote.
        current_candidate_tally = candidate_votes[x[2]] + 1
        
        # Then, I take the candidate tally and update my dictionary with the new tally for the next time around, so it's one higher than before. Effectively tallying the votes.
        candidate_votes[x[2]] = current_candidate_tally
        
        # Then I set the current candidate tally to 0, so it can be properly used the during the next iteration.
        current_candidate_tally = 0
                        
               
        
# create a set of unqiue candidate names        
candidates_unique = set(candidates_dup) 

# sort that set alphabetically and store it as a final ist
candidates_final = sorted(candidates_unique)    
        
# Print the results       
print("Election Results")
print("-------------------------")

# Print the total votes
print(f"Total Votes: {Total_votes}")
print("-------------------------")

# Then I must loop through my candidates and calculate their vote percentage
for x in candidates_final:
   # The vote percentage is equal to the votes the candidate received which I stored in my candidate_votes dictionary divided by the total votes
   vote_percentage = candidate_votes[x]/Total_votes
   
   # Now I'm rounding the vote percentage to report it correctly to 3 decimal places like the instructions show. The following line of code was found using chatGPT. 
   vote_percentage = round(vote_percentage * 100, 3)
   
   # Now I print my statement for each candidate showing their name, the percentage of votes they received and the total votes they received. 
   print(f"{x}: {vote_percentage}% ({candidate_votes[x]})")


# Now I exit my loop and use the candidate votes dictionary to find the winner by using the max method. 
winner_key = max(candidate_votes, key=candidate_votes.get)

# Here I print the dashes needed and the winner.
print("-------------------------")
print(f"Winner: {winner_key}")
print("-------------------------")

# Print the above output of this analysis to a text file by repeating the entire process outlined above. 
with open ("PyPoll_Text_Output.txt", 'w') as file:
    
    sys.stdout = file
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {Total_votes}")
    print("-------------------------")

    for x in candidates_final:
        vote_percentage = candidate_votes[x]/Total_votes
        vote_percentage = round(vote_percentage * 100, 3)
        print(f"{x}: {vote_percentage}% ({candidate_votes[x]})")


    winner_key = max(candidate_votes, key=candidate_votes.get)

    print("-------------------------")
    print(f"Winner: {winner_key}")
    print("-------------------------")
    
sys.stdout = sys.__stdout__
import os
# Module for reading CSV files
import csv

election_data = os.path.join('Resources', 'election_data.csv')

# Define values
VoterID = []
County = []
CanidateVote = []

# function to get unique values 
def unique(list1): 
      
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = (list(list_set)) 
    for x in unique_list: 
        print(x)
# function to get percentage
def percentage(part, whole):
      x = float(part)/float(whole)
      return "{0: .0%}".format(x)

with open(election_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
     
    csv_header = next(csvreader)
    
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        CanidateVote.append(row[2])

# Filter out list of Canidates
# print(unique(CanidateVote))

# Get Total number of votes
Total_votes = len(VoterID)

# Calculate number of votes
Khan_votes = CanidateVote.count("Khan")
Li_votes = CanidateVote.count("Li")
Correy_votes = CanidateVote.count("Correy")
OTooley_votes = CanidateVote.count("O'Tooley")

# Calculate percentage of votes
Khan_pct = percentage(Khan_votes,Total_votes)
Li_pct = percentage(Li_votes,Total_votes)
Correy_pct = percentage(Correy_votes,Total_votes)
OTooley_pct = percentage(OTooley_votes,Total_votes)

# Calculate winner
from collections import Counter  

# Count the votes for persons and stores in the dictionary 
vote_count=Counter(CanidateVote) 
  
# Find the maximum number of votes 
max_votes=max(vote_count.values()) 
  
# Search for people having maximum votes and store in a list 
tally =[i for i in vote_count.keys() if vote_count[i]==max_votes] 
  
# Sort the list and determine winner

winner = (sorted(tally)[0]) 


# Convert number of votes to string
Khan_votes = "(" + str(Khan_votes) + ")"
Li_votes = "(" + str(Li_votes) + ")"
Correy_votes = "(" + str(Correy_votes) + ")"
OTooley_votes = "(" + str(OTooley_votes) + ")"


Election_Results = {
    "Total Votes" : Total_votes,
    "Khan" : Khan_pct + " " + Khan_votes,
    "Li" : Li_pct + " " + Li_votes,
    "Correy": Correy_pct + " " + Correy_votes,
    "O'Tooley": OTooley_pct + " " + OTooley_votes,
    "Winner" : winner
}

print(Election_Results)

# Write into text file Analysis Folder
import sys

output_path = os.path.join('Analysis','election_analysis.txt')

with open(output_path, 'w') as f:
    print(Election_Results, file=f)
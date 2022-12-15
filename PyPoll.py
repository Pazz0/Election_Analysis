#Data needed to be pulled
#1 total num of votes
#2 List of candidates who got votes
#3 percentage of votes for each candidate
#4 total num of votes for ea candidate
#5 Winner of election baased on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("/Users/pazzo/Desktop/Analasys Projects Git Hub/Election_Analysis/Election_Analysis/Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("/Users/pazzo/Desktop/Analasys Projects Git Hub/Election_Analysis/Election_Analysis/analysis", "election_analysis.txt")

# 1. Init total Vote Counter
total_votes = 0

#Canidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     # Read the header row.
     headers = next(file_reader)

     # Print each row in the CSV file.
     for row in file_reader:
        #2. Add to vote count
        total_votes += 1
    
     # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add votes
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

     # Determine winning vote count and candidate
     # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
     winning_count = votes
     winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
     winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


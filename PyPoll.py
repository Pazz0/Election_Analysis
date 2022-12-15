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

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Print each row in the CSV file.
     headers = next(file_reader)
     print(headers)
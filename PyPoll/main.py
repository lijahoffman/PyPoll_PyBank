import os
import csv
# Dependencies imported. 


voters = []
candidate_full = []
candidate_short = []
candidate_dict ={}
# Empty lists and dictionary created for later code. 



py_poll_csv = os.path.join("Resources", "election_data.csv")
# CSV filepath created. 

with open(py_poll_csv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    # Opening and reading csv file. Header row skipped. 

    for row in csv_reader:
        voters.append(int(row[0]))
        candidate_full.append(row[2])
    # For loop using csv to populate lists voters (all voter ids) and candidte_full (candidates with repeats).



for i in candidate_full: 
    if candidate_short.count(i) == 0: 
        candidate_short.append(i)
    else: 
        continue
# Conditional nested withing for loop populating list candidate_short with each name in candidate_full, listed only once. 



total = len(voters)
# Defining variable for use in later code. 
winner_count = 0 
# Creating counter for use in later code. 



for i in candidate_short: 
    x = candidate_full.count(i)
    candidate_dict[i] = str(round((float(x/total) * 100), 3)) + "% (" + str(x) + ")"
    # For loop that creates variable x, defined as the number of times each candidates name (indexed using candidate_short) appears in candidate_full. 
    # Dictionary key:value pair created where the key is each candidate's name and the value is a string containing the percent of votes (rounded to 3 decimal places) and the total number of votes each candidate received. 

    if x > winner_count: 
        winner_count = x
        winner = i 
    # If count for a candite (x) is greater than the existing value of winner_count, that value is used to redefine winner_count and the associated candidate name is stored as the winner. 

    

 

output_path = os.path.join("Analysis", "election_results.txt")
# Output path created to store text file in analysis folder. 
election_results = open(output_path,"w")
# Text file created and opened for writing. 

election_results.write("Election Results" + "\n")
election_results.write("--------------------" + "\n")
election_results.write("Total Votes: " + str(total) + "\n")
election_results.write("--------------------" + "\n")
for i in candidate_dict: 
    election_results.write(i + ": " + candidate_dict[i] + "\n")
election_results.write("--------------------" + "\n")
election_results.write("Winner: " + winner + "\n")
election_results.write("--------------------" + "\n")
# Text file populated. 

election_results.close()
# Text file closed. 




print("Election Results")
print("-----------------------")
print("Total Votes: " + str(total))
print("-----------------------")

for i in candidate_dict: 
    print(i + ": " + candidate_dict[i])

print("-----------------------")
print("Winner: " + winner)
print("-----------------------")
# Results printed to terminal. 


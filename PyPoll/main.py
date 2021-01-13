#import the os module to allow us to create file paths across operating systems
import os
#module for reading CSV Files
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)
    
    #Counter for tally of total votes
    count = 0 
    #Dictionary to track unique candidates and votes tally 
    candidates_dict = {}
    #List of unique candidates
    candidates = []
    #Set initial winning count value/variable to zero
    winning_count = 0 
    
    for row in csvreader :
        #Add to vote counter to keep tally of total votes
        count = count + 1
        #set candidate value to current row column 3/index 2
        candidate = row[2]
        #if candidate is already in the unique candidates list
        if candidate in candidates:
            #Then add to their vote tally
            candidates_dict[candidate] += 1
        #otherwise add them to the candidates list and candidates dictionary with an initial vote tally of 1
        elif candidate not in candidates:
            candidates.append(row[2])
            candidates_dict[candidate] = 1
    
    #ouput path for writing to text file
    output = os.path.join("Analysis", "analysis.txt")
    txt = open(output, "w")

    #Print to terminal 
    print("Election Results")
    print("-----------------------")        
    print("Total Votes: " + str(count))
    print("-----------------------")

    #Print to text file
    txt.write("Election Results\n")
    txt.write("-----------------------\n")        
    txt.write(f"Total Votes: {count}\n")
    txt.write(f"-----------------------\n")
    
    #Find percentage of votes each candidate won:
    #make a call to the dictionary value of votes count for each candidate
    #Then divide by overall count    
    for candidate in candidates:
        percentage = round(candidates_dict[candidate] / count, 2) * 100
        #print(f"{candidate} received {candidates_dict[candidate]} votes")
        print(f"{candidate}: {percentage}% ({candidates_dict[candidate]})")
        txt.write(f"{candidate}: {percentage}% ({candidates_dict[candidate]})\n")
        #set the candidates vote count to match the value placed in the dictionary
        candidate_count = candidates_dict[candidate]
        #if the candidates vote count is greater than the current winning tally
        if (candidate_count > winning_count):
                #then set new current winning tally to the current candidate's vote tally
                winning_count = candidate_count
                winner = candidate
    #The winner of the election based on popular vote.
    print(f"Winner: {winner}")
    txt.write(f"Winner: {winner}")
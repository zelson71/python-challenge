# libraries to import
import csv
import os

# variable declaration
voter = []
cast = []
cand = []
vote = []
file_to_write = "analysis/vote_summary.txt"
# open data file
with open("Resources/election_data.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        voter.append(row[0])
        cast.append(row[2])


# get a list of distinct values of candidates in order
cand2 = list(set(cast))
cand2.sort()
# get a vote count for each candidate
for cand in cand2:
    vote.append(cast.count(cand))
print(f"Election Results\n"+"---------------------------------\n" +
      "Total Votes: {len(voter)}\n"+"---------------------------------")
for c in range(len(cand2)):
    '''
    {:.2%} Format percentage
    '''
    print(
        f"{cand2[c]}: {'{:.2%}'.format(vote[c]/len(cast))} ({vote[c]})")
print("---------------------------------\n" +
      f"Winner: {cand2[vote.index(max(vote))]}\n"+"---------------------------------")
# write to analysis file
with open(file_to_write, "w") as txt_file:
    txt_file.write(f"Election Results\n"+"---------------------------------\n" +
                   "Total Votes: {len(voter)}\n"+"---------------------------------\n")
    for c in range(len(cand2)):

        txt_file.write(
            f"{cand2[c]}: {'{:.2%}'.format(vote[c]/len(cast))} ({vote[c]})\n")
    txt_file.write("---------------------------------\n" +
                   f"Winner: {cand2[vote.index(max(vote))]}\n"+"---------------------------------")

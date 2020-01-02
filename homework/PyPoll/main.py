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

print("Election Results")
print("---------------------------------")
print(f"Total Votes: {len(voter)}")
print("---------------------------------")

# get a list of distinct values of candidates in order
cand2 = list(set(cast))
cand2.sort()
# get a vote count for each candidate
for cand in cand2:
    vote.append(cast.count(cand))

for c in range(len(cand2)):
    print(
        f"{cand2[c]}: {'{:.2%}'.format(vote[c]/len(cast))} ({vote[c]})")
print("---------------------------------")
print(f"Winner: {cand2[vote.index(max(vote))]}")
print("---------------------------------")
# write to analysis file
with open(file_to_write, "w") as txt_file:
    txt_file.write("Voter Analysis")
    txt_file.write("\n")
    txt_file.write("__________________________________")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {len(voter)}")
    txt_file.write("\n")

    for c in range(len(cand2)):
        txt_file.write(
            f"{cand2[c]}: {'{:.2%}'.format(vote[c]/len(cast))} ({vote[c]})")
        txt_file.write("\n")
    txt_file.write("__________________________________")
    txt_file.write("\n")
    txt_file.write(f"Winner: {cand2[vote.index(max(vote))]}")
    txt_file.write("\n")
    txt_file.write("__________________________________")

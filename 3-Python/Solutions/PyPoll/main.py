import csv

budget_csv = "PyPoll/CSV/election_data.csv"

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    candidateList = {}
    
    # Loop through the data
    for row in csvreader:
       
        if row[2] in candidateList:
            candidateList[row[2]].append(row[0])
        else:
            candidateList[row[2]] = [row[0]]

    # Loop through candidate list to grab the amount of entries per person
    totalBallots = 0
    for person in candidateList:
        # Store the total amount of ballots
        totalBallots += len(candidateList[person])
        
    # Store the winner
    winner = ""
    for person in candidateList:
        if winner == "":
            winner = person
        # Grab new winner if their ballots are more than the last stored winner
        elif len(candidateList[person]) > len(candidateList[winner]):
            winner = person
    
    # print the initial f'
    print(f'Election Results \n-------------------------\nTotal Votes: {totalBallots} \n-------------------------\n')

    # loop through candidates and print the f' with name percent and total
    for person in candidateList:
        pBallots = (len(candidateList[person])/totalBallots)*(100)
        pBallots = round(pBallots, 3)
        print(f'{person}: {pBallots}% ({len(candidateList[person])})')

    # print the winner
    print(f' \n-------------------------\nWinner: {winner}')

    
    
    # Create a txt file and write f' into it
    f = open("pypoll.txt", "x")
    f.write(f'Election Results \n-------------------------\nTotal Votes: {totalBallots} \n-------------------------\n')
    for person in candidateList:
        pBallots = (len(candidateList[person])/totalBallots)*(100)
        pBallots = round(pBallots, 3)
        f.write(f'{person}: {pBallots}% ({len(candidateList[person])})\n')
    f.write(f' \n-------------------------\nWinner: {winner}')
    f.close()
    # Open the txt file to read
    f = open("pypoll.txt", "r")
    print(f.read())
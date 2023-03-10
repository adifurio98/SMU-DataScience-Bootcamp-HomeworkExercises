import csv

budget_csv = "PyBank/CSV/budget_data.csv"


monthsList = []
netTotal = []
changeList = []
cmList = []
profitList = []
lossList = []
last = 0
totalChange = 0


# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
       
        # loop and grab the months and amount
        monthsList.append(row[0])
        netTotal.append(int(row[1]))

        # store the current and last values to create a change in amounts each month
        current = int(row[1])
        change = current - last
        changeList.append(change)
        cmList.append(row[0])
        
        totalChange += change

        # create two lists for profits and losses based on value of change between months
        if int(row[1]) >0:
            profitList.append(int(row[1]))
        else:
            lossList.append(int(row[1]))
        
        last = int(row[1])     


months = len(monthsList)

totalChange = totalChange - int(changeList[0])
total = sum(netTotal)

# remove first value in list because it had nothing before to compare to
changeList.pop(0)
cmList.pop(0)


average = totalChange / (months - 1)
average = round(average, 2)


maxi = max(changeList)
mini = min(changeList)
iMax = (max(range(len(changeList)), key=changeList.__getitem__))
dMax = cmList[iMax]
iMin = (min(range(len(changeList)), key=changeList.__getitem__))
dMin = cmList[iMin]

print(f'Financial Analysis \n----------------------------\nTotal Months: {months} \nTotal: ${total} \nAverage Change: ${average} \nGreatest Increase in Profits: {dMax} ${maxi} \nGreatest Decrease in Profits: {dMin} ${mini}')

# create a new file and write in f'  
f = open("pybank.txt", "x")
f.write(f'Financial Analysis \n----------------------------\nTotal Months: {months} \nTotal: ${total} \nAverage Change: ${average} \nGreatest Increase in Profits: {dMax} ${maxi} \nGreatest Decrease in Profits: {dMin} ${mini}')
f.close()

# open new file to read
f = open("pybank.txt", "r")
print(f.read())
        
        
        
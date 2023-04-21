import csv
import matplotlib.pyplot as plt 
import math

def printMenu():
        print (input("Read sales data enter 1 "))
        analyzesales()

readsalesdata = "1"
userInput = "" 

def analyzesales():
        print("analyzing")
        with open("sales - sales.csv") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the first row
        data = [float(row[1]) for row in reader]

    first_digits = [int(str(abs(d))[0]) for d in data if d != 0]
    counts = [0] * 9
    for digit in first_digits:
        counts[digit - 1] += 1
    expected_counts = [len(data) * math.log10(1 +1.0 / d) for d in range(1, 10)]
                
        fig, ax = plt.subplots()
    ax.bar(range(1, 10), counts)
    ax.plot(range(1, 10), expected_counts, 'ro--', label='Expected')
    ax.set_xlabel('First digit')
    ax.set_ylabel('Frequency')
    ax.set_title('Benford\'s Law Analysis')
    ax.legend()
        
        
plt.show()
        
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"


while userInput != exitCondition:
    printMenu()
    userInput = input();
    if userInput == readsalesdata:
                analyzesales()

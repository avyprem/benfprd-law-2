import csv


def printMenu():
        print (input("Read sales data enter 1 "))

readsalesdata = "1"
userInput = "" 

def analyzesales():
        print("analyzing")
        with open("sales - sales.csv") as file:
                reader = csv.reader(file, delimiter=",")
                list = list(reader)

                

                
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"


while userInput != exitCondition:
    printMenu()
    userInput = input();
    if userInput == readsalesdata:
                analyzesales()

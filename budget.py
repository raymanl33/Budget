import csv
import sys
import datetime


def commandlines():
    """ take commands from the command line """
    try:
        filename = sys.argv[0]
        
        return filename

    except IndexError:
        sys.exit(f'Incorect filename please try python3 budget.py')


def menu():
    """ main menu """
    print("welcome to Big Mondey Saver Budget App")
    confirmation = input(f'Would you like to edit an existing budget.CSV file or create a new budget.CSV? Existing CSV file [E], New CSV file [N]: ')
    confirm = False 
    while confirm == False:
        if confirmation.upper() == 'E':
            confirm = True

            return confirmation 
        
        elif confirmation.upper() == 'N':
            confirm = True

            return confirmation 
        else:
            print()
            print(f'"{confirmation}" is not a correct input. Please [E] to open an existing file or [N] to open a new file')
            print()
            confirmation = input(f'Would you like to edit an existing budget.CSV file or create a new budget.CSV? Existing CSV file [E], New CSV file [N]: ')
            print()



def currenttime():
    """ get the current time and return it """
    now = datetime.date.today()
    
    return now

def existingfile(time):
    """ find the existing CSV file and edit it """
    try:
        CSVfile = input(f'Please enter an existing CSV file name: ')
        with open(CSVfile, 'a') as results:
            csv_writer = csv.writer(results)
            data = []
            item = input(f'Please enter the name of the item you would like to add to {CSVfile}.CSV: ')
            cost = f'$' + input(f'Please enter the cost of the item: ')
            data.append(item)
            data.append(cost)
            data.append(time)
            csv_writer.writerow(data)

    except FileNotFoundError:
        sys.exit(f'{CSVfile} not found. Please try again!')
    

def createCSVfile():
    """ take user input to create a new csv file """
    newfile = input(f'Please enter a new CSV name')
    filename = False
    while filename == False:
        if len(newfile) <= 0:
            print (f'CSV file name needs to have at least one character or number')
            newfile = input(f'Please enter a new CSV name: ')
        elif len(newfile) > 0:
                
            data = ['Item', 'Cost', 'Date']
            with open(newfile, 'w', newline='') as results:
                csv_writer = csv.writer(results)
                csv_writer.writerow(data)
                filename = True
   


def main():
    argv = commandlines()
    confirm = menu()
    current_time = currenttime()
    if confirm.upper() == 'E':
        existingfile(current_time)
    elif confirm.upper() == 'N':
        createCSVfile()
    print (argv, csv)

main()




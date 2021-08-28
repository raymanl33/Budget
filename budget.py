import csv
import sys
import datetime
import os


def commandlines():
    """ take commands from the command line """
    try:
        filename = sys.argv[0]
        
        return filename

    except IndexError:
        sys.exit(f'Incorect filename please try python3 budget.py')


def menu():
    """ main menu """
    print("\nwelcome to Big Mondey Saver Budget App\n")
    confirmation = input(f'To create a new CSV file enter "C"\nTo read a CSV \
file enter "R"\nTo edit an existing CSV file enter "E"\nTo delete a CSV \
file enter "D": \n')
    confirm = False 
    while confirm == False:
        if confirmation.upper() == 'C' or confirmation.upper() == 'R' or confirmation.upper() == 'E' or confirmation.upper() == 'D':
            confirm = True

            return confirmation
        else:
            print()
            print(f'"{confirmation}" is not a correct input. Please re-enter the command')
            print()
            confirmation = input(f'To create a new CSV file enter "C"\nTo read a CSV \
file enter "R"\nTo edit an existing CSV file enter "E"\nTo delete a CSV \
file enter "D": \n')
            print()



def currenttime():
    """ get the current time and return it """
    now = datetime.date.today()
    
    return now

def existingCSVfile(time):
    """ find the existing CSV file and edit it """
    try:
        CSVfile = input(f'Please enter an existing CSV file name: ')
        with open(CSVfile, 'a') as results:
            csv_writer = csv.writer(results)
            data = []
            item = input(f'Please enter the name of the item you would like to \
add to {CSVfile}.CSV: ')
            cost = f'$' + input(f'Please enter the cost of the item: ')
            data.append(item)
            data.append(cost)
            data.append(time)
            csv_writer.writerow(data)

    except FileNotFoundError:
        sys.exit(f'{CSVfile} not found. Please try again!')
    

def createCSVfile():
    """ take user input to create a new csv file """
    newfile = input(f'Please enter a new CSV name: ')
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

def readCSVfile():
    """ read existing CSV file and output the result on the command screen """
    fileExist = False
    read_file = input(f'To read a CSV file, please enter an existing CSV filename: ')
    while fileExist == False:
        try:
            with open(read_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    print(*row, sep=", ")
                fileExist = True

        except FileNotFoundError:
            print(f'{read_file} not found. Please try again!')
            read_file = input(f'To read a CSV file, please enter an existing CSV filename: ')

def deleteCSVfile():
    """ delete a specific CSV file """
    filename = input(f'Please enter an existing CSV file you would like to delete: ')
    fileExist = False
    while fileExist == False:
        if(os.path.exists(filename) and os.path.isfile(filename)):
            confirmation = input(f'Are you sure you would like to delete {filename}? Yes[Y]/ No[N]: ')
            confirm = False
            fileExist = True
            while confirm == False:
                if confirmation.upper() == 'Y':
                    os.remove(filename)
                    print(f"{filename} deleted")
                    confirm = True
                elif confirmation.upper() == 'N':
                    print(f'{filename} not deleted')
                    confirm = True
                else:
                    print(f'{confirmation} is not a valid input. Please enter again.')
                    confirmation = input(f'Are you sure you would like to delete {filename}? Yes[Y]/ No[N]: ')
                    confirm = False
        else:
            print(f"{filename} file not found")
            filename = input(f'Please enter an existing CSV file you would like to delete: ')

def main():
    commandlines()
    confirm = menu()
    current_time = currenttime()
    if confirm.upper() == 'E':
        existingCSVfile(current_time)
    elif confirm.upper() == 'C':
        createCSVfile()
    elif confirm.upper() == 'R':
        readCSVfile()
    elif confirm.upper() == 'D':
        deleteCSVfile()
  
main()




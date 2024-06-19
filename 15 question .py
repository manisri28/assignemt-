import csv

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

filename = input("Enter the name of the CSV file: ")
read_csv_file(filename)

import csv

def read_csv(path):
        arr = []
        with open(path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                arr.append(row)
        return arr
import csv
filename = 'url.csv'
with open(filename,'r') as f:
    csvreader = csv.reader(f)
    fields = next(csvreader)
    for row in csvreader:
        row.append(row)
        result = csvreader.line_num
        final_result = result - 1

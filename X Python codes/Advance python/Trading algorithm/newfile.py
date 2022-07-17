import csv 
with open('NSEI.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row[1])
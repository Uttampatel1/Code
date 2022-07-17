import csv

with open("50.csv","r") as file:
	
	reader=csv.DictReader(file)
	for i in reader:
		print (i['Year'])
import csv

title = input("The : ")

with open ("netflix_titles.csv","r") as file:
	reader =csv.DictReader(file)
	count =0
	for i,row in enumerate(reader):
		if row["release_year"] == title:
			print (i+2,".",row["country"])
			count +=1
print (count)
try:
	age = int(input("Enter age or year of birth : ")) 
	
	if age in range(1,101):
		age=2021-age
		print (f"\nyou will be 100 year old in {age+100} year")
	
	elif age in range(1930,2022):
		print (f"\nyou will be 100 year old in {age+100} year")
		print ("your age this year is",2021-age)
	
	elif age > 2021 or age<0:
		print("\nyou are not yet Bron.")
	else :
		print ("\nYou seem to be the oldest person alive. ")
#	interestedYear = int(input("Enter the year you want to know your age in\n"))

#	print(f"You will be {interestedYear - age} years old in {interestedYear}")
except Exception as e:
	print ("\nplease check the input.")
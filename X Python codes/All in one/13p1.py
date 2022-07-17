name = input ("Enter your name: \n")
mark = input ("Enter your mark: \n")
phonenumber = int(input("Enter your phone number: \n"))

Template = "The name of the student is {} ,his mark are {} and phonenumber is {}"
output = Template.format(name,mark,phonenumber)
print (output)
letter=''' Dear NAME,
🥳🥳🥳
greetings for uttam coding house, I am happy to tell you selection 
You are selected !
congratulations  👏👏
Thanks and regards! 
🥳🥳🥳
date : DATE
'''

name=input ('enter your name:\n ')
date=input("enter date:\n ")
letter=letter.replace("NAME",name)
letter=letter.replace("DATE",date)
print ('\n',letter)
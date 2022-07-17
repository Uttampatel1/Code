import re

pattern = r"^gr.y$"

if re.match(pattern,"grey"):
	print ("match 1")
	
if re.match(pattern,"gray"):
	print ("match 2")

if re.match(pattern,"blue"):
	print ("match 3")

if re.match(pattern,"stringray"):
	print ("match 4")
	
'''	
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"): 	print("Match 1")

if re.search(pattern,"qwertyuiop"): 
	print("Match 2")

if re.search(pattern, "rhythmmyths"):
	00print("Match 3")'''
	
'''	
import re

pattern = r"[A-Z][a-z][0-9]"

if re.search(pattern,"LS8"):
	print ("Match 1")
if re.search(pattern,"E3"):
	print ("Match 2")
	
if re.search(pattern,"1ab"):
	print ("Match 3")
print (re.search(pattern,"1ab"))

pattern = r"egg(spam)*"

if re.match(pattern, "egg"): 		print("Match 1")

if re.match(pattern,"eggspamspamegg"):
	print("Match 2")

if re.match(pattern, "spam"):
	print("Match 3")
	'''
	

pattern = r"g+"

if re.match(pattern, "g"): 		print("Match 1")

if re.match(pattern,"gggggg"):
	print("Match 2")

if re.match(pattern, "abc"):
	print("Match 3")
	

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
	print("Match 1")

if re.match(pattern, "icecream"):
	print("Match 2")

if re.match(pattern, "sausages"):
	print("Match 3")

if re.match(pattern, "ice--ice"):
	print("Match 4")
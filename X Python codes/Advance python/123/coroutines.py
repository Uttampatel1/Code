def searcher():
	import time 
	book = "uttam is good boy and he is very  smart boy 👦"
    while True:
    	text=(yield)
    	if text in book:
    		print ("This text in the book")
    	else:
    		print ("This text in not book")
search =searcher()
next (search)
print ("start searching....")
search.send("uttam")
print ("again searching...")
search.send("hdis")
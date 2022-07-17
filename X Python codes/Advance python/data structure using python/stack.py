class Stack:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items ==[]
	def push(self,val):
		self.items.insert(0,val)
	def pop(self):
		return self.items.pop(0)
	def print_stack(self):
		print(self.items)
s = Stack()
s.push(3)	
s.push(5)
s.push(10)
s.print_stack()
s.pop()
s.print_stack()
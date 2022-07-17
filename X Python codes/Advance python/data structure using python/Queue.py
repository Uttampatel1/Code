class Queue:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items ==[]
	def enqueue(self,val):
		self.items.insert(0,val)
	def dequeue(self):
		return self.items.pop()
	def print_queue(self):
		print(self.items)

q = Queue()
q.enqueue(3)
q.enqueue(10)
q.enqueue(45)
q.enqueue(50)
q.print_queue()
q.dequeue()
q.print_queue()
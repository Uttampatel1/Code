import hashlib


class NeuralCoinBlock:
	
	def __init__(self,previous_block_hash,transition_list):
		self.previous_block_hash= previous_block_hash
		self.transition_list = transition_list
		
		self.block_data = "-".join (transition_list)+"-"+previous_block_hash 
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
		
		
t1 ="Jay sends 3.4 NC to nirav"
t2 ="bhautik sends 4 NC to jay"
t3 ="mitul sends 2.43 NC to bhano"
t4 ="nirav sends 1.5 NC to sahil"
t5 ="bhano sends 3 NC to parth"
t6 ="mihir sends 4.64 NC to bh:ano"


initial_block =NeuralCoinBlock("initial string", [t1,t2])

print (initial_block.block_data)
print (initial_block.block_hash)
print ()

second_block =NeuralCoinBlock(initial_block.block_hash, [t3,t4])

print (second_block.block_data)
print (second_block.block_hash)
print ()

third_block =NeuralCoinBlock(second_block.block_hash, [t5,t6])

print (third_block.block_data)
print (third_block.block_hash)
from time import time
from hashlib import sha512

class Block(object):

	count = 0

	def __init__(self, previousHash, transaction):
		Block.count += 1
		self.time = time()
		self.transaction = transaction
		self.blockNumber = Block.count
		self.previousHash = previousHash

	def hash(self):
		h =  sha512()
		h.update(repr(self))
		return h.hexdigest()

	def __repr__(self):
		return "%s%s%s%s" % (self.time , self.transaction, self.blockNumber, self.previousHash)

	def __str__(self):
		return "time : %s -- transaction : %s -- number : %5i --  hash : %s" % (self.time , self.transaction, self.blockNumber, self.hash())


pre = Block("", "a givs 10$ to b")
for x in range(10,30):
	print pre
	new = Block(pre.hash(), "a givs %i$ to b" % x)
	pre = new
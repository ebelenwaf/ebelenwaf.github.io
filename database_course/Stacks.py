class Stacks(Object):

	def __init__(self , size):
		self.array = [0 for i in range(size)]
		self.counter = 0	#keeps track of current size of the stack



	def push(self, value):
		if not isFull():
			self.array[counter] = value
			counter +=1
		else:
			return -1 	#can't push stack's full



	def pop(self):

		last_element = self.array[counter-1] 
		self.array[counter-1] = 0		#assume you deleted this element.
		counter-=1
		return last_element


	def isFull(self):
		if counter == (size-1):
			return True
		else:
			return False


	def isEmpty(self):
		return counter == 0


	def peek(self):
		return self.array[counter-1]


		
		
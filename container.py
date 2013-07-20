class stack(list):
	def __init__(self):
		list.__init__([])

	def push(self,val):
		self.insert(0,val)

	def pop(self):
		return super().pop(0)
class Edges:

	def __init__(self,e1,e2,weight=None,orientation=None):
		if weight!=None:
			self.weight=float(weight)
		else:
			self.weight = None

		if orientation==1:
			self.orientation = e1
		elif orientation == 2:
			self.orientation = e2
		else:
			self.orientation=None

		self.e1 = e1
		self.e2 = e2

	def getWeight(self):
		return self.weight

	def getOrientation(self):
		return self.orientation
class Edges:

	def __init__(self,v1,v2,weight=None,orientation=None):
		if weight!=None:
			self.weight=float(weight)
		else:
			self.weight = None

		if orientation==1:
			self.orientation = v1
		elif orientation == 2:
			self.orientation = v2
		else:
			self.orientation=None

		self.v1 = v1
		self.v2 = v2

	def getWeight(self):
		return self.weight

	def getOrientation(self):
		return self.orientation
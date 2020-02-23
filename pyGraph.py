from edges import Edges
from vertices import Vertices 

class Graph:
	def __init__(self,oriented=False,weighted=False):
		self.oriented = oriented
		self.weighted = weighted

		self.edges = []
		self.vertices = []

	def getNumberEdges(self):
		"""
			Get the number of edges of the Graph
		"""
		return len(self.edges)

	def getNumberVertices(self):
		"""
			Get the number of vertices of the Graph
		"""
		return len(self.vertices)

	def getEdges(self,name=True):
		"""
			Return all the names of the edges

			Optinal parameters:
			name : if True will return names, else return objects
		"""
		if name == True:
			return [e.getName() for e in self.edges]
		else:
			return self.edges

	def getVertices(self,name=True,get_object=False):
		"""
			Return all the vertices

			Optinal parameters:
			name : if True will return names of the edge, else return objects
			get_object : if True, return the content of vertices, else return objects
		"""
		out = []
		for v in self.vertices:
			add = {}
			if get_object:
				add = v
			else:
				if name==False:
					add["e1"] = v.e1.getName()
					add["e2"] = v.e2.getName()
				else:
					add["e1"] = v.e1
					add["e2"] = v.e2
				if v.getWeight()!=None:
					add["weight"] = v.getWeight()
				if v.getorientation()!=None:
					add["orientation"] = v.georientation()
			out.append(add)
		return out

	def existingVertices(self,e1,e2):
		"""
			Test if a vertice exist in the Graph by giving the name of the edges
		"""
		list_vertices = self.getVertices()
		for element in list_vertices:
			if element["e1"]==e1 and element["e2"]==e2:
				return True
		return False

	def addEdges(self,list_edges=[]):
		"""
			Add new Edges in the Graph if names are not used
			
			Optional parameters:
			list_edges : a list of names for new edges
		"""
		existing_edges = self.getEdges()
		for edge in list_edges:
			if type(edge) == str:
				if not(edge in existing_edges):
					newEdge = Edges(edge)
					self.edges.append(newEdge)
				else:
					print("Error : "+edge+" already exists.")
			else:
				print("Error : "+edge+" must be a String.")
			

	def addVertices(self,e1,e2,weight=None,orientation=None):
		"""
			Add a new vertices in the Graph

			Required parameters :
			e1 : the first edge
			e2 : the second edge

			Optional parameters :
			weight : if weighted graph, must add a weight (default : None)
			orientation : if oriented graph, must add an orientation (default : None)
		"""
		existing_edges = self.getEdges()
		if e1 in existing_edges and e2 in existing_edges:
			if not self.existingVertices(e1,e2):
				if not self.weighted:
					weight=None
				else:
					if weight==None:
						print("Error : Weighted graph, must add a weight.")
						return -1
				if not self.oriented:
					orientation=None
				else:
					if orientation==None:
						print("Error : Oriented Graph, must add an orientation.")
						return -1
				new_vertices = Vertices(e1,e2,weight,orientation)
				self.vertices.append(new_vertices)
			else:
				print("Error : ["+e1+","+e2+"]"+" already exists.")
		else:
			print("Error : "+e1+" or "+e2+" doesn't exist.")

	def getDegre(self,edge):
		"""
			Get the degre of a specific edge

			Required parameter :
			edge : the name of the edge
		"""
		count = 0
		vertices = self.getVertices()
		for ele in vertices:
			if ele["e1"]==edge or ele["e2"]==edge:
				count+=1
		return count

	def getOrientedDegre(self,edge):
		"""
			Get the input degre and the output degre of a specific edge
			
			Required parameter :
			edge : the name of the edge
		"""
		if self.oriented==False:
			return None
		count_in = 0
		count_out = 0

		vertices = self.getVertices()
		for ele in vertices:
			if ele["e1"]==edge or ele["e2"]==edge:
				if ele["orientation"] == edge:
					count_in+=1
				else:
					count_out+=1
		return count_in,count_out
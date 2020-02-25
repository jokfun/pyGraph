
from edges import Edges
from vertices import Vertices 

class Graph:
	def __init__(self,oriented=False,weighted=False):
		self.oriented = oriented
		self.weighted = weighted

		self.vertices = []
		self.edges = []

	def getNumberVertices(self):
		"""
			Get the number of vertices of the Graph
		"""
		return len(self.vertices)

	def getNumberEdges(self):
		"""
			Get the number of edges of the Graph
		"""
		return len(self.edges)

	def getVertices(self,name=True):
		"""
			Return all the names of the vertices

			Optinal parameters:
			name : if True will return names, else return objects
		"""
		if name == True:
			return [e.getName() for e in self.vertices]
		else:
			return self.vertices

	def getEdges(self,name=True,get_object=False):
		"""
			Return all the edges

			Optinal parameters:
			name : if True will return names of the edge, else return objects
			get_object : if True, return the content of edges, else return objects
		"""
		out = []
		for v in self.edges:
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
				if self.weighted:
					add["weight"] = v.getWeight()
				if self.oriented:
					add["orientation"] = v.getOrientation()
			out.append(add)
		return out

	def existingEdges(self,e1,e2):
		"""
			Test if a vertice_ exist in the Graph by giving the name of the vertices
		"""
		list_edges = self.getEdges()
		for element in list_edges:
			if element["e1"]==e1 and element["e2"]==e2:
				return True
		return False

	def addVertices(self,list_vertices=[]):
		"""
			Add new vertices in the Graph if names are not used
			
			Optional parameters:
			list_vertices : a list of names for new vertices
		"""
		existing_vertices = self.getVertices()
		for vertices in list_vertices:
			if type(vertices) == str:
				if not(vertices in existing_vertices):
					newVertice = Vertices(vertices)
					self.vertices.append(newVertice)
				else:
					print("Error : "+vertices+" already exists.")
			else:
				print("Error : "+vertices+" must be a String.")
			

	def addEdges(self,e1,e2,weight=None,orientation=None):
		"""
			Add a new edges in the Graph

			Required parameters :
			e1 : the first edge
			e2 : the second edge

			Optional parameters :
			weight : if weighted graph, must add a weight (default : None)
			orientation : if oriented graph, must add an orientation (default : None)
		"""
		existing_vertices = self.getVertices()
		if e1 in existing_vertices and e2 in existing_vertices:
			if not self.existingEdges(e1,e2):
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
				new_edges = Edges(e1,e2,weight,orientation)
				self.edges.append(new_edges)
			else:
				print("Error : ["+e1+","+e2+"]"+" already exists.")
		else:
			print("Error : "+e1+" or "+e2+" doesn't exist.")

	def getDegree(self,vertice):
		"""
			Get the degree of a specific vertice

			Required parameter :
			vertices : the name of the vertice
		"""
		count = 0
		edges = self.getEdges()
		for edge in edges:
			if edge["e1"]==vertice or edge["e2"]==vertice:
				count+=1
		return count

	def getOrientedDegree(self,vertice):
		"""
			Get the input degree and the output degree of a specific edge
			
			Required parameter :
			vertice : the name of the vertice
		"""
		if self.oriented==False:
			return None
		count_in = 0
		count_out = 0

		edges = self.getedges()
		for edge in edges:
			if edge["e1"]==vertice or edge["e2"]==vertice:
				if edge["orientation"] == vertice:
					count_in+=1
				else:
					count_out+=1
		return count_in,count_out
import math
import treeFunctions as tfun
import externTools as ext

def shortestPath(graph,source,target=None):
	"""
		Function to calculate the shortest path
		Uses the Dijkstra algorithm.
		If no target vertex is specified, will return the shortest path 
			from the source to each target vertex.

		Required parameters :
		graph : a graph built with the object Graph
		source : the start of the path

		Optional parameters :
		target : the last vertex of the path and only focus
	"""
	all_vertices = graph.getVertices()
	all_distance = graph.getAllDistances()

	if not (source in all_vertices):
		print("Error : Source vertex must be in the Graph.")
		return None
	if target!= None and not (target in all_vertices):
		print("Error : Target vertex must be in the Graph.")
		return None

	dist = {}
	previous = {}
	for vertex in all_vertices:
		dist[vertex] = math.inf
		previous[vertex] = None
	dist[source] = 0

	while len(all_vertices) > 0:

		#Take all the distance of dist depending on the last vertices
		cop_dist = {e:dist[e] for e in all_vertices}
		#The key of the min value in the cop_dist dictionary
		vertex = min(cop_dist, key=cop_dist.get)
		#Remove the vertex of the possible list
		all_vertices = [e for e in all_vertices if e != vertex]

		if target!=None and target==vertex:
			break

		neighbors = graph.getNeighbors(vertex)
		for neighbor in neighbors:
			alt = dist[vertex] + all_distance[vertex+","+neighbor]
			if alt < dist[neighbor]:
				dist[neighbor] = alt
				previous[neighbor] = vertex

	#If there's a target, will return the path of it and the distance
	if target!=None:
		path = []
		edge = target
		if edge in previous or edge == source:
			while edge in previous :
				path.insert(0,edge)
				edge = previous[edge]
		return dist[target],path
	else:
		return dist,previous

def isConnected(graph):
	"""
		Test if a graph is fully connected 
			-> Each vertex has a path to any other vertex

		Required parameters:
		graph : a Graph oject
	"""
	all_vertices = graph.getVertices()
	root = all_vertices[0]
	cop_all_vertices = all_vertices[1:]
	tree = tfun.buildTree(root,graph,cop_all_vertices)
	count_nodes = tfun.countNodes(tree)
	if count_nodes == len(all_vertices):
		return True 
	else:
		return False

def findHamiltonian(graph,root,node,last_vertices,path,cycle):
	"""
		-- Recursive method --
		Find a hamitonian path from the root

		Required paramters :
		root : the start of the path
		node : the actual position of the search
		last_vertices : last possible vertices you can explore
		path : the built path
		cycle : if you want to build a hamiltonian cycle
	"""
	if len(last_vertices)==0:
		if cycle==True:
			if root in graph.getNeighbors(node):
				return True,path+[node,root]
			else:
				return False,None
		else:
			return True,path+[node]
	path+=[node]
	neighbors = [neighbor for neighbor in graph.getNeighbors(node) if neighbor in last_vertices]

	if len(neighbors)==0:
		return False,None

	for neighbor in neighbors:
		vertices = last_vertices.copy()
		vertices.remove(neighbor)
		return findHamiltonian(graph,root,neighbor,vertices,path,cycle)


def hamiltonian(graph,cycle=False):
	"""
		Compute a hamiltonian path of a graph
		If no path is found, will return an empty list

		Required parameters :
		graph : a Graph object

		Optional parameters :
		cycle : if you want to return a hamiltonian cycle
	"""
	if graph.getNumberVertices() > 2:
		list_vertices = graph.getVertices()
		vertex = list_vertices[0]
		copy_vertices = list_vertices.copy()
		copy_vertices.remove(vertex)
		result,path = findHamiltonian(graph,vertex,vertex,copy_vertices,[],cycle)
		if result == True:
			return path
		else:
			return []
	else:
		print("Error : hamiltonian algorithm with a number of vertex > 2.")
		return []



def buildTree(root, graph, vertices):
	"""
		-- Recursive method --
		Build a tree with a specific graph

		Required Arguments : 
		root : the root the of the tree
		graph : a Graph object
		vertices : the list of vertices of the graph
	"""
	if len(vertices)==0:
		return None
	else:
		neighbors = graph.getNeighbors(root)
		neighbors = [e for e in neighbors if e in vertices]
		result = [root]
		for neighbor in neighbors:
			cop_vertices = vertices.copy()
			cop_vertices = [e for e in cop_vertices if e!=neighbor]
			new = buildTree(neighbor,graph,cop_vertices)
			if new !=None:
				result.append(new)
	return result

def countNodes(tree):
	"""
		-- Recursive method --
		Count the number of nodes of a tree

		Required Arguments :
		tree : a tree -_-
	"""
	if len(tree)==0:
		return 1
	else:
		result = 1 #The root
		for i in range(1,len(tree)):
			result+=countNodes(tree[i])
		return result

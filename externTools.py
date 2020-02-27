"""
	Functions inside this file are not made to be called by the user
"""

def toDic(list_edges,oriented=False):
	"""
		Convert the edges of a Graph into a dictionnary

		Required Arguments :
		list_edges : a list of edges built with Graph object

		Optionnal arguments :
		oriented : boolean of the orientation of the edges
	"""
	dic_result = {}
	for edge in list_edges:
		if oriented:
			name = edge["v1"] + "," + edge["v2"]
			dic_result[name] = True
		else:
			name = edge["v1"] + "," + edge["v2"]
			dic_result[name] = True
			name = edge["v2"] + "," + edge["v1"]
			dic_result[name] = True
	return dic_result

def inDic(v1,v2,dic,oriented=False):
	"""
		Test if an edge between 2 vertices exist in a, edges' dic

		Required Arguments :
		v1 : the first vertex
		v2 : he econd vertex
		dic : the edges' dic

		Optionnal arguments :
		oriented : boolean of the orientation of the edges
	"""
	if oriented:
		name = v1 + "," + v2
		cond = True if name in dic else False
		return cond
	else:
		name1 = v1 + "," + v2
		name1 = v2 + "," + v1
		cond = True if (name1 in dic or name2 in dic) else False
		return cond

def delEDic(v1,v2,dic,oriented=False):
	"""
		Remove the edge built with v1 and v2 in dic

		Required Arguments :
		v1 : the first vertex
		v2 : he econd vertex
		dic : the edges' dic

		Optionnal arguments :
		oriented : boolean of the orientation of the edges
	"""
	name = v1 + "," + v2
	del dic[name]
	if not oriented:
		name = v2 + "," + v1
		del dic[name]
	return dic
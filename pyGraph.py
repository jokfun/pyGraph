
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
            Return all the names of vertices

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
                    add["v1"] = v.v1.getName()
                    add["v2"] = v.v2.getName()
                else:
                    add["v1"] = v.v1
                    add["v2"] = v.v2
                if self.weighted:
                    add["weight"] = v.getWeight()
                if self.oriented:
                    add["orientation"] = v.getOrientation()
            out.append(add)
        return out

    def existingEdges(self,v1,v2):
        """
            Test if a vertice_ exist in the Graph by giving the name of the vertices
        """
        list_edges = self.getEdges()
        for element in list_edges:
            if element["v1"]==v1 and element["v2"]==v2:
                return True
        return False

    def addVertices(self,list_vertices=[]):
        """
            Add new vertices in the Graph if names are not used
            
            Optional parameters:
            list_vertices : a list of names for new vertices
        """
        existing_vertices = self.getVertices()
        for vertex in list_vertices:
            if type(vertex) == str:
                if not(vertex in existing_vertices):
                    newVertex = Vertices(vertex)
                    self.vertices.append(newVertex)
                else:
                    print("Error : "+vertex+" already exists.")
            else:
                print("Error : "+vertex+" must be a String.")
            

    def addEdges(self,v1,v2,weight=None,orientation=None):
        """
            Add a new edges in the Graph

            Required parameters :
            v1 : the first edge
            v2 : the second edge

            Optional parameters :
            weight : if weighted graph, must add a weight (default : None)
            orientation : if oriented graph, must add an orientation (default : None)
        """
        existing_vertices = self.getVertices()
        if v1 in existing_vertices and v2 in existing_vertices:
            if not self.existingEdges(v1,v2):
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
                new_edges = Edges(v1,v2,weight,orientation)
                self.edges.append(new_edges)
            else:
                print("Error : ["+v1+","+v2+"]"+" already exists.")
        else:
            print("Error : "+v1+" or "+v2+" doesn't exist.")

    def removeVertex(self,vertex):
        """
            Remove a specific vertex of the graph and all edges containing this vertex

            Required paramters:
            vertex : the vertex you want to remove
        """
        self.removeEdge(vertex)
        pos = self.getVertices().index(vertex)
        self.vertices = self.vertices[:pos] + self.vertices[pos+1:]


    def removeEdge(self,v1,v2=None):
        """
            Remove edges containg specific vertex

            Required parameters:
            v1 : a vertex, if an edge contains v1 it'll be remove

            Optional parameters:
            v2 : a vertex (default None), remove all the edges connecting v1 and v2
        """
        all_edges = self.getEdges()
        remove_list = []
        for i in range(len(all_edges)):
            edge = all_edges[i]
            if v2==None:
                if edge["v1"]==v1 or edge["v2"]==v1:
                    remove_list.append(i)
            else:
                if (edge["v1"]==v1 and edge["v2"]==v2) or (edge["v1"]==v2 and edge["v2"]==v1):
                    remove_list.append(i)
        self.edges = [self.edges[i] for i in range(len(self.edges)) if not(i in remove_list)]

    def getDegree(self,vertex):
        """
            Get the degree of a specific vertex

            Required parameter :
            vertices : the name of the vertex
        """
        count = 0
        edges = self.getEdges()
        for edge in edges:
            if edge["v1"]==vertex or edge["v2"]==vertex:
                count+=1
        return count

    def getOrientedDegree(self,vertex):
        """
            Get the input degree and the output degree of a specific edge
            
            Required parameter :
            vertex : the name of the vertex
        """
        if self.oriented==False:
            return None
        count_in = 0
        count_out = 0

        edges = self.getedges()
        for edge in edges:
            if edge["v1"]==vertex or edge["v2"]==vertex:
                if edge["orientation"] == vertex:
                    count_in+=1
                else:
                    count_out+=1
        return count_in,count_out

    def getNeighbors(self,vertex):
        """
            Get the neighbors of a specific vertex

            Required parameters :
            vertex : the vertex you want to get the neighbor of
        """
        all_vertices = self.getVertices()
        if not (vertex in all_vertices):
            print("Error : {} not in vertices".format(vertex))
            return None
        result = []
        all_edges = self.getEdges()
        for edge in all_edges:
            if edge["v1"] == vertex:
                if not self.oriented:
                    result.append(edge["v2"])
                elif self.oriented and edge["orientation"]!=verte:
                    result.append(edge["v2"])
            if edge["v2"] == vertex:
                if not self.oriented:
                    result.append(edge["v1"])
                elif self.oriented and edge["orientation"]!=verte:
                    result.append(edge["v1"])
        return result

    def getAllDistances(self):
        """
            Get all the distance of the graph in a dic
        """
        result = {}
        all_edges = self.getEdges()
        for edge in all_edges:
            if self.oriented:
                if edge["orientation"] == edge["v1"]:
                    edge["v2"] + "," + edge["v1"]
                else : 
                    edge["v1"] + "," + edge["v2"]
                if self.weighted:
                    result[name] = edge["weight"]
                else:
                    result[name] = 1
            else:
                namv1 = edge["v1"] + "," + edge["v2"]
                namv2 = edge["v2"] + "," + edge["v1"]
                if self.weighted:
                    result[namv1] = edge["weight"]
                    result[namv2] = edge["weight"]
                else:
                    result[namv1] = 1
                    result[namv2] = 1
        return result

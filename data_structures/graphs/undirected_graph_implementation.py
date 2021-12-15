"""
Graphs are data structure which contains nodes or vertices and the connection between them.
LinkedList or Trees are basically graphs having nodes and connection between the nodes
Graphs are of 3 types:
    - cyclic/Acyclic Graphs
    - weighted / unweighted graphs
    - directed / undirected graphs
A graph can be represented in 3 ways:
    - Adjacency list: stores the nodes with which a particular node is connected in a linkedlist or array.
                    All these lists or arrays can be stored in a hash table(dict in python) with the keys being
                    the nodes and the values being their respective lists
                    {0: [0,1,2] }
    - Adjacency matrix: it is a nXn matrix with n is the number of nodes. M[i][j] = 1 if nodes i and j are connected
                        else 0
    - Edge list: contains all the pair of nodes which are connected to each other. If the graph is weighted then it
                will contain their weight as well
In this example, we will be using Adjacency list to build Graphs
"""


class Graph:

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self, node):
        if node not in self.adjacency_list:
            self.number_of_nodes += 1
            self.adjacency_list[node] = []

    def add_edge(self, vertex1, vertex2):

        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            print(f"Edge between {vertex1} and {vertex2} already exits!")

    def print_graph(self):
        for item in self.adjacency_list:
            # print(f"{item[0]} --> {item[1]}")
            print(f"{item} -->> {' '.join(map(str, self.adjacency_list[item]))}")


mygraph = Graph()
mygraph.add_vertex('0')
mygraph.add_vertex('1')
mygraph.add_vertex('2')
mygraph.add_vertex('3')
mygraph.add_vertex('4')
mygraph.add_vertex('5')
mygraph.add_vertex('6')

mygraph.add_edge('0', '2')
mygraph.add_edge('1', '0')
mygraph.add_edge('1', '3')
mygraph.add_edge('1', '2')
mygraph.add_edge('2', '4')
mygraph.add_edge('3', '4')
mygraph.add_edge('5', '4')
mygraph.add_edge('5', '6')

mygraph.add_edge('5', '6')
mygraph.add_vertex('6')
mygraph.add_vertex('6')
mygraph.add_vertex('5')

mygraph.print_graph()

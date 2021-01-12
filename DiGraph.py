from GraphInterface import GraphInterface
from NodeData import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        """
        The constructor for object DiGraph
        """
        self.nodes = {}
        self.NumOfEdges = 0
        self.ModeCount = 0

    def getNode(self, key):
        """
        returns the node_data by the key.
        """
        if key not in self.nodes:
            return None
        else:
            return self.nodes[key]

    def getEdge(self, src, dest):
        """
        returns the data of the edge (src,dest), null if none.
        Note: this method should run in O(1) time.
        """
        if src in self.nodes:
            return self.nodes[src].getNiEdge(dest)
        else:
            return None

    def addNode(self, n):
        """
        adds a new node to the graph with the given node_data.
        """
        if n.getKey() not in self.nodes:
            self.nodes[n.getKey()] = n
            self.ModeCount += 1

    def add_node(self, node_id, pos=None):
        """
        adds a node to the graph with id 'node_id'
        """
        n = NodeData(node_id, pos)
        self.addNode(n)

    def hasEdge(self, src, dest):
        """
        return true iff (if and only if) there is an edge between src and dest
        Note: this method should run in O(1) time
        """
        if src in self.nodes:
            return self.nodes[src].hasNi_out(dest)
        else:
            return False

    def add_edge(self, id1, id2, weight):
        """
        Connects an edge with weight 'weight' between node id1 to node id2.
        Note: this method should run in O(1) time.
        """
        if not self.hasEdge(id1, id2) and id1 != id2:
            self.nodes[id1].addNi_out(id2, weight)
            self.nodes[id2].addNi_in(id1)
            self.NumOfEdges += 1
            self.ModeCount += 1

    def getV(self):
        """
        This method returns a pointer (shallow copy) for the
        collection representing all the nodes in the graph.
        Note: this method should run in O(1) time.
        """
        return self.nodes.values()

    def get_all_v(self):
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
        """
        return self.nodes

    def get_all_e(self):
        s = set()
        for v in self.nodes.values():
            for e in v.getNi_out():
                s.add(e)
            for e in v.getNi_in():
                s.add(self.getEdge(e, v.getKey()))
        return list(s)

    def all_in_edges_of_node(self, id1):
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
        """
        if id1 in self.nodes:
            connected_nodes = {}
            in_edges = self.nodes[id1].getNi_in()
            for i in in_edges:
                connected_nodes[i] = self.getEdge(i, id1).getWeight()
            return connected_nodes
        else:
            return {}

    def all_out_edges_of_node(self, id1):
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 in self.nodes:
            connected_nodes = {}
            out_edges = self.nodes[id1].getNi_out()
            for edge in out_edges:
                connected_nodes[edge.getDest()] = edge.getWeight()
            return connected_nodes
        else:
            return {}

    def getE(self, node_id):
        """
        This method returns a pointer (shallow copy) for the
        collection representing all the edges getting out of
        the given node (all the edges starting (source) at the given node).
        Note: this method should run in O(k) time, k being the collection size.
        """
        if node_id in self.nodes:
            return self.nodes[node_id].getNi_out()
        else:
            return {}

    def remove_node(self, key):
        """
        Deletes the node (with the given ID) from the graph -
        and removes all edges which starts or ends at this node.
        This method should run in O(k), V.degree=k, as all the edges should be removed.
        """
        if self.getNode(key) is not None:
            in_edges = self.nodes[key].getNi_in()
            for i in in_edges:
                self.nodes[i].removeEdge_out(key)
                self.NumOfEdges -= 1
                self.ModeCount += 1
            del self.nodes[key]
            return True
        else:
            return False

    def remove_edge(self, node_id1, node_id2):
        """
        Deletes the edge from the graph.
        Note: this method should run in O(1) time.
        """
        if self.hasEdge(node_id1, node_id2):
            e = self.nodes[node_id1].removeEdge_out(node_id2)
            self.nodes[node_id2].removeEdge_in(node_id1)
            self.NumOfEdges -= 1
            self.ModeCount += 1
            return e
        else:
            return None

    def v_size(self):
        """
        Returns the number of vertices (nodes) in the graph.
        Note: this method should run in O(1) time.
        """
        return len(self.nodes)

    def e_size(self):
        """
        Returns the number of edges (assume directional graph).
        Note: this method should run in O(1) time.
        """
        return self.NumOfEdges

    def get_mc(self):
        """
        Returns the Mode Count - for testing changes in the graph.
        """
        return self.ModeCount

    def __eq__(self, other):
        """
        equals function - return true if the two object are equals.
        else, return false.
         """
        if len(self.nodes) != len(other.getV()):
            return False
        for i in self.nodes:
            if other.getNode(i) is None:
                return False
            if other.getNode(i) != self.nodes[i]:
                return False
        return True


    def __repr__(self):
        """
        Returns a string representing the directed graph
        """
        s = "-----\nDiGraph: \nNodes: (Total of " + str(self.v_size()) + " nodes.\n"
        for n in self.nodes.values():
            s += str(n.getKey()) + ', '
        s += "\nEdges: (Total of " + str(self.e_size()) + " edges.\n"
        for e in self.get_all_e():
            s += "edge src: " + str(e.getSrc()) + ", dest: " + str(e.getDest()) + ", w: " + str(e.getWeight()) + '\n'
        s += "Num of MC: " + str(self.ModeCount) + "\n-----"
        return s



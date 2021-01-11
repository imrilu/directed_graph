from EdgeData import EdgeData


class NodeData:

    def __init__(self, key, gl=None, tag=None, info=None, weight=None):
        """
        the constructor for object NodeData
        """
        self.key = key
        self.gl = gl
        self.tag = tag
        self.info = info
        self.weight = weight
        self.out_edges = {}
        self.in_edges = []

    def getNi_out(self):
        """
        This method returns a collection with all the out edges of this node_data
        """
        return self.out_edges.values()

    def getNi_in(self):
        """
        This method returns a HashSet with all the in edges of this node_data
        """
        return self.in_edges

    def getNiEdge(self, dest):
        """
        This method returns a specific edge of this node_data
        """
        if dest in self.out_edges:
            return self.out_edges[dest]
        return None

    def addNi_out(self, dest, w):
        """
        This method adds the out_edge to this node_data
        """
        edge = EdgeData(self.key, dest, w)
        self.out_edges[dest] = edge

    def addNi_in(self, src):
        """
        This method adds the in_edge to this node_data
        """
        if src not in self.in_edges:
            self.in_edges.append(src)

    def hasNi_out(self, dest):
        """
        return true iff this<==>key are adjacent, as an edge between them.
        """
        if self.out_edges and dest in self.out_edges:
            return True
        else:
            return False

    def removeEdge_out(self, key):
        """
        Removes the out-edge with the key - 'key'
        """
        if key in self.out_edges:
            e = self.out_edges[key]
            del self.out_edges[key]
            return e
        else:
            return None

    def removeEdge_in(self, key):
        """
        Removes the in-edge with the key - 'key'.
        """
        if key in self.in_edges:
            self.in_edges.remove(key)

    def getKey(self):
        """
        Returns the key (id) associated with this node.
        """
        return self.key

    def getLocation(self):
        """
        Returns the location of this node, if
        none return null.
        """
        return self.gl

    def setLocation(self, p):
        """
        Allows changing this node's location.
        """
        self.gl = p

    def getWeight(self):
        """
        Returns the weight associated with this node.
        """
        return self.weight

    def setWeight(self, w):
        """
        Allows changing this node's weight.
        """
        self.weight = w

    def getInfo(self):
        """
        Returns the remark (meta data) associated with this node.
        """
        return self.info

    def setInfo(self, s):
        """
        Allows changing the remark (meta data) associated with this node.
        """
        self.info = s

    def getTag(self):
        """
        Temporal data (aka color: e,g, white, gray, black)
        which can be used be algorithms
        """
        return self.tag

    def setTag(self, t):
        """
        Allows setting the "tag" value for temporal marking an node - common
        practice for marking by algorithms.
        """
        self.tag = t

    def __eq__(self, other):
        """
        equals function - return true if the two object are equals.
        else, return false.
        """
        if self.key != other.getKey():
            return False
        for i in self.out_edges:
            if not other.hasNi_out(i):
                return False
        return True


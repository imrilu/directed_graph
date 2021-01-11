

class EdgeData:

    def __init__(self, src, dest, weight, info=None, tag=None):
        """
        constructor for object EdgeData
        """
        self.src = src
        self.dest = dest
        self.weight = weight
        self.info = info
        self.tag = tag

    def getSrc(self):
        """
        return the id of the source node of this edge
        """
        return self.src

    def getDest(self):
        """
        return the id of the destination node of this edge
        """
        return self.dest

    def getWeight(self):
        """
        return the weight of this edge (positive value).
        """
        return self.weight

    def getInfo(self):
        """
        return the remark (meta data) associated with this edge
        """
        return self.info

    def getTag(self):
        """
        which can be used in algorithms
        temporal data (aka color: white, gray, black)
        """
        return self.tag

    def setInfo(self, info):
        """
        Allows changing the remark (meta data) associated with this edge.
        """
        self.info = info

    def setTag(self, tag):
        """
        this method allows setting the tag value for temporal marking an edge -
        common practice for marking by algorithms.
        """
        self.tag = tag
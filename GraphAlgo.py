import json
import os
import matplotlib.pyplot as plt
from numpy import random
from pathlib import Path
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=None):
        """
        constructor for GraphAlgo class
        """
        if g is None:
            self.dwg_alg = DiGraph()
        else:
            self.dwg_alg = g
        self.d1 = {}
        self.p1 = {}

    def init(self, g):
        """
        init function for class GraphAlgo
        """
        self.dwg_alg = g

    def get_graph(self):
        """
        returns the directed graph on which the algorithm works on
        """
        return self.dwg_alg

    def parse_path(self, file_name):
        """
        a helper function to parse the file absolute path
        """
        file_name = file_name.replace('/', '\\')
        file_name = file_name.replace('\\\\', '\\')
        file_name = file_name.split('\\')
        base_path = Path(__file__).parent
        file_path = ""
        for i in range(len(file_name) - 1):
            if file_name[i].startswith(".."):
                continue
            file_path += file_name[i] + '/'
        file_path += file_name[len(file_name) - 1]

        return (base_path / file_path).resolve()

    def load_from_json(self, file_name):
        """
        Loads a graph from a json file.
        """
        file_path = self.parse_path(file_name)
        with open(file_path, 'r') as fp:
            data = json.load(fp)
            nodes_list = data["Nodes"]
            edges_list = data["Edges"]

        for n in nodes_list:
            if "pos" in n:
                p = n["pos"].split(',')
                pos = (float(p[0]), float(p[1]))
            else:
                pos = None
            self.dwg_alg.add_node(n["id"], pos)
        for edge in edges_list:
            self.dwg_alg.add_edge(edge["src"], edge["dest"], edge["w"])
        return True

    def save_to_json(self, file_name):
        """
        saves the graph in JSON format to a file
        """
        file_path = self.parse_path(file_name)
        nodes = self.dwg_alg.getV()
        edges = self.dwg_alg.get_all_e()
        nodes_parsed = []
        edges_parsed = []
        for v in nodes:
            if v.getLocation() is not None:
                temp_node = {'id': v.getKey(), 'pos': v.getLocation()}
            else:
                temp_node = {'id': v.getKey()}
            nodes_parsed.append(temp_node)
        for e in edges:
            if e.getWeight() is not None:
                temp_edge = {'src': e.getSrc(), 'dest': e.getDest(), 'w': e.getWeight()}
            else:
                temp_edge = {'src': e.getSrc(), 'dest': e.getDest()}
            edges_parsed.append(temp_edge)
        file = {'Nodes': nodes_parsed, 'Edges': edges_parsed}

        try:
            os.remove(file_path)
        except OSError:
            pass
        with open(file_path, 'x') as fp:
            json.dump(file, fp)
            return True

    def connected_components(self):
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        """
        nodes = list(self.dwg_alg.get_all_v().keys())
        SCC = []
        while nodes:
            component = self.connected_component(nodes[0])
            SCC.append(component)
            for n in component:
                nodes.remove(n)
        return SCC

    def connected_component(self, id1):
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        """
        node = self.dwg_alg.getNode(id1)
        if node is not None:
            self.Dijkstra(node)
            component = set()
            component.add(id1)
            reachable = []
            for n in self.d1:
                if self.d1[n] < float('inf'):
                    reachable.append(n)
            for n in reachable:
                if self.shortest_path_dist(n, id1) < float('inf'):
                    component.add(n)
            return list(component)

    def Dijkstra(self, s):
        """
        implementation of the dijkstra algorithm
        """
        self.d1 = {}
        self.p1 = {}
        visited = set()
        q = []
        for n in self.dwg_alg.getV():
            self.d1[n.getKey()] = float('inf')
            self.p1[n.getKey()] = None
        self.d1[s.getKey()] = float(0)
        q.append(self.Node(s.getKey(), 0))
        while len(visited) != self.dwg_alg.v_size() and len(q) > 0:
            key = q.pop(0).getKey()
            if key not in visited:
                for v in self.dwg_alg.getE(key):
                    if v.getDest() not in visited:
                        sumDest = self.d1[key] + self.dwg_alg.getEdge(key, v.getDest()).getWeight()
                        if sumDest < self.d1[v.getDest()]:
                            self.d1[v.getDest()] = sumDest
                            self.p1[v.getDest()] = self.dwg_alg.getNode(key)
                        q.append(self.Node(v.getDest(), self.d1[v.getDest()]))
                        sorted(q, key=self.Node.getDistance)
            visited.add(key)


    def shortest_path_dist(self, id1, id2):
        """
        helper function to get the distance of the shortest path between id1 and id2
        """
        self.Dijkstra(self.dwg_alg.getNode(id1))
        return self.d1[id2]

    def shortest_path(self, id1, id2):
        """
        a function to return a list of the shortest path between id1 and id2
        """
        self.Dijkstra(self.dwg_alg.getNode(id1))
        s = self.dwg_alg.getNode(id2)
        l = []
        while s is not None:
            l.append(s)
            s = self.p1[s.getKey()]
        l.reverse()
        return self.d1[id2], l

    def get_graph_lims(self):
        """
        a helper function for the plot graph func. will calculate the borders of the graph to be plotted
        """
        nodes = self.dwg_alg.get_all_v()
        xmin, xmax = float('inf'),float('-inf')
        ymin, ymax = float('inf'),float('-inf')
        for n in nodes.values():
            if n.getLocation() is not None:
                x,y = n.getLocation()
                if x < xmin:
                    xmin = x
                if x > xmax:
                    xmax = x
                if y < ymin:
                    ymin = y
                if y > ymax:
                    ymax = y
        if xmax == float('-inf'):
            xmax = 1
        if ymax == float('-inf'):
            ymax = 1
        if ymin == float('inf'):
            ymin = -1
        if xmin == float('inf'):
            xmin = -1
        return xmin, xmax, ymin, ymax

    def plot_graph(self, real_locations=False):
        """
        plots the graph using matplotlib
        """
        ax = plt.axes()
        if real_locations:
            xmin, xmax, ymin, ymax = self.get_graph_lims()
        else:
            param = self.dwg_alg.v_size()
            xmin, xmax, ymin, ymax = -param, param, -param, param
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        edges = self.dwg_alg.get_all_e()
        nodes = self.dwg_alg.get_all_v()
        nodes_locations = {}
        nodes_graphics = []
        for n in nodes.values():
            if n.getLocation() is not None and real_locations:
                nodes_locations[n.getKey()] = (n.getLocation()[0], n.getLocation()[1])
                nodes_graphics.append(plt.Circle((n.getLocation()[0], n.getLocation()[1]), 0.25, color='b'))
                plt.text(n.getLocation()[0], n.getLocation()[1], n.getKey(), fontweight='bold', ha="center", va="center", color='w')
            else:
                rand_loc = (random.uniform(xmin, xmax), random.uniform(ymin, ymax))
                nodes_locations[n.getKey()] = rand_loc
                nodes_graphics.append(plt.Circle(nodes_locations[n.getKey()], 0.25, color='b'))
                plt.text(rand_loc[0], rand_loc[1], n.getKey(), fontweight='bold', ha="center", va="center", color='w')

        for e in edges:
            src_location = nodes_locations[e.getSrc()]
            dest_location = nodes_locations[e.getDest()]
            ax.arrow(src_location[0], src_location[1], dest_location[0] - src_location[0], dest_location[1] - src_location[1], head_width=0.5, head_length=0.5, fc='k', ec='k')
            if self.dwg_alg.getEdge(e.getDest(), e.getSrc()) is not None and \
                            self.dwg_alg.getEdge(e.getDest(), e.getSrc()).getInfo() == "plotted":
                plt.text((src_location[0] + dest_location[0]) / 2, (src_location[1] + dest_location[1]) / 2,
                         float("{:.2f}".format(e.getWeight())), fontweight='bold', ha="right", va="center",
                         color='r')
            else:
                e.setInfo("plotted")
                plt.text((src_location[0] + dest_location[0]) / 2, (src_location[1] + dest_location[1]) / 2,
                         float("{:.2f}".format(e.getWeight())), fontweight='bold', ha="left", va="baseline",
                         color='r')
        for circle in nodes_graphics:
            ax.add_artist(circle)
        plt.show()

    class Node:
        """
        I created this Node class thats implements compare func to fill the PriorityQueue by distance order.
        """
        def __init__(self, key=None, distance=None):
            self.key = key
            self.distance = distance

        def getKey(self):
            return self.key

        def getDistance(self):
            return self.distance

        def __cmp__(self, other):
            if self.distance < other.getDistance():
                return -1
            elif self.distance > other.getDistance():
                return 1
            else:
                return 0

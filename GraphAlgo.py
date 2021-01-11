from typing import List
import json
import queue as queue
import os
import matplotlib.pyplot as plt
from numpy import random
from NodeData import NodeData
from EdgeData import EdgeData
from pathlib import Path
import math
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=None):
        self.dwg_alg = g
        self.d1 = {}
        self.p1 = {}

    def init(self, g):
        self.dwg_alg = g

    def get_graph(self):
        return self.dwg_alg

    def load_from_json(self, file_name):
        """
        Loads a graph from a json file.
        """
        file_name = file_name.replace('/', '\\')
        file_name = file_name.replace('\\\\', '\\')
        file_name = file_name.split('\\')
        base_path = Path(__file__).parent
        # TODO: generalize
        file_path = (base_path / file_name[1] / file_name[2]).resolve()

        with open(file_path, 'r') as fp:
            data = json.load(fp)
            nodes_list = data["Nodes"]
            edges_list = data["Edges"]

        for n in nodes_list:
            if "pos" in n:
                pos = n["pos"]
            else:
                pos = None
            self.dwg_alg.add_node(n["id"], pos)
        for edge in edges_list:
            self.dwg_alg.add_edge(edge["src"], edge["dest"], edge["w"])
        return True

    def save_to_json(self, file_name):
        nodes = self.dwg_alg.getV()
        edges = self.dwg_alg.getE()
        nodes_parsed = []
        edges_parsed = []
        for v in nodes:
            if v.getLocation() is not None:
                temp_node = {'id': v.getSrc(), 'pos': v.getLocation()}
            else:
                temp_node = {'id': v.getSrc()}
            nodes_parsed.append(temp_node)
        for e in edges:
            if e.getWeight() is not None:
                temp_edge = {'src': e.getSrc(), 'dest': e.getDest(), 'w': e.getWeight()}
            else:
                temp_edge = {'src': e.getSrc(), 'dest': e.getDest()}
            edges_parsed.append(temp_edge)
        file = {'Nodes': nodes_parsed, 'Edges': edges_parsed}

        try:
            os.remove(file_name)
        except OSError:
            return False
        with open(file_name, 'x') as fp:
            json.dump(file, fp)
            return True

    def specialDFS(self, i, low_link, ids, OnStack, st, sccCount, id):
        st.push(i)
        OnStack[i] = True
        ids[i] = id
        low_link[i] = id
        id += 1
        for e in self.dwg_alg.getE(i):
            if ids[e.getDest()] == -1:
                self.specialDFS(e.getDest(), low_link, ids, OnStack, st, sccCount, id)
            if OnStack[e.getDest()]:
                low_link[i] = min(low_link[i], low_link[e.getDest()])
            w = -1
            if ids[i] == low_link[i]:
                while w != i:
                    w = st.pop()
                    OnStack[w] = False
                    low_link[w] = ids[i]
                sccCount += 1

    def isConnected(self):
        ids = [-1] * self.dwg_alg.v_size()
        low_link = [-1] * self.dwg_alg.v_size()
        OnStack = [False] * self.dwg_alg.v_size()
        st = []
        sccCount = 0
        id = 0
        for i in range(self.dwg_alg.v_size()):
            if ids[i] == -1:
                self.specialDFS(i, low_link, ids, OnStack, st, sccCount, id)
        if sccCount == 1:
            return True
        else:
            return False

    def Dijkstra(self, s):
        self.d1 = {}
        self.p1 = {}
        visited = set()
        q = []
        for n in self.dwg_alg.getV():
            self.d1[n.getKey()] = float('inf')
            self.p1[n.getKey()] = None
        self.d1[s.getKey()] = float(0)
        q.append(self.Node(s.getKey(), 0))
        while len(visited) != self.dwg_alg.v_size():
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
        self.Dijkstra(self.dwg_alg.getNode(id1))
        return self.d1[id2]

    def shortest_path(self, id1, id2):
        self.Dijkstra(self.dwg_alg.getNode(id1))
        s = self.dwg_alg.getNode(id2)
        l = []
        while s is not None:
            l.append(s)
            s = self.p1[s.getKey()]
        l.reverse()
        return l

    def plot_graph(self):
        ax = plt.axes()
        xlim = 2
        ylim = 2
        plt.xlim(-xlim, xlim)
        plt.ylim(-ylim, ylim)
        edges = self.dwg_alg.get_all_e()
        nodes = self.dwg_alg.get_all_v()
        nodes_rand_locations = {}
        nodes_graphics = []
        for n in nodes.values():
            if n.getLocation() is not None:
                nodes_graphics.append(plt.Circle((n.getLocation()[0], n.getLocation()[1]), 0.05, color='r'))
            else:
                nodes_rand_locations[n.getKey()] = (random.uniform(-xlim, xlim), random.uniform(-ylim, ylim))
                nodes_graphics.append(plt.Circle(nodes_rand_locations[n.getKey()], 0.05, color='b'))

        for e in edges:
            src_location = nodes_rand_locations[e.getSrc()]
            dest_location = nodes_rand_locations[e.getDest()]
            ax.arrow(src_location[0], src_location[1], dest_location[0] - src_location[0], dest_location[1] - src_location[1], head_width=0.3, head_length=0.1, fc='k', ec='k')
            plt.text((src_location[0] + dest_location[0]) / 2, (src_location[1] + dest_location[1]) / 2, e.getWeight(), fontweight='bold', ha="center", va="center", color='r')
            print("src:", src_location)
            print("dest:", dest_location)

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

import unittest
import os

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class GraphAlgo_test(unittest.TestCase):

    def test_init(self):
        print("start GraphAlgo init test")
        g_algo = GraphAlgo()
        self.assertIsInstance(g_algo.get_graph(), DiGraph)
        g = DiGraph()
        g_algo = GraphAlgo(g)
        self.assertIsInstance(g_algo.get_graph(), DiGraph)

    def test_json(self):
        print("start GraphAlgo json test")
        g = DiGraph()
        json = "test.json"
        g_algo = GraphAlgo(g)
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 20)
        g_algo.save_to_json(json)
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json("test.json")
        self.assertIsInstance(g_algo2, GraphAlgo)
        g2 = g_algo2.get_graph()
        self.assertTrue(g2.e_size() == 2)
        self.assertTrue(g2.v_size() == 3)
        self.assertIsNotNone(g2.getEdge(0, 1))
        self.assertEqual(g2.getEdge(0, 1).getWeight(), 10)
        self.assertEqual(g2.getEdge(0, 2).getWeight(), 20)
        self.assertIsNotNone(g2.getEdge(0, 2))
        self.assertIsNotNone(g2.getNode(0))
        self.assertIsNotNone(g2.getNode(1))
        self.assertIsNotNone(g2.getNode(2))
        # deleting test.json file
        try:
            os.remove(g_algo.parse_path(json))
        except OSError:
            raise AssertionError("error deleting json file")

    def test_connected_components(self):
        print("start GraphAlgo connected components test")
        g = DiGraph()
        g_algo = GraphAlgo(g)
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0, 1, 10)
        g.add_edge(1, 0, 20)
        scc = g_algo.connected_components()
        self.assertIsInstance(scc, list)
        self.assertEqual(len(scc), 2)
        self.assertTrue((len(scc[0]) == 2 and len(scc[1]) == 1) or (len(scc[0]) == 1 and len(scc[1]) == 2))
        if len(scc[0]) == 2:
            self.assertTrue(0 in scc[0])
            self.assertTrue(1 in scc[0])
            self.assertTrue(2 in scc[1])
        else:
            self.assertTrue(0 in scc[1])
            self.assertTrue(1 in scc[1])
            self.assertTrue(2 in scc[0])

if __name__ == '__main__':
    unittest.main()

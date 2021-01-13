import unittest

from NodeData import NodeData
from EdgeData import EdgeData
from DiGraph import DiGraph

class DiGraph_test(unittest.TestCase):

    def test_init(self):
        print("start DiGraph init test")
        g = DiGraph()
        self.assertIsInstance(g, DiGraph)
        self.assertEqual(g.get_mc(), 0)
        self.assertEqual(g.e_size(), 0)
        self.assertIsInstance(g.get_all_v(), dict)
        self.assertEqual(g.get_all_v(), {})

    def test_add_node(self):
        print("start DiGraph add node test")
        g = DiGraph()
        g.add_node(0)
        self.assertIsInstance(g.get_all_v()[0], NodeData)
        self.assertEqual(g.get_all_v()[0].getKey(), 0)
        self.assertIsNone(g.get_all_v()[0].getLocation())

    def test_add_edge(self):
        print("start DiGraph add edge test")
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 10)
        self.assertIsInstance(g.get_all_e()[0], EdgeData)
        self.assertIsInstance(g.getEdge(0, 1), EdgeData)
        self.assertIsNotNone(g.getE(0))
        self.assertEqual(g.get_all_e()[0].getSrc(), 0)
        self.assertEqual(g.get_all_e()[0].getDest(), 1)

    def test_all_in_edges(self):
        print("start DiGraph all in edges test")
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(1, 0, 10)
        g.add_edge(2, 0, 20)
        all_in = g.all_in_edges_of_node(0)
        self.assertIsInstance(all_in, dict)
        self.assertTrue(len(all_in) == 2)
        # checking that correct weights are in dict
        self.assertEqual(all_in[1], 10)
        self.assertEqual(all_in[2], 20)

    def test_all_out_edges(self):
        print("start DiGraph all out edges test")
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 20)
        all_out = g.all_out_edges_of_node(0)
        self.assertIsInstance(all_out, dict)
        self.assertTrue(len(all_out) == 2)
        # checking that correct weights are in dict
        self.assertEqual(all_out[1], 10)
        self.assertEqual(all_out[2], 20)

    def test_remove_node(self):
        print("start DiGraph remove node test")
        g = DiGraph()
        g.add_node(0)
        self.assertIsNotNone(g.getNode(0))
        g.remove_node(0)
        self.assertIsNone(g.getNode(0))

    def test_remove_edge(self):
        print("start DiGraph remove edge test")
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 10)
        self.assertIsNotNone(g.getEdge(0, 1))
        g.remove_edge(0, 1)
        self.assertIsNone(g.getEdge(0, 1))

    def test_equals(self):
        print("start DiGraph equals test")
        g = DiGraph()
        self.assertTrue(g.__eq__(g))

if __name__ == '__main__':
    unittest.main()

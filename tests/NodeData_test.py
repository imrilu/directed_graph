import unittest

from NodeData import NodeData
from EdgeData import EdgeData

class NodeData_test(unittest.TestCase):

    def test_init(self):
        print("start NodaData init test")
        node = NodeData(0, (1, 2))
        self.assertIsInstance(node, NodeData, "node is not instance of class")
        self.assertIsNotNone(node.getKey(), "no key for node")
        self.assertIsNotNone(node.getLocation(), "no location for node")
        self.assertIsNone(node.getTag(), "tag should be none")
        self.assertIsNone(node.getInfo(), "info should be none")
        self.assertIsNone(node.getWeight(), "weight should be none")
        self.assertEqual(node.getNi_in(), [], "error init in_edges list")
        self.assertIsInstance(node.getNi_out(), type({}.values()), "error init out_edges list")

    def test_setters(self):
        print("start node setters test")
        node = NodeData(0)
        node.setWeight(1)
        node.setTag("tag")
        node.setInfo("info")
        node.setLocation((1,3))
        self.assertEqual(node.getWeight(), 1)
        self.assertEqual(node.getTag(), "tag")
        self.assertEqual(node.getInfo(), "info")
        self.assertEqual(node.getLocation(), (1,3))

    def test_equals(self):
        print("start node equals test")
        node1 = NodeData(0)
        self.assertTrue(node1.__eq__(node1))

    def test_Ni_in(self):
        print("start in_edges test")
        node1 = NodeData(1)
        node2 = NodeData(2)
        edge1 = EdgeData(1, 2, 10)
        node2.addNi_in(2)
        self.assertEqual(node2.getNi_in()[0], 2)

    def test_Ni_out(self):
        print("start out_edges test")
        node1 = NodeData(1)
        node2 = NodeData(2)
        node1.addNi_out(2, 10)
        out_edges = node1.getNi_out()
        e = list(out_edges)[0]
        self.assertIsInstance(e, EdgeData)
        self.assertTrue(e.getSrc(), 1)
        self.assertTrue(e.getDest(), 2)
        self.assertTrue(e.getWeight(), 10)
        self.assertTrue(node1.hasNi_out(2), "node1 doesnt have out connection")
        self.assertIsNotNone(node1.removeEdge_out(2))

if __name__ == '__main__':
    unittest.main()

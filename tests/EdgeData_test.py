import unittest

from EdgeData import EdgeData

class EdgeData_test(unittest.TestCase):

    def test_init(self):
        print("start edge init test")
        edge = EdgeData(1, 2, 10, "info", "tag")
        self.assertIsInstance(edge, EdgeData)
        self.assertEqual(edge.getSrc(), 1)
        self.assertEqual(edge.getDest(), 2)
        self.assertEqual(edge.getWeight(), 10)
        self.assertEqual(edge.getInfo(), "info")
        self.assertEqual(edge.getTag(), "tag")

    def test_setters(self):
        print("start edge setters test")
        edge = EdgeData(1, 2, 10)
        edge.setInfo("info")
        edge.setTag("tag")
        self.assertEqual(edge.getInfo(), "info")
        self.assertEqual(edge.getTag(), "tag")


if __name__ == '__main__':
    unittest.main()

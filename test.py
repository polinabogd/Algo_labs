import unittest
from kruskal import Graph


class MyTestCase(unittest.TestCase):
    def test_kruskal_1(self):
        g = Graph(4)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 6)
        g.add_edge(0, 3, 5)
        g.add_edge(1, 3, 15)
        g.add_edge(2, 3, 4)
        self.assertEqual(g.kruskal(), 19)

    def test_kruskal_2(self):
        g = Graph(6)
        g.add_edge(0, 1, 4)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 2)
        g.add_edge(1, 0, 4)
        g.add_edge(2, 0, 4)
        g.add_edge(2, 1, 2)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 5, 2)
        g.add_edge(2, 4, 4)
        g.add_edge(3, 2, 3)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 2, 4)
        g.add_edge(4, 3, 3)
        g.add_edge(5, 2, 2)
        g.add_edge(5, 4, 3)
        self.assertEqual(g.kruskal(), 14)


if __name__ == '__main__':
    unittest.main()

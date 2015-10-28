#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#


import unittest

from vertex import Vertex


class TestVertex(unittest.TestCase):


    def setUp(self):
        self.v1 = Vertex()
        self.v2 = Vertex()
        self.x = Vertex('x')
        self.another_x = Vertex('x')


    def test_a_vertex_has_auto_label(self):
        self.assertNotEqual(self.v1, self.v2)

    def test_a_vertex_can_receive_a_label(self):
        self.assertEqual(str(self.x), "x")
        self.assertEqual(str(self.another_x), "x")

    def test_two_vertices_with_same_label_are_equal(self):
        self.assertEqual(self.x, self.another_x)

if __name__ == '__main__':
    unittest.main(verbosity=2)


import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	6	24
-1	-1	1
-1	1	1
1	1	1
1	-1	1
-1	-1	-1
-1	1	-1
1	1	-1
1	-1	-1
4	1    2    3    4
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5
4	8    7    6    5"""
        fake_file_path = 'data/poly_cube.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.poly_cube = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        fake_file_content = """200.0	60.0	-140.0	60.0
8	5	20
-1	-1	1
-1	1	1
1	1	1
1	-1	1
-1	-1	-1
-1	1	-1
1	1	-1
1	-1	-1
4	1    2    3    4
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/poly_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.poly_box = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        fake_file_content = """100.0	0.0 0.0	0.0
4 1 4
1   1   1
1   -2  1
-2  -2  1
-2  1   1
4   1   2   3   4"""
        fake_file_path = 'data/poly_square.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.poly_square = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.poly_box.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.poly_box.facets), 5)

    def test_num_edges(self):
        self.assertEqual(len(self.poly_box.edges), 20)

    # tests for perimetr with good points

    # polyedr perimetr

    def test_box_perimetr(self):
        self.assertEqual(self.poly_box.good_perimetr, 12)

    # double edges (with two facets) can be countable

    def test_cube_perimetr(self):
        self.assertEqual(self.poly_cube.good_perimetr, 12)

    # perimetr can be equal zero

    def test_sq_perimetr(self):
        self.assertEqual(self.poly_square.good_perimetr, 0)

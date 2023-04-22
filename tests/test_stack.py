import unittest
from src import stack
nd = stack.Node('a', None)

class TestStack(unittest.TestCase):
    def test_node(self):
        self.assertEqual(nd.data, 'a')
        self.assertEqual(nd.next_node, None)
        test_value = stack.Stack()
        test_value.push('data1')
        self.assertEqual(test_value.pop(), 'data1')


if __name__ == '__main__':
    unittest.main()

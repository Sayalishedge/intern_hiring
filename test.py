import unittest
from assignment import friends_main

class TestFriends(unittest.TestCase):
    def setUp(self):
        self.friendships = {
            'A': ['B', 'C', 'J'],
            'D': ['E', 'F', 'G'],
            'H': ['I', 'K', 'V'],
            'J': ['V'],
            'K': ['L', 'M', 'N', 'A'],
            'O': ['P', 'V', 'U'],
            'Q': ['S', 'T', 'D'],
            'U': ['H', 'J'],
            'V': ['W', 'X', 'Y', 'Z']
        }

    def test_start_M(self):
        start_candidate = 'M'
        contacted_candidates = friends_main(start_candidate)
        expected_result = ['M', 'K', 'L', 'N', 'A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z']
        self.assertEqual(contacted_candidates, expected_result)

    def test_start_D(self):
        start_candidate = 'D'
        contacted_candidates = friends_main(start_candidate)
        expected_result = ['D', 'Q', 'E', 'F', 'G', 'S', 'T']
        self.assertEqual(contacted_candidates, expected_result)

    def test_start_V(self):
        start_candidate = 'V'
        contacted_candidates = friends_main(start_candidate)
        expected_result = ['V', 'H', 'J', 'O', 'W', 'X', 'Y', 'Z', 'I', 'K', 'P', 'U', 'L', 'M', 'N', 'A', 'B', 'C']
        self.assertEqual(contacted_candidates, expected_result)

if __name__ == '__main__':
    unittest.main()

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
        expected_result = ['K', 'A', 'J', 'V', 'Z', 'Y', 'X', 'W', 'C', 'B', 'N', 'M', 'L']
        self.assertEqual(contacted_candidates, expected_result)

    def test_start_D(self):
        start_candidate = 'D'
        contacted_candidates = friends_main(start_candidate)
        expected_result = ['Q', 'D', 'G', 'F', 'E', 'T', 'S']
        self.assertEqual(contacted_candidates, expected_result)

    def test_start_V(self):
        start_candidate = 'V'
        contacted_candidates = friends_main(start_candidate)
        expected_result = ['O', 'U', 'J', 'V', 'Z', 'Y', 'X', 'W', 'H', 'K', 'A', 'C', 'B', 'N', 'M', 'L', 'I', 'P']
        self.assertEqual(contacted_candidates, expected_result)

if __name__ == '__main__':
    unittest.main()

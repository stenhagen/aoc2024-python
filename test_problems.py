import unittest
import p1

class TestProblems(unittest.TestCase):

    def test_1a(self):
        self.assertEqual(p1.p1a(True), 11)
    
    def test_1a_prop(self):
        self.assertEqual(p1.p1a(True, "1t_prop.txt"), 12)

    def test_1b(self):
        self.assertEqual(p1.p1b(True), 31)
        
if __name__ == '__main__':
    unittest.main()
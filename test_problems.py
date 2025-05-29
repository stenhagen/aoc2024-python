import unittest
import p1
import p2
import p3

class TestProblems(unittest.TestCase):

    def test_1a(self):
        self.assertEqual(p1.p1a(True), 11)
    
    def test_1a_prop(self):
        self.assertEqual(p1.p1a(True, "1t_prop.txt"), 12)

    def test_1b(self):
        self.assertEqual(p1.p1b(True), 31)

    def test_2a(self):
        self.assertEqual(p2.p2a(True), 2)

    def test_2b(self):
        self.assertEqual(p2.p2b(True), 4)
    
    def test_3a(self):
        self.assertEqual(p3.p3a(True), 161)
        
if __name__ == '__main__':
    unittest.main()
import unittest
import p1
import p2
import p3
import p4
import p5

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

    def test_3b(self):
        self.assertEqual(p3.p3b(True), 48)

    def test_4a(self):
        self.assertEqual(p4.p4a(True), 18)

    def test_4b(self):
        self.assertEqual(p4.p4b(True), 9)

    def test_5a(self):
        self.assertEqual(p5.p5a(True), 143)
    
    def test_5b(self):
        self.assertEqual(p5.p5b(True), 123)

if __name__ == '__main__':
    unittest.main()
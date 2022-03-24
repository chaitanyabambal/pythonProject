import unittest

def cubeVolume(x):
    return x*x*x

class volumeCube(unittest.TestCase):
    def test_cube(self):
        x=5.555
        result=cubeVolume(x)
        self.assertAlmostEqual(result,x*x*x)

if __name__=="__main__":
    unittest.main()
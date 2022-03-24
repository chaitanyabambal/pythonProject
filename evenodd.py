import unittest

def check(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

class Myapp1(unittest.TestCase):
    def test_case_even(self):
        a=30
        result=check(a)
        self.assertEqual("even",result)

    def test_case_odd(self):
        a=35
        result=check(a)
        self.assertEqual("odd",result)



if __name__=="__main__":
    unittest.main()
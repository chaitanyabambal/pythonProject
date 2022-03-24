import unittest

def odev(a):
    if a%2==0:
       return "even"
    else:
        return "odd"

def add(a, b):

    return a+b


class c1(unittest.TestCase):

    def testcase1(self):
        a=10
        b=20
        c= add(a,b)
        self.assertEqual(a+b,c)


class c2(unittest.TestCase):

    def testc2(self):
        x= int(input("enter even no : "))
        y=odev(x)

        self.assertEqual("even", y)

    def testc3(self):
        x = int(input("enter odd no : "))
        y = odev(x)

        self.assertEqual("odd", y)



if __name__ == "__main__":
    unittest.main()
# Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List

import unittest

class sum_neg_pos_even_odd(unittest.TestCase):
    def test_list(self):
       self.assertEqual(sum_list([-43,-67,24,89,37,69,64,-12,25]),(-122, 308, 88, 220))


def  sum_list(list1):
    Neg = 0
    Pos = 0
    Even = 0
    Odd = 0
    for i in list1:
        if i < 0:
            Neg = Neg + i
        else:
            Pos = Pos + i
            if i % 2 == 0:
                Even = Even + i
            else:
                Odd = Odd + i
    return Neg,Pos,Even,Odd

list1 = [-43,-67,24,89,37,69,64,-12,25]

print(sum_list(list1))

if __name__ == "__main__":
    unittest.main()

    


            
    
        

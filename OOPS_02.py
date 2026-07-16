import math
class Calculator :
    def __init__(self,n:int)-> int :
        self.sqr =  n* n
        self.cube =  ( self.sqr * n )
        self.sqroot = math.isqrt(n)
    def calculation (self,n:int)-> int :
        print(f"The square {self.sqr} , square root {self.sqroot }, cube {self.cube} of number {n}")
e1 = Calculator(8)
e1.calculation(8)









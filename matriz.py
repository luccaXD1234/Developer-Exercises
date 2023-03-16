from random import *


FIL = 5
COL = 5

m = [[randint(1,100) for j in range(COL)] 
                        for i in range(FIL)]

for i in m:
    print(i)


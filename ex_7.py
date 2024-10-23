# Un programme pour afficher le nieme nombre premier

import math
n = int(input("Entrez un nombre svp : "))
count = 0
nieme_premier = 2
while count < n:
    if (math.factorial(nieme_premier - 1) + 1)%nieme_premier == 0:
        count += 1
        if count == n:
            break
    nieme_premier += 1
print(nieme_premier)
# Prime detector

n = int(input("Entrez un entier naturel : "))
is_prime = True

for j in range(1, n+1):
    if(j != 1 and j != n and n%j == 0):
        is_prime = False
        break

if is_prime:
    print("Ce nombre est premier")
else:
    print("Ce nombre n'est pas premier")

# Une autre methode (Theoreme de Wilson)

import math

if((math.factorial(n-1) + 1)%n == 0):
    print("Ce nombre est premier")
else:
    print("Ce nombre n'est pas premier")
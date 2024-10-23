import math

n = int(input("Entrer un nombre superieur à 2 : "))
p= n
  
if n >= 2:
    for i in range(1, n):
        p = math.sqrt(p) + (n - i) 
    print(math.sqrt(p))   
else:
    print("Invalide")
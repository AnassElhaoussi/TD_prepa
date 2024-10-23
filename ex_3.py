import math
n = int(input("Dkhel chi ra9m : "))
idx = 0
# Premier model

for i in range(1, n):
    if i < math.floor(n/2):
        for j in range(1, i):
            print("*", end=" ")
        
    else:
        for k in range(1, n-i):
            print("*", end=" ")   
    print("\n")

# Deuxieme model

m = int(input("Dkhel chi haja : "))

for p in range(1, n):
    for l in range(1, p + 1):
        print(p, end=" ")
    print("\n")
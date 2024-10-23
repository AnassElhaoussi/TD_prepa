
a = int(input("Entrez un nombre svp : "))
print(a)

for i in range(10):
    if a%2 == 0:
        a = a/2
        print(a)
    else:  
        a = 3*a + 1
        print(a)
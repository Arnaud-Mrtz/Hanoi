def hanoi(n, de , a, par):
    
    if n>0:
        hanoi(n-1,de, par, a)
        a.append(de[len(de)-1])
        de.pop()
        print("""

            Etape suivante :
        """)
        print("Base 1"+str(A))
        print("Base 2"+str(B))
        print("Base 3"+str(C))
        hanoi(n-1, par, a, de)
Disks=["Disque 5","Disque 4","Disque 3","Disque 2","Disque 1"]
A=[]
B=[]
C=[]
print("""
Tours de Hanoi
Voici les la liste des déplacements pour faire passer les disques de la tour A vers la tour C
""")
n = int(input("Nombre de disques (de 1 à 5) : "))
for i in range(n):
    A.append(Disks[i+(len(Disks)-n)])
print(A)
hanoi(n,A,C,B)
print("Bon jeu.")
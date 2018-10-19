__author__='juan carlos meza serrano'

def MCD (A,B):
    if B==0:
        return A
    else:
        return MCD(B,A%B)

num1=int(input("primer Numero: "))
num2=int(input("segundo Numero: "))

print("El maximo común divisor es  ", MCD(num1,num2))

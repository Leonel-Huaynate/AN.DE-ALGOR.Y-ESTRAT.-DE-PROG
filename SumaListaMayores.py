
def sumaMayores(lst,n,indice):

    if indice == len(lst):
        return 0


    if lst[indice] >= n:
        return lst[indice] + sumaMayores(lst, n, indice + 1)
    else:
        return sumaMayores(lst,n,indice+1)
    
lista=[3,1,7,8,2,10,4]

n=int(input("Ingrese un numero : "))

print(f"La suma de los elementos de la lista {lista} mayores e iguales es : ",end="")
print(sumaMayores(lista,n,0))
from random import *


def mariz(n,m):                         
    mat = [ [0] * n for i in range(m)]

    for i in range(m):                 #i fila 
        for j in range(n):             #j columna 
            mat[i][j]=randint(1, 10)
    return mat



def resolverF1(mat,n,m):
    for i in range(5):
        if mat[i][0] == mat[i][1] == mat[i][2] == mat[i][3]:
            print("secuencia de 4 números consecutivos horizontal encontrada , desde la posicion ",i,"0 hasta ",i,"4")	
    return()
def resolverF2(mat,n,m):
    for i in range(5):
        if mat[i][1] == mat[i][2] == mat[i][3] == mat[i][4]:
            print("secuencia de 4 números consecutivos horizontal encontrada , desde la posicion ",i,"1 hasta ",i,"5")
    return()

def resolverC1(mat,n,m):
    for j in range(5):
        if mat[0][j] == mat[1][j] == mat[2][j] == mat[3][j]:
            print("secuencia de 4 números consecutivos vertical encontrada , desde la posicion ",j,"0 hasta ",j,"4")
    return()
def resolverC2(mat,n,m):
    for j in range(5):
        if mat[1][j] == mat[2][j] == mat[3][j] == mat[4][j]:
            print("secuencia de 4 números consecutivos vertical encontrada , desde la posicion ",j,"1 hasta ",j,"5")
    return()
           

def main():

    n=5
    m=5
    mat = mariz(n,m)
    print(mat)
    resolverF1(mat,n,m)
    resolverF2(mat,n,m)
    resolverC1(mat,n,m)
    resolverC2(mat,n,m)

if __name__=="__main__":
    main()
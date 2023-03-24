from random import *
n=5
m=5


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

    mat =  [[9,8,9,8,9],
			[9,7,8,7,8],
			[9,6,5,6,5],
			[9,2,3,2,3],
			[1,0,1,0,0]]
    print(mat)
    resolverF1(mat,n,m)
    resolverF2(mat,n,m)
    resolverC1(mat,n,m)
    resolverC2(mat,n,m)

if __name__=="__main__":
    main()
from random import *



def mariz(n,m):   
    mat = [ [0] * n for i in range(m)]
    print(mat)

    for i in range(m):
        for j in range(n):
            mat[i][j]=randint(1, 10)
    return mat



def resolverF(mat,n,m):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==mat[i+1][j]:
                print("caca")
    return()


def resolverC(mat,n,m):
    pass
    return()
           


def main():

    print("hola")
    n=5
    m=5
    mat = mariz(n,m)
    print(mat)
    resolverF(mat,n,m)
    resolverC(mat,n,m)

if __name__=="__main__":
    main()
# matrix multiplication
def createMatrix():
    rows = int(input("Enter rows :"))
    mat = []
    cols = int(input("Enter columns :"))
    for i in range(rows):
        mat.append([])
        for j in range(cols):
            mat[i].append(int(input("Enter the number for row {} col {} : ".format(i,j))))
    return mat

def printMatrix(_matrix):
    for i in range(len(_matrix)):
        fstr = '{:<3d}'
        fstr = fstr * len(_matrix[0])
        print(fstr.format(*_matrix[i]),sep=' ')
firstMat = createMatrix()
secondMat = createMatrix()
printMatrix(firstMat)

print()
printMatrix(secondMat)



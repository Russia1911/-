


matrix = [[-1, 0, 1], [-1, 0, 1], [0, 1, -1]]




def printMatrix ( matrix ):
   for i in range ( len(matrix) ):
      for j in range ( len(matrix[i]) ):
          print ( "{:4d}".format(matrix[i][j]), end = "" )
      print ()


a = printMatrix(matrix)


import unittest

class matrix: 
    def __init__(self, m):
        self.mtx = m
        self.r = len(m)
        self.c = len(m[0])
    
    def Add(self, mtx2):
        if self.r == mtx2.r and self.c == mtx2.c:
            result = matrix([[self.mtx[i][j] + mtx2.mtx[i][j] for j in range(self.c)] for i in range(self.r)])
            return result
        else:
            print("Can't be added")
            return

    def Subtract(self, mtx2):
        if self.r == mtx2.r and self.c == mtx2.c:
            result = matrix([[self.mtx[i][j] - mtx2.mtx[i][j] for j in range(self.c)] for i in range(self.r)])
            return result
        else:
            print("Can't be subtracted")
            return

    def Multiply(self, mtx2):
        if self.c == mtx2.r:
            result = [[0 for j in range(mtx2.c)] for i in range(self.r)]

            for i in range(self.r):
                for j in range(mtx2.c):
                    for k in range(self.c):
                        result[i][j] += self.mtx[i][k]*mtx2.mtx[k][j]

            return matrix(result)

        else:
            print("Can't be multiply")
            return

    def Determinant(self):
        if self.r == self.c:
            if self.r == 2:
                return self.mtx[0][0]*self.mtx[1][1] - self.mtx[0][1]*self.mtx[1][0]
            
            det = 0
            for i in range(self.c):
                det += ((-1)**i) * self.mtx[0][i] * self.minor(0, i).Determinant()
            return det

        else:
            print("Determinant is not possible as given matrix isn't a square matrix")
            return

    def minor(self, i, j):
        m = [row[:j] + row[j+1:] for row in (self.mtx[:i]+self.mtx[i+1:])]
        Minor = matrix(m)
        return Minor

    def Exponentiate(self, n):
        if self.r == self.c:
            m = [[0 for j in range(self.c)] for i in range(self.r)]
            for i in range(self.r):
                for j in range(self.c):
                    if i == j:
                        m[i][j] = 1
                    else:
                        m[i][j] = 0
            In = matrix(m)
            for i in range(n):
                In = In.Multiply(self)
            return In
        else:
            print("Can't exponentiate as given matrix isn't square")
            return

#-------------------------------------Tests to check the above functions----------------------------------------

m1 = [[1,1,6,8], [5,6,7,1], [6,9,6,9], [0,4,2,0]]
m2 = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

matrix1 = matrix(m1)
matrix2 = matrix(m2)

class TestMatrixMethods(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(matrix1.Add(matrix2).mtx, [[2,1,6,8], [5,7,7,1], [6,9,7,9], [0,4,2,1]])

    def test_Subtract(self):
        self.assertEqual(matrix1.Subtract(matrix2).mtx, [[0,1,6,8], [5,5,7,1], [6,9,5,9], [0,4,2,-1]])
    
    def test_Multiply(self):
        self.assertEqual(matrix1.Multiply(matrix2).mtx, [[1,1,6,8], [5,6,7,1], [6,9,6,9], [0,4,2,0]])
    
    def test_Determinant(self):
        self.assertEqual(matrix1.Determinant(), -1248)
    
    def test_Exponentiate(self):
        self.assertEqual(matrix1.Exponentiate(10).mtx, [[676127385159, 1094463947673, 1069257088059, 867854680824],
                                                        [1033502281733, 1672959092991, 1634428596212, 1326577435786], 
                                                        [1322627793543, 2140971533460, 2091663920610, 1697688176931],
                                                        [364824152966, 590548918200, 576949328342, 468279455410]])

if __name__ == '__main__':
    unittest.main()







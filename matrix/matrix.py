import unittest

class DimensionError(Exception):
    def __init__(self, msg):
        print(msg)
class matrix: 
    def __init__(self, m):
        self.rowCheck = False
        self.typeFlag = True
        self.isInt = False
        self.isList = False
        for x in m:
            if self.isInt:
                if  not isinstance(x, int):
                    self.typeFlag = False
                    raise DimensionError("Both int and list can't be entered together")
            if self.isList:
                if not isinstance(x, list):
                    self.typeFlag = False
                    raise DimensionError("Both int and list can't be entered together")
            if type(x) is int:
                self.isInt = True
            if type(x) is list:
                self.isList = True

        if self.isList:
            self.rowLen = len(m[0])
            for x in m:
                if len(x) != self.rowLen:
                    raise DimensionError("rows of the matrix must be of same length")
            self.rowCheck = True

        if self.isInt and self.typeFlag:
            self.rowCheck = True

        if self.rowCheck and self.typeFlag:
            if self.isInt:
                self.mtx = [m]
                self.r = 1
                self.c = len(m)
            if self.isList:
                self.mtx = m
                self.r = len(m)
                self.c = len(m[0])
            
    def __add__(self, mtx2):
        if self.r == mtx2.r and self.c == mtx2.c:
            result = matrix([[self.mtx[i][j] + mtx2.mtx[i][j] for j in range(self.c)] for i in range(self.r)])
            return result
        else:
            raise DimensionError("Matrices can't be added as they are not of same size")

    def __sub__(self, mtx2):
        if self.r == mtx2.r and self.c == mtx2.c:
            result = matrix([[self.mtx[i][j] - mtx2.mtx[i][j] for j in range(self.c)] for i in range(self.r)])
            return result
        else:
            raise DimensionError("Matrices can't be subtracted as they are not of same size")

    def __mul__(self, mtx2):
        if self.c == mtx2.r:
            result = [[0 for j in range(mtx2.c)] for i in range(self.r)]

            for i in range(self.r):
                for j in range(mtx2.c):
                    for k in range(self.c):
                        result[i][j] += self.mtx[i][k]*mtx2.mtx[k][j]

            return matrix(result)

        else:
            raise DimensionError("Matrices can't be multiplied as they are not in the form of p*q and q*r")

    def Determinant(self):
        if self.r == self.c:
            if self.r == 2:
                return self.mtx[0][0]*self.mtx[1][1] - self.mtx[0][1]*self.mtx[1][0]
            
            det = 0
            for i in range(self.c):
                det += ((-1)**i) * self.mtx[0][i] * self.minor(0, i).Determinant()
            return det

        else:
            raise DimensionError("Determinant is not possible as given matrix isn't a square matrix")

    def minor(self, i, j):
        m = [row[:j] + row[j+1:] for row in (self.mtx[:i]+self.mtx[i+1:])]
        Minor = matrix(m)
        return Minor

    def __pow__(self, n):
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
                In = In*self
            return In
        else:
            raise DimensionError("Can't exponentiate as given matrix isn't square")


#-------------------------------------Tests to check the above functions----------------------------------------

m1 = [[1,1,6,8], [5,6,7,1], [6,9,6,9], [0,4,2,0]]
m2 = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
#row matrix
m3 = [[1,2,1,7,6]] #can also be entered as m3 = [1,2,1,7,6]
#column matrix
m4 = [[0], [6], [9], [3], [1]]

matrix1 = matrix(m1)
matrix2 = matrix(m2)
matrix3 = matrix(m3)
matrix4 = matrix(m4)

class TestMatrixMethods(unittest.TestCase):
    def test_Add(self):
        self.assertEqual((matrix1 + matrix2).mtx, [[2,1,6,8], [5,7,7,1], [6,9,7,9], [0,4,2,1]])
    
    def test_Add_wrong(self):
        def tester():
            matrix1 + matrix3
        self.assertRaises(DimensionError, tester)

    def test_Subtract(self):
        self.assertEqual((matrix1 - matrix2).mtx, [[0,1,6,8], [5,5,7,1], [6,9,5,9], [0,4,2,-1]])

    def test_Subtract_wrong(self):
        def tester():
            matrix2 - matrix4
        self.assertRaises(DimensionError, tester)
    
    def test_Multiply(self):
        self.assertEqual((matrix1 * matrix2).mtx, [[1,1,6,8], [5,6,7,1], [6,9,6,9], [0,4,2,0]])

    def test_Multiply_wrong(self):
        def tester():
            matrix2 * matrix3
        self.assertRaises(DimensionError, tester)
    
    def test_Determinant(self):
        self.assertEqual(matrix1.Determinant(), -1248)
    
    def test_Determinant_wrong(self):
        self.assertRaises(DimensionError, matrix3.Determinant)
    
    def test_Exponentiate(self):
        self.assertEqual((matrix1**10).mtx, [[676127385159, 1094463947673, 1069257088059, 867854680824],
                                             [1033502281733, 1672959092991, 1634428596212, 1326577435786], 
                                             [1322627793543, 2140971533460, 2091663920610, 1697688176931],
                                             [364824152966, 590548918200, 576949328342, 468279455410]])
    
    def test_Exp_wrong(self):
        def tester():
            matrix3 ** 42
        self.assertRaises(DimensionError, tester)

if __name__ == '__main__':
    unittest.main()







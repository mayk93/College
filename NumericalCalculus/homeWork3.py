'''
Numerical Calculus
Homework 3
'''
#Libraries
import gmpy2

#Variables
b = []

#Functions
"""
The function newEmptyMatrix(size)
will return a size x size 0 filled matrix.
"""
def newEmptyMatrix(size):
    newMatrix = []
    for i in range(0,size):
        newRow = []
        for j in range(0,size):
            newRow.append(0)
        newMatrix.append(newRow)
    return newMatrix
def freeTerms(size):
    newB = []
    for i in range(0,size):
        newB.append(1)
    return newB
'''
This method should be refactored to cgeck for negatives
'''
def isZero(listToCheck):
    index = 0
    for item in listToCheck:
        if item == 0:
            return (True,index)
        else:
            index += index
    return (False,index)
#Classes
"""
This class with implement square matrices
"""
class Matrix:
    def __init__(self,size):
        self.size = size
        self.matrix = newEmptyMatrix(size)
    '''
    The fillMatrix method will set the elements
    of the matrix to their appropriate values
    '''
    def fillMatrix(self):
        for i in range(0,self.size):
            self.matrix[i][i]   = 2
            try:
                self.matrix[i][i+1] = 1
            except:
                pass
            try:
                self.matrix[i+1][i] = 1
            except:
                pass
    def testMatrix(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                self.matrix[i][j] = i*10+j
    '''
    The iterate will iterate over the matrix
    but with mathematical notation:
    1 through n would translate to 0 to n-1 ( both ends included )
    '''
    def iterate(self,rowStart,rowStop,columnStart,columnStop):
        isZeroTest,badIndex = isZero([rowStart,rowStop,columnStart,columnStop])
        if not isZeroTest:
            rowStart = rowStart-1
            rowStop  = rowStop
            columnStart = rowStart-1
            columnStop  = rowStop
            for i in range(rowStart,rowStop):
                for j in range(columnStart,columnStop):
                    print(str(self.matrix[i][j])+" ",end='')
                print("")
        else:
            print("Bad index:",badIndex)
            return -1
    def getLength(self):
        maxNumerOfDigits = 0
        for row in self.matrix:
            currentNumberOfDigits = 0
            for number in row:
                currentNumberOfDigits = currentNumberOfDigits + len(str(number))
            if currentNumberOfDigits > maxNumerOfDigits:
                maxNumerOfDigits = currentNumberOfDigits
        return maxNumerOfDigits
    def displayMatrix(self):
        LENGTH = self.getLength()
        for k in range(0,LENGTH+self.size):
            print("=",end='')
        print("")
        for i in range(0,self.size):
            for j in range(0,self.size):
                print(str(self.matrix[i][j])+" ",end='')
            print("")
        for k in range(0,LENGTH+self.size):
            print("=",end='')
        print("")
#Main
def main():
    A = Matrix(12)
    A.displayMatrix()
    A.testMatrix()
    A.displayMatrix()
    A.iterate(6,8,4,8)

if __name__ == '__main__':
    main()

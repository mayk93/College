import copy
import matrix
from matrix import Matrix

def main():
    A = Matrix(5,6)
    print("A:")
    A.display()
    A.insert(1,2,9)
    print("A after insertion:")
    A.display()
    print("A[1][2] - Info:")
    print(A.at(1,2))
    print("A[2][3] - Math:")
    print(A.mathAt(2,3))
    B = copy.deepcopy(A)
    print("B:")
    B.display()
    B.matrix = matrix.identityMatrix(B.numberOfRows,B.numberOfColumns)
    print("B after change to identity:")
    B.display()
    print("A, to compare:")
    A.display()
    A.matrix = matrix.identityMatrix(A.numberOfRows,A.numberOfColumns)
    B.matrix = matrix.zeroMatrix(B.numberOfRows,B.numberOfColumns)
    print("A after change to identity:")
    A.display()
    print("B after change to zero")
    B.display()
    A.insert(1,2,9)
    print("A after insertion:")
    A.display()
    A.mathInsert(1,1,6)
    print("A after math insertion. There should be 6 in the corner.")
    A.display()
    A.transpose()
    print("A after transposition.")
    A.display()
    print("A has",A.numberOfRows,"rows.")
    print("A has",A.numberOfColumns,"columns.")


if __name__ == '__main__':
    main()

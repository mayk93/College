import copy
import matrix
import random
from matrix import Matrix
from math import sqrt

def fillMatrix(matrixToFill):
    toReturn = copy.deepcopy(matrixToFill)
    for i in range(0,matrixToFill.numberOfRows):
        for j in range(0,matrixToFill.numberOfColumns):
            if i == j:
                toReturn.insert(i,j,2)
            elif i == j+1:
                toReturn.insert(i,j,1)
            elif j == i+1:
                toReturn.insert(i,j,1)
    return toReturn

def fillResultVector(vector):
    VECTOR = 0 # A vector can be seen as a matrix with one column ( or one row )
    toReturn = copy.deepcopy(vector)
    for i in range(0,vector.numberOfRows):
        toReturn.insert(i,VECTOR,1) #Here, I am telling the matrix API to insert '1' at [i,0], that is, form a single column matrix that will server as our vector.
    return toReturn

def computeYiSum(Bsigma,bsig,x,i,mathM):
    toReturn = 0
    for j in range(1,mathM):
        toReturn = toReturn + (Bsigma.mathAt(i,j) * x.mathAt(j,1) + bsig.mathAt(i,1))
    return copy.deepcopy(toReturn)

def computeErrSum(A,y,x,i,mathM):
    toReturn = 0
    for j in range(1,mathM):
        toReturn = toReturn + (A.mathAt(i,j) * (y.mathAt(j,1)-x.mathAt(j,1)) * (y.mathAt(i,1)-x.mathAt(i,1)))
    return (copy.deepcopy(toReturn))

def Jacobi(m,A,a,epsilon,p):
    '''
    The following 5 lines are not part of the algorithm per se. They are helpers.
    '''
    VECTOR = 1 # See above. Here, it is 1 because we use math notation
    nOptim = 0
    xOptim = Matrix(m,m)
    mathP = p+1 #We use mathP (p+1) because the algorithm is written in mathematical notation (k = 1,p). By employing the matrix API, we can directly use the mathematical notation
    mathM = m+1 #We use mathM for the same reason we use mathP. It is used only for iterations, not defining sizes

    ni = copy.deepcopy(A.infiniteNorm())
    for k in range(1,mathP):
        sigma = ((2*k)/((mathP+1)*ni))
        Bsigma = Matrix(m,m)

        '''
        Compute Bsigma Matrix
        '''
        for i in range(1,mathM):
            for j in range(1,mathM):
                if i == j:
                    Bsigma.mathInsert(i,j,1-sigma) #(1-siga*A.mathAt(i,i)))
                else:
                    Bsigma.mathInsert(i,j,-sigma*(A.mathAt(i,j)/A.mathAt(i,i))) #(-sigma*A.mathAt(i,j)))
        '''
        Compute bsig vector
        '''
        bsig = Matrix(m,1)
        for i in range(1,mathM):
            bsig.mathInsert(i,VECTOR,(sigma*A.mathAt(i,VECTOR)))
        '''
        Initialize
        '''
        n = 0
        x = Matrix(m,1)
        '''
        Do while loop
        '''
        condition = True
        while condition:
            n = n + 1
            y = Matrix(m,1)
            for i in range(1,mathM):
                yi = copy.deepcopy(computeYiSum(Bsigma,bsig,x,i,mathM))
                y.mathInsert(i,VECTOR,yi)
                err = copy.deepcopy(sqrt( abs(computeErrSum(A,y,x,i,mathM)) ))
            for i in range(1,mathM):
                x.mathInsert(i,VECTOR,copy.deepcopy(y.mathAt(i,VECTOR)))
            condition = err < epsilon
        if k == 1:
            nOptim = copy.deepcopy(n)
            xOptim = copy.deepcopy(x)
        elif k>1:
            if n < nOptim:
                nOptim = copy.deepcopy(n)
                xOptim = copy.deepcopy(x)
        else:
            print("This should never be seen. If you see this, something is very, very wrong ...")
    print("===== Jacobi =====")
    print("Optim n:",nOptim)
    print("Optim solution (x):")
    x.display()
    print("Test:")
    result = A.multiplyMatrix(x)
    result.display()
    print("====================")

def computeAijYjSum(A,y,i):
    toReturn = 0
    for j in range(1,i-1):
        toReturn = toReturn + A.mathAt(i,j)*y.mathAt(j,1)
    return copy.deepcopy(toReturn)

def computeAijXjSum(A,x,i,mathM):
    toReturn = 0
    for j in range(i+1,mathM):
        toReturn = toReturn + A.mathAt(i,j)*x.mathAt(j,1)
    return copy.deepcopy(toReturn)

def computeGaussSiedelErrSum(A,y,x,mathM):
    toReturn = 0
    for i in range(1,mathM):
        for j in range(1,mathM):
            toReturn = toReturn + A.mathAt(i,j) * (y.mathAt(j,1)-x.mathAt(j,1)) * y.mathAt(i,1)-x.mathAt(i,1)
    return copy.deepcopy(toReturn)

def GaussSiedel(m,A,a,epsilon,p):
    '''
    The following 5 lines are not part of the algorithm per se. They are helpers.
    '''
    VECTOR = 1 # See above. Here, it is 1 because we use math notation
    nOptim = 0
    xOptim = Matrix(m,m)
    mathP = p+1 #We use mathP (p+1) because the algorithm is written in mathematical notation (k = 1,p). By employing the matrix API, we can directly use the mathematical notation
    mathM = m+1 #We use mathM for the same reason we use mathP. It is used only for iterations, not defining sizes

    for k in range(1,mathP):
        sigma = ((2*k)/(p+1))
        n = 0
        x = Matrix(m,VECTOR)
        condition = True
        while condition:
            n = n+1
            y = Matrix(m,1)
            for i in range(1,mathM):
                yi = ((1-sigma) * x.mathAt(i,VECTOR)) + (sigma/A.mathAt(i,i)*(a.mathAt(i,VECTOR)-computeAijYjSum(A,y,i) - computeAijXjSum(A,x,i,mathM)))
                y.mathInsert(i,VECTOR,yi)
            err = copy.deepcopy(sqrt(abs(computeGaussSiedelErrSum(A,y,x,mathM))))
            for i in range(1,mathM):
                x.mathInsert(i,VECTOR,(copy.deepcopy(y.mathAt(i,VECTOR))))
            condition = err < epsilon
        if k == 1:
            nOptim = copy.deepcopy(n)
            xOptim = copy.deepcopy(x)
        elif k>1:
            if n < nOptim:
                nOptim = copy.deepcopy(n)
                xOptim = copy.deepcopy(x)
        else:
            print("This should never be seen. If you see this, something is very, very wrong ...")
    print("===== Gauss Siedel =====")
    print("Optim n:",nOptim)
    print("Optim solution (x):")
    x.display()
    print("Test:")
    result = A.multiplyMatrix(x)
    result.display()
    print("====================")

def ConjugatedGradient(m,A,a,epsilon,p):
    '''
    The following 5 lines are not part of the algorithm per se. They are helpers.
    '''
    VECTOR = 1 # See above. Here, it is 1 because we use math notation
    nOptim = 0
    xOptim = Matrix(m,m)
    mathP = p+1 #We use mathP (p+1) because the algorithm is written in mathematical notation (k = 1,p). By employing the matrix API, we can directly use the mathematical notation
    mathM = m+1 #We use mathM for the same reason we use mathP. It is used only for iterations, not defining sizes

    X = Matrix(m,VECTOR)
    Y = Matrix(m,VECTOR)
    r = Matrix(m,VECTOR)
    aux = Matrix(m,VECTOR)
    v = Matrix(m,VECTOR)

    for i in range(1,mathM):
        X.mathInsert(i,VECTOR,1)
    aux = copy.deepcopy(A.multiplyMatrix(X))
    r = copy.deepcopy(a.substractMatrix(aux))
    v = copy.deepcopy(r)
    for i in range(1,mathM):
        sum1 = 0
        for j in range(1,mathM):
            sum1 = sum1 + r.mathAt(j,1)**2
        av = Matrix(m,VECTOR)
        av = copy.deepcopy(A.multiplyMatrix(v))
        sum2 = 0
        for j in range(1,mathM):
            sum2 = sum2 + av.mathAt(j,1) * v.mathAt(j,1)
        ai = 0
        ai = sum1 / sum2+(10**(-10))
        aux = copy.deepcopy(v.scalarMultiplication(ai))
        aux = copy.deepcopy(aux.addMatrix(X))
        Y = copy.deepcopy(aux)
        aux = copy.deepcopy(A.multiplyMatrix(Y))
        r = copy.deepcopy(a.substractMatrix(aux))
        sum3 = 0
        ci = 0
        for j in range(1,mathM):
            sum3 = sum3 + r.mathAt(j,1)**2
        ci = sum3 / sum1
        aux = copy.deepcopy(v.scalarMultiplication(ci))
        aux = copy.deepcopy(r.addMatrix(aux))
        v = copy.deepcopy(aux)
        X = copy.deepcopy(Y)
    print("===== Conjugated Gradient =====")
    print("Optim solution (x):")
    X.display()
    print("Test:")
    result = A.multiplyMatrix(X)
    result.display()
    print("====================")

def otherGaussSiedelB(A,m):
    toReturn = Matrix(m,m)
    for i in range(0,m):
        for j in range(0,m):
            if i == j:
                toReturn.insert(i,j,(1-A.at(i,j)))
            else:
                toReturn.insert(i,j,(-A.at(i,j)))
    return copy.deepcopy(toReturn)

def otherGaussSiedelSum(B,x,b,i,mathM):
    toReturn = 0
    for j in range(1,mathM):
        toReturn = toReturn + B.mathAt(i,j)*x.mathAt(i,1) + b.mathAt(i,1)
    return toReturn

def computeNorm(x,newX,norm):
    if norm == 1:
        xMinusNewX = copy.deepcopy(x.substractMatrix(newX))
        return xMinusNewX.normOne()
    elif norm == 999:
        xMinusNewX = copy.deepcopy(x.substractMatrix(newX))
        return xMinusNewX.infiniteNorm()
    else:
        print("Bad norm.")
        return None

def otherGaussSiedel(m,A,a,epsilon,p):
    VECTOR = 1 # See above. Here, it is 1 because we use math notation
    nOptim = 0
    xOptim = Matrix(m,m)
    mathP = p+1 #We use mathP (p+1) because the algorithm is written in mathematical notation (k = 1,p). By employing the matrix API, we can directly use the mathematical notation
    mathM = m+1 #We use mathM for the same reason we use mathP. It is used only for iterations, not defining sizes

    B = Matrix(m,m)
    B = copy.deepcopy(otherGaussSiedelB(A,m))

    q0 = B.normOne()
    q1 = B.infiniteNorm()
    q = -1
    norm = -1
    if q0 < 1 or q1 < 1:
        if q0 < 1:
            q = q0
            norm = 1
        elif q1 < 1:
            q = q1
            norm = 999
        #Initialize x
        x = Matrix(m,VECTOR)
        #print("X:")
        #x.display()
        x.mathInsert(random.randrange(1,mathM),VECTOR,random.randrange(1,5))
        #print("X after first insertion:")
        #x.display()
        x.mathInsert(random.randrange(1,mathM)-1,VECTOR,random.randrange(1,5)+2)
        #print("X after second insertion:")
        #x.display()
        x.mathInsert(random.randrange(1,mathM)-1,VECTOR,random.randrange(1,5)+7)
        #print("X after third insertion:")
        #x.display()

        newX = copy.deepcopy(Matrix(m,VECTOR))
        condition = True
        iteration = 0
        while condition:
            iteration += 1
            newX = copy.deepcopy(Matrix(m,VECTOR))
            for i in range(1,mathM):
                newElementOfX = otherGaussSiedelSum(B,x,a,i,mathM)
                #print(">!< Haha")
                newX.mathInsert(i,VECTOR,newElementOfX)
            conditionValue = ( (q/(1-q))*computeNorm(x,newX,norm) )
            condition = conditionValue > epsilon

            '''
            print("Old x:")
            x.display()
            print("New x:")
            newX.display()
            '''

            for xIndex in range(1,mathM):
                x.mathInsert(xIndex,VECTOR,newX.mathAt(xIndex,VECTOR))

            '''
            print("X after reasignment:")
            x.display()
            '''

            #print("Iteration:",iteration," - ",conditionValue,"out of",epsilon,".")
        print("===== Other Gauss Siedel =====")
        print("Optim solution (x):")
        x.display()
        print("Test:")
        result = A.multiplyMatrix(newX)
        result.display()
        print("====================")
    else:
        print("Else Other Gauss Siedel.")


def main():
    m = 10
    A = Matrix(m,m)
    A = copy.deepcopy(fillMatrix(A))
    a = Matrix(m,1)
    a = copy.deepcopy(fillResultVector(a))
    epsilon = 10**(-10)
    p = 10

    print("The matrix A:")
    A.display()
    Jacobi(m,A,a,epsilon,p)
    GaussSiedel(m,A,a,epsilon,p)
    ConjugatedGradient(m,A,a,epsilon,p)
    otherGaussSiedel(m,A,a,epsilon,p)

if __name__ == '__main__':
    main()

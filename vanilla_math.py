

A = [[1,2,3],[4,-5,6]]
B = [[-1,0,1],[0,1,2],[-1,1,0]]

def mult(A, B):

    # matrices are only multiplyable if 
    # number of columns in A equals number of rows in B:
    A_col_count = len(A[0])
    B_row_count = len(B)
    if A_col_count != B_row_count:
        raise ValueError("Invalid inputs. Number of columns in A must match number of rows in B, but: A=" + str(A) + ", and B=" + str(B))

    # Result size is A_row_count x B_col_count
    A_row_count = len(A)
    B_col_count = len(B[0])

    # Init empty result matrix
    result=[]
    for i in range(A_row_count):
        result.append([])
        for j in range(B_col_count):
            result[i].append(0)

    row = 0
    col = 0
    for A_row in A:
        col = 0
        for B_col in zip(*B):
            dot_product = 0
            for a,b in zip(A_row, B_col):
                dot_product += a*b
            result[row][col] = dot_product
            col+= 1
        row += 1

    return result

def add(A, B):
    if len(A) != len(B):
        raise ValueError("Row count of A=" + str(len(A)) + " does not equal row count of B=" + str(len(B)))
    if len(A[0]) != len(B[0]):
        raise ValueError("Column count of A=" + str(len(A[0])) + " does not equal column count of B=" + str(len(B[0])))
    
    result = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result

# v,w must be column vectors
def dot_product(v,w):
    return sum([v[i][0]*w[i][0] for i in range(len(v))])

# Scales the matrix A elementwise
def scale(A, c):
    return [[c*a_ij for a_ij in A_row] for A_row in A]

# Retuns column i of matrix A, in column form
def getColumn(A, i):
    return [[row[i]] for row in A]

def transpose(A):
    return [list(tuple) for tuple in zip(*A)]

def unit_matrix(size):
    return [[ 1 if i==j else 0 for i in range(size)] for j in range(size)]

# Applies the given function f element wise on the column vector v
def apply_function_element_wise(f,v):
    return [[f(v[i][0])] for i in range(len(v))]


# test dot prod
#v = [[1], [-1], [2]]
#w = [[3], [1], [-2]]

#res = dot_product(v,w)
#print("Result: " + str(res))
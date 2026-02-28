import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A=np.array(A)
    trace=sum(A[i,i] for i in range(A.shape[0]))
    return trace
    pass

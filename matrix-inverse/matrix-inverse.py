import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A=np.array(A)
    if(A.ndim!=2  or  A.shape[0]!=A.shape[1] or np.isclose(np.linalg.det(A),0)):
        return None
    inv=np.linalg.inv(A)
    return inv

pass

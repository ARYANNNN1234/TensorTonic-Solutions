import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    m,n=X.shape
    w=np.zeros(n)
    b=0.0
    for i in range(steps):
        z=X@w+b
        p=_sigmoid(z)
        grad_w=(1/m)*(X.T@(p-y))
        grad_b=(1/m)*np.sum(p-y)

        w-=lr*grad_w
        b-=lr*grad_b
    # Write code here
    return (w,b)
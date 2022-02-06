import numpy as np

def L_1_norm_single_value(value, ref_value):
    return (value - ref_value)/ref_value

def L_k_norm(values, ref_values, k):
    res = 0.
    for i,j in zip(values, ref_values):
        res += (i - j)**k/j**k
    return res**(1./k)

def moving_L_k_norm(values, ref_values, k, step):
    if len(values) != len(ref_values):
        raise Exception("values and ref_values have dofferent length!")
    return np.array([L_k_norm(values[i:i+step], ref_values[i:i+step], k) for i in np.arange(len(values) - step)])
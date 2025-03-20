import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    mat = np.array(list).reshape(3, 3)
    ops = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }
    calculations = {}

    for op_name in ops:
        calculations[op_name] = [
            np.apply_along_axis(ops[op_name], axis=0, arr=mat).tolist(),
            np.apply_along_axis(ops[op_name], axis=1, arr=mat).tolist(),
            np.apply_along_axis(ops[op_name], axis=0, arr=mat.flatten()).tolist(),
        ]

    return calculations
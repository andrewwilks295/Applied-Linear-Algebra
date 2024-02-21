import numpy as np

def T0(x):
    return 0.13386706 * x[0] + 0.48665644 * x[1] - 0.44882137 * x[2] - 0.11857828 * x[3] - 0.77450658

def T1(x):
    return -0.04557434 * x[0] - 0.89097497 * x[1] + 0.44399217 * x[2] - 0.98747422 * x[3] + 2.17328698

def T2(x):
    return -0.08829271 * x[0] + 0.40431853 * x[1] + 0.00482919 * x[2] + 1.1060525 * x[3] - 2.3987804

def f(x):
    values = [T0(x), T1(x), T2(x)]
    v = np.argmax(values)
    if v == 0:
        print("Setosa")
    elif v == 1:
        print("Versicolour")
    elif v == 2:
        print("Virginica")
    
    return v

# Example usage:
x = [4,3,2,1]
print(x)
result = f(x)
print("argmax:", result)

print("----------------")

x = [1,1,1,1]
print(x)
result = f(x)
print("argmax:", result)

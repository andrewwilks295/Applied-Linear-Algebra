'''Dot product and Norms of two vectors'''
#------------------
# Andrew Wilks
# 9/8/2023
# MATH 2170
#-------------------

def rms(x):
    '''rms'''
    total = 0
    for i in range(len(x)):
        y = x[i]**2
        total += y
    answer = (total / len(x))**0.5
    return answer

def avg(x):
    '''avg'''
    total = 0
    for i in range(len(x)):
        total += x[i]
    answer = total / len(x)
    return answer

def std(x, avg):
    total = 0
    for i in range(len(x)):
        y = (x[i] - avg)**2
        total += y
    answer = (total / len(x))**0.5
    return answer

x = [67.62205015, 18.85856747, 89.87482278, 33.23317543, 67.85376642, -7.76168227, 32.4542289,
-5.69862975, 71.17102728, 22.10567789, 6.15236876, 80.30186233, 63.52505289, 46.06165362,
18.30431459, 82.95936131, 31.25160879, 34.81357958, 24.1450134, 56.96792735, 50.38486339,
62.0442239, 5.38461851, 19.41416245, 41.11320126, -5.09183741, 90.80877811, 72.99345778,
99.17639035, 72.66443221]

avg_value = avg(x)
rms_value = rms(x)
std_value = std(x, avg_value)

print("Avg:", avg_value)
print("Rms:", rms_value)
print("Std:", std_value)

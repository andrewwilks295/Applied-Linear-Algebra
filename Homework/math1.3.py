'''Dot product and Norms of two vectors'''
#------------------
# Andrew Wilks
# 3/6/2023
# MATH 2170
#-------------------
x = [5.68926168, 6.48028365, 5.64919868, 4.64594575, 9.70900398, 8.2673083,
    1.48566455, 9.48149181, 0.30697194, 8.19313516]
y = [4.12159476, -0.90500151, -1.24963052, -4.18992406, 5.47895589, 6.658136,
     -4.20026454, -7.38517255, -2.03795684, -6.02101768]
total = 0
for i in range(len(x)):
    z = x[i]*y[i]
    total += z

print("\n\n\nDot Product of x and y:", total)

total_under_sqrt_x = 0
for i in range(len(x)):
    z = x[i]**2
    total_under_sqrt_x += z
print("Norm of x:", total_under_sqrt_x**0.5)

total_under_sqrt_y = 0
for i in range(len(y)):
    z = y[i]**2
    total_under_sqrt_y += z
print("Norm of y:", total_under_sqrt_y**0.5, "\n\n\n")

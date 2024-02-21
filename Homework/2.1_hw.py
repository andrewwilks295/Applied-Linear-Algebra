#For my contribution 1, this python program can solve question 39 on
#2.1 fairly easy. You can make this a simple python problem where they
#have to find all solutions for the linear system between 0 and 20.

answers = []
b = True
for x in range(20):
    for y in range(20):
        for z in range(20):
            # print(x, y, z)
            f1 = 2 * x - y + z
            f2 = x + 3 * y - 10 * z
            f3 = -3 * x + 2 * y - 3 * z
            if f1 == 11 and f2 == 2 and f3 == -17:
                answers.append([x, y, z])
print(answers)


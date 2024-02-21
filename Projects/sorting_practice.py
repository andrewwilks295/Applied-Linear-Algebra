'''Mathletics and Computing'''
#------------------
# Andrew Wilks
# 9/6/2023
# MATH 2170
#-------------------
name_team = ["Pete Weyl from the Duschesne Determinants",
"Karla Gauss from the Tremonton Trigs",
"Hermie Wielandt from the St. George Scalars",
"Artie Cayley from the Logan Logarithms",
"Emmy Noether from the SLC SVDs",
"Evie Galois from the Ephraim Exponentials",
"Rowan ""Quaternion"" Hamilton from the Parowan Permutations",
"Dave Hilbert from the Ogden Orthogonals",
"Sophie Lie from the Manti Matrices",
"Jorge Frobenius from the Vernal Vectors",
"Izzy Schur from the Alpine Algebros",
"Stevie Humphries from the Lindon Linears",
"Mikey Muzychuk from the Tooele Tangents",
"Manny Leung from the Deseret Derivatives",
"Ollie Tamaschke from the Enterprise Inner Products"]

x = [[11,  9, 10, 13, 30], 		    #Pete Weyl
 [ 7, 17, 10,  1, 11],              #Karla Gauss
 [26, 22, 11, 22, 10],              #Hermie Wielandt
 [13, 25,  7,  1, 13],              #Artie Cayley
 [13, 9, 18, 14, 5],                #Emmy Noether
 [ 4, 14, 10, 25,  0],              #Evie Galois
 [ 9, 21, 8, 22, 19],               #Rowan "Quaternion" Hamilton
 [30, 14,  7, 24, 16],              #Dave Hilbert
 [ 3,  7, 18,  5, 11],              #Sophie Lie
 [28, 11, 25,  9, 20],              #Jorge Frobenius
 [27, 11, 29,  2, 13],              #Izzy Schur
 [ 7, 4, 10, 12, 10],               #Stevie Humphries
 [14,  2,  5,  4, 2],               #Mikey Muzychuk
 [ 5,  2, 11, 10, 10],              #Manny Leung
 [ 3, 19, 14, 19, 9]]               #Ollie Tamaschke
ranking = []
print("Scoring: (5, 4, 3, 2, 1)")
print("-------------------------------------------------------------------------")

for i in range(len(x)):
    score = 5*(x[i][0]) + 4*(x[i][1]) + 3*(x[i][2]) + 2*(x[i][3]) + 1*(x[i][4])
    ranking.append([score, i])

ranking.sort(reverse=True)
for i in range(len(ranking)):
    print(i + 1, ".", name_team[ranking[i][1]], "with", ranking[i][0])
print("-------------------------------------------------------------------------\n")

print("Scoring: (7, 4, 3, 1, 1)")
print("-------------------------------------------------------------------------")

ranking = []
for i in range(len(x)):
    score = 7*(x[i][0]) + 4*(x[i][1]) + 3*(x[i][2]) + 1*(x[i][3]) + 1*(x[i][4])
    ranking.append([score, i])

ranking.sort(reverse=True)
for i in range(len(ranking)):
    print(i + 1, ".", name_team[ranking[i][1]], "with", ranking[i][0])

print("-------------------------------------------------------------------------\n")

print("Scoring: (14, 4, 3, 2, 0)")
print("-------------------------------------------------------------------------")

ranking = []
for i in range(len(x)):
    score = 14*(x[i][0]) + 4*(x[i][1]) + 3*(x[i][2]) + 2*(x[i][3]) + 0*(x[i][4])
    ranking.append([score, i])

ranking.sort(reverse=True)
for i in range(len(ranking)):
    print(i + 1, ".", name_team[ranking[i][1]], "with", ranking[i][0])

print("-------------------------------------------------------------------------\n")

print("Scoring: (1, 1, 1, 0, 0)")
print("-------------------------------------------------------------------------")

ranking = []
for i in range(len(x)):
    score = 1*(x[i][0]) + 1*(x[i][1]) + 1*(x[i][2]) + 0*(x[i][3]) + 0*(x[i][4])
    ranking.append([score, i])

ranking.sort(reverse=True)
for i in range(len(ranking)):
    print(i + 1, ".", name_team[ranking[i][1]], "with", ranking[i][0])

# b = False
# for i in range(5):
#     if b is True:
#         break
#     for j in range(5):
#         if b is True:
#             break
#         for k in range(5):
#             if b is True:
#                 break
#             for l in range(5):
#                 if b is True:
#                     break
#                 for m in range(5):
#                     if b is True:
#                         break
#                     if i < j or j < k or k < l or l < m:
#                         break
#                     else:
#                         ranking = []
#                         for n in range(len(x)):
#                             score = i*(x[n][0]) + j*(x[n][1]) + k*(x[n][2]) + l*(x[n][3]) + m*(x[n][4])
#                             ranking.append([score, i])

#                         ranking.sort(reverse=True)
#                         print(name_team[ranking[i][1]], " ", ranking[i][0])
#                         # for i in range(len(ranking)):
#                         #     print(i + 1, ".", name_team[ranking[i][1]], "with", ranking[i][0])
#                         print("Scoring: (", i, ",", j, ",", k, ",", l,",", m,")")
#                         print("-------------------------------------------------------------------------")


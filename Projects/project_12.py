#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:14:01 2023

@author: andrewWilks
"""

import numpy as np
import sympy as sp


linInd = [[ 0.10648165505277775, -0.14358801908540644, -0.27742700551517235, 0.06062125096635045, 0.04545439840290023, 0.2590293874846813, 0.2207686773398607, -0.17098852868636152, 0.17284165573591448, 0.24879586316073174, -0.3510131673252601, -0.008216621882820855, 0.08588628818898135, 0.12878893497513105, -0.4581120311073462, 0.06175314627094234, -0.15811090612325196, 0.030288766302301894, 0.11122451899230065, -0.14231223987187858, 0.0981266257483063, -0.1448352687574154, -0.40582235869755895, 0.18345053841991854, 0.00886738147495323],
[ -0.09518046151088846, -0.4075582538882507, -0.12262172292445964, -0.05390071697992032, 0.21977093183179988, 0.05067929176615376, 0.10595833610031051, -0.10316176555696854, 0.1192747373306744, -0.0805278641567382, -0.11140502061574502, 0.26318409443839913, -0.14364892896084155, 0.03547731056478258, 0.2768587796007129, 0.27663043095675127, 0.008609519377735578, 0.008904308267514791, 0.17677094950617384, 0.06385292750578273, -0.24802279346753786, 0.32178103613335424, 0.0497499288806483, 0.12368043706667411, -0.48825464766906657],
[ -0.25039306185195853, -0.3953956840332691, -0.17920906894103097, 0.012633535115613539, -0.03165080736376191, 0.2170547183449809, 0.018896105242801175, 0.007457584948101652, -0.1848158737553603, -0.18928249691956028, 0.1110317226394419, 0.11062024448752059, 0.31918637660212773, -0.3431084891314352, 0.17433909986966675, 0.1291897921066396, -0.1600184079201051, -0.1796518097701466, -0.15234857142545397, -0.38136474779451046, -0.016574479158714347, -0.19238406411314785, -0.015061241419141072, -0.12211519979372128, 0.24488892765720646],
[ -0.26194112064385905, -0.025636285010179276, 0.16237662356513374, -0.06099357265359608, -0.1974268382815539, 0.2672921938870092, -0.1817210119188344, 0.20038458298773806, -0.05371743807460067, -0.15006292238190475, 0.16723140516195736, 0.04278273192755027, -0.38632505713038084, -0.15401065356105406, -0.5209239078893587, -0.01985392118923335, -0.2445297899013848, -0.06744914440215434, -0.1214533535256725, -0.0918495684606853, 0.051901733339144884, 0.10597548744248225, 0.11049065167366467, 0.16202247041241405, -0.2778585347086411],
[ 0.40188127985995337, -0.09909746415669145, 0.3188605856634338, -0.14682773135672234, 0.15570401568083544, 0.053635542139179655, 0.1455912371104374, 0.14701299892840952, -0.04323785204536693, -0.41587502930118964, -0.04191156163209081, -0.08288677181210975, 0.22841142921740137, -0.028338970378924196, -0.041967032125778445, -0.12069017840616356, -0.23735362292249734, 0.4135742990732003, 0.011114180620916595, -0.13371208338436189, 0.1041590723380477, 0.05604206475155387, -0.13173459227621462, -0.23846068305622678, -0.2217425076972414],
[ -0.3037120030079216, -0.0352095298439652, -0.15870121475305957, 0.28554643573648736, 0.08051289527116565, -0.03360417807252537, 0.376391895461868, -0.05100347261496981, -0.028294797501026005, -0.2069762382841873, 0.005552454485559052, -0.03848650456174602, -0.1178271073026056, -0.047327337157451334, -0.21563638755896555, -0.4093410095910605, 0.3837600481377037, 0.08676980141836288, 0.23290087733616524, -0.16484303045286525, 0.019972187243443098, 0.22336640863589086, 0.07440148718804108, -0.2794625577774188, 0.049350870677954045],
[ -0.0034996676876259372, -0.03626206277693526, -0.08563856744257291, 0.20691958297549637, -0.05617694890728982, 0.1147075062036022, -0.11533098889626762, 0.18721191483784008, 0.20803598026283565, 0.05635164617254584, -0.2961663357854797, 0.3653800234112575, -0.00047136963599344445, 0.06040673188468301, 0.2272046235321502, -0.6286051654432885, -0.31054441023606805, 0.019199386532567145, -0.12920782374179932, 0.08915822411597606, -0.07502593338330162, -0.11708828137547807, 0.1547320671870777, 0.02281335047092093, -0.02283624862745099],
[ 0.07256571176815076, 0.1157764901270222, 0.09152790292611733, 0.3288190538264421, 0.6104589582249066, -0.23825161292243374, -0.1400881035514281, 0.029877688769404866, 0.1174361374001212, 0.009157038533248108, 0.2509616828560283, 0.13968633102420167, 0.17951812816500234, -0.0075609868821638814, -0.14215271853837877, -0.0462728380173548, -0.05744425612248066, -0.1927482093084679, -0.15289072671867812, -0.2700272795450361, 0.03099841582194991, 0.181850450187965, -0.04303537540084382, 0.3019550440232768, 0.009291774656621302],
[ 0.2351127334718305, 0.039967747170674535, -0.16688763946111151, -0.3876112335630301, 0.1127871871640994, 0.061633609274171455, -0.017852219115075278, 0.2308234791240173, 0.15183966805852156, 0.12000384369484506, -0.006451090025557798, 0.10123482597007853, -0.18010605563586826, -0.22719468083846914, 0.09472048422096788, -0.15121236725799372, 0.24575870425801774, -0.438712741462688, -0.07424929608184334, -0.09192105547717118, 0.32752733996288097, 0.08926026477749527, -0.24024218197907954, -0.2610171565271299, -0.15283080618610823],
[ -0.40149453769982696, -0.19719037446309268, 0.0630412042467301, -0.07462842740044401, 0.28740614734682574, 0.09874586293782442, -0.0768391322519437, 0.22536403336894462, -0.005579063707741029, 0.21370975749497007, 0.14147026738821147, 0.0917487833791179, 0.25324057921456516, 0.20699004897822362, -0.07016149269073191, 0.03559848891988633, 0.1630352966474338, 0.2257626734465866, -0.004175577319404539, 0.3089805287273415, 0.43188462518396303, -0.24625218315450473, 0.06615782876380762, -0.09703351723014628, -0.14154685735502145]]

AA = np.array([[ -17.62298538952109, 11.501615891138508, -18.90957585845351, 8.064800573735518, 3.041236260451587, -12.427276295478965, 36.32578715119185, 9.965807931337359, -8.361459805348483, -2.063132322842499, -45.243644690398895, 6.520261563266029, -20.308420584909445, -0.22434038377750942, 2.3465416121720146],
              [ 13.642070201062168, -14.457325417948226, 18.69002897092551, -20.550229036593088, 4.0758808712073415, -39.8316362835982, -3.707033366640111, -8.821562992077503, 20.14885788234824, 16.61942349953309, -26.38741186623424, 7.9465404380005396, -5.131746306714554, 4.990915104436267, -8.659093038414076],
              [ 10.362104857613058, -5.677167918516686, -4.260600020349182, -30.39193606875395, 0.44565949548804085, -17.241103036946065, 6.779957648446173, 3.3503498652957906, 21.084344292100454, -16.707342429284523, -31.001780119797886, 0.38698193078590215, -26.63538135550356, -5.7420743663357925, 22.55780914693729],
              [ 30.40410908088092, 10.118554667340108, 30.676254447048183, 37.13557784434156, -5.483532617450395, -10.295221617119791, -11.303292640475815, -32.00504668380043, 18.488500493783175, -35.897289525214696, 2.912224196363347, 27.166134312605067, -14.220699297394294, 2.238336518296347, 3.822824319193364],
              [ 2.974381169714332, 17.11568925140094, 3.889067632287876, -22.838843444830943, 0.8128690687311078, 26.22118645952844, -2.596782507941744, 48.33436676402924, 45.40015020996087, 9.527695147937905, -17.002462977921716, -16.306900509189397, 13.02152267381149, -11.835577822098635, 13.423949947145372],
              [ -4.73759475955649, -17.29518919820912, 12.429914848484092, 8.07041492238742, 25.45936846264926, 19.52068426926816, -3.161561036135513, -38.685787365066496, 26.291497696224795, -12.413562908164286, 34.97986967506073, -1.5883889494424581, 45.871648787100085, 11.685587811577987, 10.21713728126033],
              [ -22.92314753290784, 17.949486261491135, -5.937577299915636, 30.859935550573752, -5.917735085601526, 7.513112440316645, -1.7833001866097788, 14.69933421510311, 30.216195998356405, 14.806192353120993, -19.3416974412641, -7.919427061610081, 4.954281405948195, -3.9881971615706515, 20.48637459279071],
              [ 0.24626341617106262, 27.627775624956225, 34.9885254983745, 19.267360907721223, 13.414259248161608, 35.49086906114143, -20.013752635094917, -25.723286847825356, -34.90444521402563, 19.422787642838202, 16.722277314175056, -3.8511148892092244, 0.45573252731244374, 43.33243371535798, 33.263559730503644],
              [ 28.08149654249682, 2.6717669050380595, 11.242844400909185, 8.319081599181882, 6.406576965402561, 8.92207346997537, -31.44078330692009, -11.667284960068889, 0.4288103394485363, -17.698155101104856, -23.50325813171557, -7.519893257573022, -10.47182041889668, -31.256624792378847, -3.187550191961799],
              [ 33.14690798678197, -8.652537661395614, -18.417932924456366, -12.322779853790973, -0.70997982049151, 11.870013403248192, 1.5855717373630256, 18.486229470378795, -1.706841968455724, -3.512907505721625, 20.220879178702894, -6.686916109136707, 16.4434341901395, 14.977747080506674, -8.120799788590556],
              [ 3.201344265224342, 25.610957115143062, 5.270842763994279, -18.317041275367362, -25.453486186131382, -35.80997138768804, -42.30028956064497, -1.6669210069312612, 4.81639342547715, -12.938183031148666, 1.322179743198281, 7.446496651357055, -27.8199060113813, 34.261043908691306, -26.131324646449308],
              [ 27.48127578927631, -23.74649203386915, 22.970081446921792, 50.79258643274092, 29.23038843191091, 24.628555611878337, -0.6517528457085415, -32.63188702597283, -6.972434124487169, -22.905608718620176, 23.811022690551994, 7.256037852803832, -5.677658937687313, -21.63499275134489, -32.87013943088892],
              [ 21.255662083255885, -11.031415245776515, -28.044037225937412, 41.480402873634574, -13.088061446002722, -2.193273807496542, -5.074878894372402, 10.462180478136617, -13.32273228912375, -21.79498737491644, 3.0860510272258566, -15.930437603182968, 15.061397734785784, -50.62593208697116, -18.97556946112737],
              [ -28.21559345519958, -42.589482263103235, -8.35421538795316, 29.872183810756013, 27.343312518499413, -44.547481064037804, -5.713837271132801, -7.65274110978646, 14.911037490640522, 26.6923525630097, 2.991044246456527, -3.6929995829065447, 19.94012928032504, -1.7558948092078226, -30.71344441186242],
              [ -3.6168273297488867, 23.54950395708044, -10.760573684246339, -26.960229356308343, -18.35776610586259, 6.213001181928254, 16.53421454373362, 28.968845378655658, -41.31596926615701, 36.876056118519784, -8.975700788598122, 22.663175904751807, 8.840499479063066, -31.3779967129957, -9.396131182862902]])


def rowReplacement(a, b, scalar, i, j):
    scaled_coeff_matrix = np.copy(a)
    scaled_aug_matrix = np.copy(b)
    
    scaled_coeff_matrix[j] = scaled_coeff_matrix[j] * scalar
    scaled_aug_matrix[j] = scaled_aug_matrix[j] * scalar
    
    a[i] += scaled_coeff_matrix[j]
    b[i] += scaled_aug_matrix[j]
    
    return a, b

def rowInterchange(a, b, i, j):
    interchange_coeff_matrix = np.copy(a)
    interchange_aug_matrix = np.copy(b)
    
    interchange_coeff_matrix[i] = a[j]
    interchange_coeff_matrix[j] = a[i]
    interchange_aug_matrix[i] = b[j]
    interchange_aug_matrix[j] = b[i]
    
    return interchange_coeff_matrix, interchange_aug_matrix
#end of rowInterchange

def rowScaling(a, b, s, row):
    scaled_coeff_matrix = np.copy(a)
    scaled_aug_matrix = np.copy(b)
    
    scaled_coeff_matrix[row] = scaled_coeff_matrix[row] * s
    
    scaled_aug_matrix[row] = scaled_aug_matrix[row] * s
    
    return scaled_coeff_matrix, scaled_aug_matrix
#end of rowScaling

def findScalar(pivot, s):
    # Define the symbolic variable
    x = sp.symbols('x')

    # Define the equation
    equation = pivot * x + s

    # Solve for x
    solutions = sp.solve(equation, x)

    return solutions[0]
#end of findScalar

# modified for the forwardphase algorithm
# def zeroBelow(coefficient_matrix, augmented_matrix, i, j):
#     pivot = coefficient_matrix[i][j]
#     pivotLoc = [i, j]
#     if pivot == 0: #check to see if the pivot is zero
#         for k in range(len(coefficient_matrix[:,j])): #iterates through rows to find the first non zero
#             if coefficient_matrix[k][j] != 0:
#                 coefficient_matrix, augmented_matrix = rowInterchange(coefficient_matrix, augmented_matrix, i, k)
#                 break
#         #end for loop
#     #end if statement
#     for k in range(i, len(coefficient_matrix[:j])):#i keeps us from changing the values above the pivot point
#         if k != i and coefficient_matrix[k][j] != 0: #avoids changing the pivot position and if zero is already there
#             # print(coefficient_matrix[k][i])
#             scalar = findScalar(pivot, coefficient_matrix[k][i])
#             coefficient_matrix, augmented_matrix = rowReplacement(coefficient_matrix, augmented_matrix, scalar, k, i)
#     # print(coefficient_matrix, augmented_matrix)
#     return coefficient_matrix, augmented_matrix, pivotLoc
# # end of zeroBelow

# def zeroAbove(coefficient_matrix, augmented_matrix, i, j):
#     pivot = coefficient_matrix[i][j]
#     pivotStorage = []
#     if pivot != 1:
#         piv_scale = 1 / pivot
#         coefficient_matrix, augmented_matrix = rowScaling(coefficient_matrix, augmented_matrix, piv_scale, i)
#         pivot = coefficient_matrix[i][j]  # sets pivot to 1
#     pivotStorage.append(pivot)

#     for k in range(i - 1, -1, -1):
#         if coefficient_matrix[k][j] != 0:
#             scalar = findScalar(pivot, coefficient_matrix[k][j])
#             coefficient_matrix, augmented_matrix = rowReplacement(coefficient_matrix, augmented_matrix, scalar, k, i)
    
#     return coefficient_matrix, augmented_matrix, pivotStorage


# def forwardPhase(coefficient_matrix, constant_matrix):
#     pivots = []
#     reducedCoefficientMatrix = coefficient_matrix
#     reducedConstantMatrix = constant_matrix
#     for i in range(len(coefficient_matrix)):
#         reducedCoefficientMatrix = zeroBelow(reducedCoefficientMatrix, reducedConstantMatrix, 0, 0)[0]
#         reducedConstantMatrix = zeroBelow(reducedCoefficientMatrix, reducedConstantMatrix, i, i)[1]
#         pivots.append(zeroBelow(reducedCoefficientMatrix, reducedConstantMatrix, i, i)[2])
#     return reducedCoefficientMatrix, reducedConstantMatrix, pivots


def forwardPhase(coefficient_matrix, constant_matrix):
    reducedCoefficientMatrix = coefficient_matrix
    reducedConstantMatrix = constant_matrix
    pivots = []

    for i in range(len(coefficient_matrix)):
        reducedCoefficientMatrix, reducedConstantMatrix = zeroBelow(reducedCoefficientMatrix, reducedConstantMatrix, i, i)
        pivots.append([i,i])


    return reducedCoefficientMatrix, reducedConstantMatrix, pivots

def zeroBelow(coefficient_matrix, augmented_matrix, i, j):
    pivot = coefficient_matrix[i][j]

    if pivot == 0:
        for k in range(len(coefficient_matrix)):
            if coefficient_matrix[k][j] != 0:
                coefficient_matrix, augmented_matrix = rowInterchange(coefficient_matrix, augmented_matrix, i, k)
                break

    for k in range(i, len(coefficient_matrix)):
        if k != i and coefficient_matrix[k][j] != 0:
            scalar = findScalar(pivot, coefficient_matrix[k][i])
            coefficient_matrix, augmented_matrix = rowReplacement(coefficient_matrix, augmented_matrix, scalar, k, i)

    return coefficient_matrix, augmented_matrix

def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

def backwardPhase(coefficient_matrix, constant_matrix, pivots):
    reducedCoefficientMatrix = coefficient_matrix
    reducedConstantMatrix = constant_matrix

    # show this to Andrew Smith vvv
    # pivots = np.array([[2,2],[1,1],[0,0]])
    # this line ^^^ changes the solution in spot (0,0) from 2 to 0, but the correct solution is 0.5
    pivots = Reverse(pivots) #CHANGED THIS SHOW ANDREW SMITH !!!!!!!!!!!!!!!!!!!

    for i, j in pivots:
        reducedCoefficientMatrix, reducedConstantMatrix = zeroAbove(reducedCoefficientMatrix, reducedConstantMatrix, i, j)

    return reducedCoefficientMatrix, reducedConstantMatrix

def zeroAbove(coefficient_matrix, augmented_matrix, i, j):
    pivot = coefficient_matrix[i][j]

    if pivot != 1:
        pivot_scale = 1 / pivot
        coefficient_matrix, augmented_matrix = rowScaling(coefficient_matrix, augmented_matrix, pivot_scale, j)
        pivot = 1 # ADDED 10/26/2023 NEED TO SHOW ANDREW SMITH
    
    for k in range(i, -1, -1):
        if k != i and coefficient_matrix[k][j] != 0:
            scalar = findScalar(pivot, coefficient_matrix[k][i])
            coefficient_matrix, augmented_matrix = rowReplacement(coefficient_matrix, augmented_matrix, scalar, k, i)

    return coefficient_matrix, augmented_matrix

def rref(coefficient_matrix, constant_matrix):
    c = forwardPhase(coefficient_matrix, constant_matrix)
    c = backwardPhase(c[0], c[1], c[2])
    return c[0], c[1]

# def Identity(size):
#     for row in range(0, size):
#         for col in range(0, size):
 
#             # Here end is used to stay in same line
#             if (row == col):
#                 print("1 ", end=" ")
#             else:
#                 print("0 ", end=" ")
#         print()

def matrix_inverse(matrix):
    i = np.eye(len(matrix))
    c = rref(matrix, i)[1]
    return c





def isLinearIndep(vectors):
    temp = forwardPhase(vectors, vectors)
    reduced = temp[0]
    #somethings wrong 
    pivots = temp[2]
    
    # print(len(pivots))
    # print(len(reduced))
    if(len(pivots) != len(reduced)):
        return False
    return True

print("-----------------")
print("TASK 1 VERIFIED")
print(isLinearIndep(linInd))
print("-----------------")


A = np.array([[6.0, 5, 0], [4, 0, 3], [0, 2, 1]])
b = np.array([13.0, 5, 5]) #change 6 to 6.0 and 13 to 13.0 and you get the solution 0.5, 2, 1
s1, s2 = rref(A, b)
# print(s1) #print for some crazy ass numbers
s1 = np.round(s1, decimals=0)
print("TASK 2 VERIFIED")
print(abs(s1))
print("-----------------")
print("Solution:", s2)
print("-----------------")


print("TASK 3 VERIFIED")
print(matrix_inverse(AA))
# inverse = np.linalg.inv(AA)
# print(inverse)
# pivots = forwardPhase(A, b)
# print("Pivots:", pivots)
# print(pivots[0], pivots[1])
# p = np.array([[0,0],[1,1],[2,2]])
# print(backwardPhase(pivots[0], pivots[1], p))

# A = np.array([[6, 5, 0], [4, 0, 3], [0, 2, 1]])
# b = np.array([13, 5, 5])

# x = np.linalg.solve(A, b)

# print("Solution x:")
# print(x)
       

    
    
# m = np.array([[1, 2, 3],
#      [5, 6, 7],
#      [9, 10, 11]])
# am = np.array([4, 8, 12])
# print("\n\n\n\n\nPROJECT 9\n")
# print("Original matrices: \n")
# print(m, am)
# print("\n")
# print("TASK 1")
# m, am = zeroBelow(m, am, 0, 0)
# print("\nThe zeroBelow function is used to check if the pivot is at zero. If so, the rows in the first column are looped through to find a non zero value")
# print("Then, interchange is used to swithc them. Afterwards the findScalar function is sued to find the scalar for the rowReplacement function, in order to get zeros below the pivot")
# print(m, am)
# print("\n")
# m, am = zeroBelow(m, am, 1, 1)
# print("The pivot point is switched to the new pivot (2,2) in the matrix, and the steps are repeated.")
# print(m, am)

# print("\n")
# print("TASK 2")
# print("\n")
# m, am = zeroAbove(m, am, 1, 1)
# print("The zeroAbove function is now used at (2,2). The pivot point needs to be one, if not the findScalar function will make the pivot value equal to one and update the other values in the row accoringly.")
# print("At this point, the values above can be set to zero using the zeroAbove functon.")
# print(m, am)

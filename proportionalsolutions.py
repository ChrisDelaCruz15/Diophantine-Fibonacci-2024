# sym.init_printing[]
# e,f = sym.symbols['e,f']
# eq1 = sym.Eq[e**3 + 3*e*f**2 + f**3, 1080]
# eq2 = sym.Eq[3*e**2*f + 3*e*f**2 + 2*f**3, 1728]
# ans = sym.solve[[eq1, eq2], [e,f]]
# print[ans[0]]
# e,f = sym.symbols['e,f']
# eq1 = e**3 + 3*e*f**2 + f**3
# eq2 = 3*e**2*f + 3*e*f**2 + 2*f**3
# A = np.array[[[1, 3, 1, 0], [0, 3, 2, 3]]]
# b = np.array[[1080, 1728]]
# x = np.linalg.solve[A, b]
# print[x]

# counter = 1
# for a in range[1, 7]:

#     for b in range[1, 7]:

#         for c in range[4, 7]:

#             for d in range [2, 7]:

#                 coef1 = a**3 + 3*a*b**2 + b**3 + c**3 + 3*c*d**2 + d**3
#                 coef2 = 3*a**2*b + 3*a*b**2 + 2*b**3 + 3*c**2*d + 3*c*d**2 + 2*d**3
#                 e,f = sym.symbols['e,f']
#                 eq1 = sym.Eq[e**3 + 3*e*f**2 + f**3, coef1]
#                 eq2 = sym.Eq[3*e**2*f + 3*e*f**2 + 2*f**3, coef2]
#                 ans = sym.solve[[eq1, eq2], [e,f], warn=True]
#                 print[f"#{counter}. [{coef1} + {coef2}t], [{a}, {b}, {c}, {d}] -> {ans[0]}"]
#                 counter += 1    
# 5,6,4,3

# a,b,c,d = 12,22,6,14
# coef1 = a**3 + 3*a*b**2 + b**3 + c**3 + 3*c*d**2 + d**3
# coef2 = 3*a**2*b + 3*a*b**2 + 2*b**3 + 3*c**2*d + 3*c*d**2 + 2*d**3
# e,f = sym.symbols['e,f']
# eq1 = sym.Eq[e**3 + 3*e*f**2 + f**3, coef1]
# eq2 = sym.Eq[3*e**2*f + 3*e*f**2 + 2*f**3, coef2]
# ans = sym.solve[[eq1, eq2], [e,f]]
       


# a,b,c,d = 8,7,10,12
# eq1 = a**3 + 3*a*b**2 + b**3 + c**3 + 3*c*d**2 + d**3
# eq2 = 3*a**2*b + 3*a*b**2 + 2*b**3 + 3*c**2*d + 3*c*d**2 + 2*d**3
# e,f = sym.symbols['e,f']
# print[coef1, coef2]
# eq1 = sym.Eq[e**3 + 3*e*f**2 + f**3, coef1]
# eq2 = sym.Eq[3*e**2*f + 3*e*f**2 + 2*f**3, coef2]
#print[solve_poly_system[[eq1, eq2], e, f, strict=True]]

# max = 5
# count = 0

# for a in range[0, max]:

#     for b in range[0, max]:

#         for c in range[0, max]:

#             for d in range [0, max]:
                
#                 for e in range [0, max]:

#                     for f in range [1, max]:

#                         eq1 = a**3 + 3*a*b**2 + b**3 + c**3 + 3*c*d**2 + d**3 - e**3 - 3*e*f**2 - f**3
#                         eq2 = 3*a**2*b + 3*a*b**2 + 2*b**3 + 3*c**2*d + 3*c*d**2 + 2*d**3 - 3*e**2*f - 3*e*f**2 - 2*f**3

#                         if eq1 == 0:

#                             if eq2 == 0:

#                                 print[f"{count}. [{a}, {b}, {c}, {d}, {e}, {f}]"]

#                         count += 1

# Pick Solutions

# a, b, c, d, e, f = 2,11,7,16,6,18
# a_prime, b_prime, c_prime, d_prime, e_prime, f_prime = 7,16,2,11,6,18

# # Calculate Norms

# norms1 = a**2 +a*b - b**2
# norms2 = c**2 + c*d - d**2
# norms3 = e**2 + e*f - f**2
# norms1_prime = a_prime**2 + a_prime*b_prime - b_prime**2
# norms2_prime = c_prime**2 + c_prime*d_prime - d_prime**2
# norms3_prime = e_prime**2 + e_prime*f_prime - f_prime**2

# Check if each of the norms are all proportional to each other.

def is_proporitional(solution, solution_prime):
    a, b, c, d, e, f = solution[0], solution[1], solution[2], solution[3], solution[4], solution[5] 
    a_prime, b_prime, c_prime, d_prime, e_prime, f_prime = solution_prime[0], solution_prime[1], solution_prime[2], solution_prime[3], solution_prime[4], solution_prime[5]

    norms1 = a**2 +a*b - b**2
    norms2 = c**2 + c*d - d**2
    norms3 = e**2 + e*f - f**2
    norms1_prime = a_prime**2 + a_prime*b_prime - b_prime**2
    norms2_prime = c_prime**2 + c_prime*d_prime - d_prime**2
    norms3_prime = e_prime**2 + e_prime*f_prime - f_prime**2

    if norms1 >= norms1_prime:
        if norms1 % norms1_prime!= 0:
            print("not proportional")
            return False
    else:    
        if norms1_prime % norms1 != 0:
            print("not proportional")
            return False

    if norms2 >= norms2_prime:
        if norms2 % norms2_prime!= 0:
            print("not proportional")
            return False
    else:    
        if norms2_prime % norms2 != 0:
            print("not proportional")
            return False

    if norms3 >= norms3_prime:
        if norms3 % norms3_prime!= 0:
            print("not proportional")
            return False
    else:    
        if norms3_prime % norms3 != 0:
            print("not proportional")
            return False
    print("proportional")
    return True

solutions_max25 = [
[1, 15, 8, 21, 6, 24],
[2, 11, 7, 16, 6, 18],
[3, 7, 6, 11, 6, 12],
[4, 3, 5, 6, 6, 6],
[5, 6, 4, 3, 6, 6],
[6, 11, 3, 7, 6, 12],
[6, 14, 12, 22, 12, 24],
[7, 10, 11, 17, 12, 18],
[7, 16, 2, 11, 6, 18],
[8, 6, 10, 12, 12, 12],
[8, 21, 1, 15, 6, 24],
[9, 2, 9, 7, 12, 6],
[9, 7, 9, 2, 12, 6],
[10, 12, 8, 6, 12, 12],
[11, 13, 16, 23, 18, 24],
[11, 17, 7, 10, 12, 18],
[12, 9, 15, 18, 18, 18],
[12, 22, 6, 14, 12, 24],
[13, 5, 14, 13, 18, 12],
[13, 8, 14, 1, 18, 6],
[14, 1, 13, 8, 18, 6],
[14, 13, 13, 5, 18, 12],
[15, 18, 12, 9, 18, 18],
[16, 12, 20, 24, 24, 24],
[16, 23, 11, 13, 18, 24],
[17, 8, 19, 19, 24, 18],
[18, 4, 18, 14, 24, 12],
[18, 14, 18, 4, 24, 12],
[19, 19, 17, 8, 24, 18],
[20, 24, 16, 12, 24, 24]
]

newlist = []
for i in solutions_max25:
    counter = 0
    for j in solutions_max25:
        print(f"is {i} proportional to {j}? ", end="")
        if is_proporitional(i, j):
            break
        else:
            counter += 1
    if counter == 0:
        print("Not proportional to anything.")
        newlist.append(i)

solutions_max50 = [[1, 15, 8, 21, 6, 24],
[2, 11, 7, 16, 6, 18],
[2, 30, 16, 42, 12, 48],
[3, 7, 6, 11, 6, 12],
[3, 26, 15, 37, 12, 42],
[4, 3, 5, 6, 6, 6],
[4, 22, 14, 32, 12, 36],
[5, 6, 4, 3, 6, 6],
[5, 18, 13, 27, 12, 30],
[6, 11, 3, 7, 6, 12],
[6, 14, 12, 22, 12, 24],
[7, 10, 11, 17, 12, 18],
[7, 16, 2, 11, 6, 18],
[7, 29, 20, 43, 18, 48],
[8, 6, 10, 12, 12, 12],
[8, 21, 1, 15, 6, 24],
[8, 25, 19, 38, 18, 42],
[9, 2, 9, 7, 12, 6],
[9, 7, 9, 2, 12, 6],
[9, 21, 18, 33, 18, 36],
[10, 12, 8, 6, 12, 12],
[10, 17, 17, 28, 18, 30],
[11, 13, 16, 23, 18, 24],
[11, 17, 7, 10, 12, 18],
[12, 9, 15, 18, 18, 18],
[12, 22, 6, 14, 12, 24],
[12, 28, 24, 44, 24, 48,],
[13, 5, 14, 13, 18, 12,],
[13, 8, 14, 1, 18, 6],
[13, 24, 23, 39, 24, 42],
[13, 27, 5, 18, 12, 30],
[14, 1, 13, 8, 18, 6],
[14, 13, 13, 5, 18, 12],
[14, 20, 22, 34, 24, 36],
[14, 32, 4, 22, 12, 36],
[15, 16, 21, 29, 24, 30],
[15, 18, 12, 9, 18, 18],
[15, 37, 3, 26, 12, 42],
[16, 12, 20, 24, 24, 24],
[16, 23, 11, 13, 18, 24],
[16, 42, 2, 30, 12, 48],
[17, 8, 19, 19, 24, 18],
[17, 27, 28, 45, 30, 48],
[17, 28, 10, 17, 18, 30],
[18, 4, 18, 14, 24, 12],
[18, 14, 18, 4, 24, 12],
[18, 23, 27, 40, 30, 42],
[18, 33, 9, 21, 18, 36],
[19, 19, 17, 8, 24, 18],
[19, 19, 26, 35, 30, 36],
[19, 38, 8, 25, 18, 42],
[20, 15, 25, 30, 30, 30],
[20, 24, 16, 12, 24, 24],
[20, 43, 7, 29, 18, 48],
[21, 11, 24, 25, 30, 24],
[21, 29, 15, 16, 24, 30],
[22, 7, 23, 20, 30, 18],
[22, 15, 23, 3, 30, 12],
[22, 26, 32, 46, 36, 48],
[22, 34, 14, 20, 24, 36],
[23, 3, 22, 15, 30, 12],
[23, 20, 22, 7, 30, 18],
[23, 22, 31, 41, 36, 42],
[23, 39, 13, 24, 24, 42],
[24, 18, 30, 36, 36, 36],
[24, 25, 21, 11, 30, 24],
[24, 44, 12, 28, 24, 48],
[25, 14, 29, 31, 36, 30],
[25, 30, 20, 15, 30, 30],
[26, 10, 28, 26, 36, 24],
[26, 16, 28, 2, 36, 12],
[26, 35, 19, 19, 30, 36],
[27, 6, 27, 21, 36, 18],
[27, 21, 27, 6, 36, 18],
[27, 25, 36, 47, 42, 48],
[27, 40, 18, 23, 30, 42],
[28, 2, 26, 16, 36, 12],
[28, 21, 35, 42, 42, 42],
[28, 26, 26, 10, 36, 24],
[28, 45, 17, 27, 30, 48],
[29, 17, 34, 37, 42, 36],
[29, 31, 25, 14, 36, 30],
[30, 13, 33, 32, 42, 30],
[30, 17, 33, 1, 42, 12],
[30, 36, 24, 18, 36, 36],
[31, 9, 32, 27, 42, 24],
[31, 22, 32, 5, 42, 18],
[31, 41, 23, 22, 36, 42],
[32, 5, 31, 22, 42, 18],
[32, 24, 40, 48, 48, 48],
[32, 27, 31, 9, 42, 24],
[32, 46, 22, 26, 36, 48],
[33, 1, 30, 17, 42, 12],
[33, 20, 39, 43, 48, 42],
[33, 32, 30, 13, 42, 30],
[34, 16, 38, 38, 48, 36],
[34, 37, 29, 17, 42, 36],
[35, 12, 37, 33, 48, 30],
[35, 23, 37, 4, 48, 18],
[35, 42, 28, 21, 42, 42],
[36, 8, 36, 28, 48, 24],
[36, 28, 36, 8, 48, 24],
[36, 47, 27, 25, 42, 48],
[37, 4, 35, 23, 48, 18],
[37, 33, 35, 12, 48, 30],
[38, 38, 34, 16, 48, 36],
[39, 43, 33, 20, 48, 42],
[40, 48, 32, 24, 48, 48]]

print(newlist)


# for i in range(0, len(solutions)):
#     print(i)
#     for j in range(0, len(solutions)):
#         is_proporitional(i, j)

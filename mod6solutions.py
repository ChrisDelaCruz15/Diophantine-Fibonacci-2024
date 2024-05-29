

solutions_list = []

count = 0
count2 = 0
max = 6

# Consider all possible 6^6 combinations of terms

for a in range(0, max):

    for b in range(0, max):

        for c in range(0, max):

            for d in range (0, max):
                
                for e in range (0, max):

                    for f in range (0, max):

                        # Check if the system of equations holds

                        eq1 = a**3 + 3*a*b**2 + b**3 + c**3 + 3*c*d**2 + d**3 - e**3 - 3*e*f**2 - f**3
                        eq2 = 3*a**2*b + 3*a*b**2 + 2*b**3 + 3*c**2*d + 3*c*d**2 + 2*d**3 - 3*e**2*f - 3*e*f**2 - 2*f**3

                        '''
                        Note: This script originally had conditions "if eq1 == 0" and "if eq2 == 0"
                        Because we're dealing with modulus 6 equations, considered all numbers divisible by 6 as 0. 
                        '''

                        if (eq1 % 6) == 0: 

                            if (eq2 % 6) == 0:

                                print(f"[{a}, {b}, {c}, {d}, {e}, {f}]")
                                solutions_list.append([(a),(b),(c),(d),(e),(f)])
                                
                                count2 += 1

                        count += 1

print(count)
print(count2)
for i in solutions_list:
    print(f"{i}", end=".")
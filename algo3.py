import math
T = (1+math.sqrt(5))/2

# Step 1: Calculate first list of (x, y, z) with |N(z)| > |N(x)|,|N(y)| 

solutions_list = [
[1, -14, 8, -13, 6, -18 , -209, -209, -396],
[1, 15, 8, 21, 6, 24 , -209, -209, -396],
[2, -9, 7, -9, 6, -12 , -95, -95, -180],
[2, 11, 7, 16, 6, 18 , -95, -95, -180],
[3, -4, 6, -5, 6, -6 , -19, -19, -36],
[3, 7, 6, 11, 6, 12 , -19, -19, -36],
[4, -18, 14, -18, 12, -24 , -380, -380, -720],
[4, 1, 5, -1, 6, 0 , 19, 19, 36],
[4, 3, 5, 6, 6, 6 , 19, 19, 36],
[5, -13, 13, -14, 12, -18 , -209, -209, -396],
[5, -1, 4, 1, 6, 0 , 19, 19, 36],
[5, 6, 4, 3, 6, 6 , 19, 19, 36],
[6, -8, 12, -10, 12, -12 , -76, -76, -144],
[6, -5, 3, -4, 6, -6 , -19, -19, -36],
[6, 11, 3, 7, 6, 12 , -19, -19, -36],
[6, 14, 12, 22, 12, 24 , -76, -76, -144],
[7, -9, 2, -9, 6, -12 , -95, -95, -180],
[7, -3, 11, -6, 12, -6 , 19, 19, 36],
[7, 10, 11, 17, 12, 18 , 19, 19, 36],
[7, 16, 2, 11, 6, 18 , -95, -95, -180],
[8, -17, 19, -19, 18, -24 , -361, -361, -684],
[8, -13, 1, -14, 6, -18 , -209, -209, -396],
[8, 2, 10, -2, 12, 0 , 76, 76, 144],
[8, 6, 10, 12, 12, 12 , 76, 76, 144],
[8, 21, 1, 15, 6, 24 , -209, -209, -396],
[9, -12, 18, -15, 18, -18 , -171, -171, -324],
[9, 2, 9, 7, 12, 6 , 95, 95, 180],
[9, 7, 9, 2, 12, 6 , 95, 95, 180],
[10, -7, 17, -11, 18, -12 , -19, -19, -36],
[10, -2, 8, 2, 12, 0 , 76, 76, 144],
[10, 12, 8, 6, 12, 12 , 76, 76, 144],
[11, -6, 7, -3, 12, -6 , 19, 19, 36],
[11, -2, 16, -7, 18, -6 , 95, 95, 180],
[11, 13, 16, 23, 18, 24 , 95, 95, 180],
[11, 17, 7, 10, 12, 18 , 19, 19, 36],
[12, -16, 24, -20, 24, -24 , -304, -304, -576],
[12, -10, 6, -8, 12, -12 , -76, -76, -144],
[12, 3, 15, -3, 18, 0 , 171, 171, 324],
[12, 9, 15, 18, 18, 18 , 171, 171, 324],
[12, 22, 6, 14, 12, 24 , -76, -76, -144],
[13, -14, 5, -13, 12, -18 , -209, -209, -396],
[13, -11, 23, -16, 24, -18 , -95, -95, -180],
[13, 5, 14, 13, 18, 12 , 209, 209, 396],
[13, 8, 14, 1, 18, 6 , 209, 209, 396],
[14, -18, 4, -18, 12, -24 , -380, -380, -720],
[14, -6, 22, -12, 24, -12 , 76, 76, 144],
[14, 1, 13, 8, 18, 6 , 209, 209, 396],
[14, 13, 13, 5, 18, 12 , 209, 209, 396],
[15, -3, 12, 3, 18, 0 , 171, 171, 324],
[15, -1, 21, -8, 24, -6 , 209, 209, 396],
[15, 18, 12, 9, 18, 18 , 171, 171, 324],
[16, -7, 11, -2, 18, -6 , 95, 95, 180],
[16, 4, 20, -4, 24, 0 , 304, 304, 576],
[16, 12, 20, 24, 24, 24 , 304, 304, 576],
[16, 23, 11, 13, 18, 24 , 95, 95, 180],
[17, -11, 10, -7, 18, -12 , -19, -19, -36],
[17, 8, 19, 19, 24, 18 , 361, 361, 684],
[17, 9, 19, 0, 24, 6 , 361, 361, 684],
[18, -15, 9, -12, 18, -18 , -171, -171, -324],
[18, 4, 18, 14, 24, 12 , 380, 380, 720],
[18, 14, 18, 4, 24, 12 , 380, 380, 720],
[19, -19, 8, -17, 18, -24 , -361, -361, -684],
[19, 0, 17, 9, 24, 6 , 361, 361, 684],
[19, 19, 17, 8, 24, 18 , 361, 361, 684],
[20, -4, 16, 4, 24, 0 , 304, 304, 576],
[20, 24, 16, 12, 24, 24 , 304, 304, 576],
[21, -8, 15, -1, 24, -6 , 209, 209, 396],
[22, -12, 14, -6, 24, -12 , 76, 76, 144],
[23, -16, 13, -11, 24, -18 , -95, -95, -180],
[24, -20, 12, -16, 24, -24 , -304, -304, -576],
[25, -27, 47, -36, 48, -42, -779, -779, -1476],
[25, -8, 38, -19, 42, -18, 361, 361, 684],
[25, 11, 29, -2, 36, 6, 779, 779, 1476],
[25, 14, 29, 31, 36, 30, 779, 779, 1476],
[26, -22, 46, -32, 48, -36, -380, -380, -720],
[26, -3, 37, -15, 42, -12, 589, 589, 1116],
[26, 10, 28, 26, 36, 24, 836, 836, 1584],
[26, 16, 28, 2, 36, 12, 836, 836, 1584],
[27, -17, 45, -28, 48, -30, -19, -19, -36],
[27, 2, 36, -11, 42, -6, 779, 779, 1476],
[27, 6, 27, 21, 36, 18, 855, 855, 1620],
[27, 21, 27, 6, 36, 18, 855, 855, 1620],
[27, 25, 36, 47, 42, 48, 779, 779, 1476],
[28, -12, 44, -24, 48, -24, 304, 304, 576],
[28, 2, 26, 16, 36, 12, 836, 836, 1584],
[28, 7, 35, -7, 42, 0, 931, 931, 1764],
[28, 21, 35, 42, 42, 42, 931, 931, 1764],
[28, 26, 26, 10, 36, 24, 836, 836, 1584],
[29, -7, 43, -20, 48, -18, 589, 589, 1116],
[29, 12, 34, -3, 42, 6, 1045, 1045, 1980],
[29, 17, 34, 37, 42, 36, 1045, 1045, 1980],
[30, -2, 42, -16, 48, -12, 836, 836, 1584],
[30, 13, 33, 32, 42, 30, 1121, 1121, 2124],
[30, 17, 33, 1, 42, 12, 1121, 1121, 2124],
[31, 3, 41, -12, 48, -6, 1045, 1045, 1980],
[31, 9, 32, 27, 42, 24, 1159, 1159, 2196],
[31, 22, 32, 5, 42, 18, 1159, 1159, 2196],
[32, 5, 31, 22, 42, 18, 1159, 1159, 2196],
[32, 8, 40, -8, 48, 0, 1216, 1216, 2304],
[32, 24, 40, 48, 48, 48, 1216, 1216, 2304],
[32, 27, 31, 9, 42, 24, 1159, 1159, 2196],
[33, 1, 30, 17, 42, 12, 1121, 1121, 2124],
[33, 13, 39, -4, 48, 6, 1349, 1349, 2556],
[33, 20, 39, 43, 48, 42, 1349, 1349, 2556],
[33, 32, 30, 13, 42, 30, 1121, 1121, 2124],
[34, -3, 29, 12, 42, 6, 1045, 1045, 1980],
[34, 16, 38, 38, 48, 36, 1444, 1444, 2736],
[34, 18, 38, 0, 48, 12, 1444, 1444, 2736],
[34, 37, 29, 17, 42, 36, 1045, 1045, 1980],
[34, 16, 38, 38, 48, 36, 1444, 1444, 2736],
[34, 18, 38, 0, 48, 12, 1444, 1444, 2736],
[35, 12, 37, 33, 48, 30, 1501, 1501, 2844],
[35, 23, 37, 4, 48, 18, 1501, 1501, 2844],
[36, 8, 36, 28, 48, 24, 1520, 1520, 2880],
[36, 28, 36, 8, 48, 24, 1520, 1520, 2880],
[37, 4, 35, 23, 48, 18, 1501, 1501, 2844],
[37, 33, 35, 12, 48, 30, 1501, 1501, 2844],
[38, 0, 34, 18, 48, 12, 1444, 1444, 2736],
[38, 38, 34, 16, 48, 36, 1444, 1444, 2736],
[38, -38, 70, -52, 72, -60, -1444, -1444, -2736],
[38, -19, 61, -35, 66, -36, 361, 361, 684],
]

new_list = []

# Step 2: For each entry in the list, calculate (x/z, y/z)

for i in solutions_list:
    x_z = (i[0]+ i[1]*T)/(i[4]+ i[5]*T)
    y_z = (i[2]+ i[3]*T)/(i[4]+ i[5]*T)
    
    for j in solutions_list:

        # Step 3: If (x/z, y/z) AND (y/z, x/z) are not in the second list then add (x/z, y/z) to second list. 

        if (j != [x_z,y_z]) and (j != [y_z,x_z]):
            print(y_z, x_z)
            new_list.append([x_z, y_z])

#print(new_list)



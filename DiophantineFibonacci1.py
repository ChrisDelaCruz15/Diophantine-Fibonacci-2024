#Every tuple (a, b) is a*tau + b
import threading as th

def element_to_string(element):
    a = str(element[0])
    b = str(element[1])
    
    return "(" + a + "t + " + b + ")"

def cube_calc(element): #Returns a ring element's cube
    a = element[0]
    b = element[1]
    tau_component = 2*(a**3) + 3*(a**2)*b + 3*a*(b**2)
    int_component = a**3 + 3*(a**2)*b + b**3
    return (tau_component, int_component)

def square_calc(element):
    a = element[0]
    b = element[1]
    tau_component = (a**2) + (2*a*b)
    int_component = a*a+b*b
    return(tau_component, int_component)

def multiply_tuples(element1, element2):
    a = element1[0]
    b = element1[1]
    c = element2[0]
    d = element2[1]
    
    tau_component = a*c + b*c + a*d
    int_component = a*c + d*b
    return(tau_component, int_component)

def power_calc(element, power):
    output = element
    for i in range((power-1)):
        output = multiply_tuples(output, element)
    return output

def sum_tuples(a, b):
    return (a[0] + b[0], a[1] + b[1])

def fermat_test(a, b, c, power):
    if a == c or b == c:
        return False
    elif c == (0, 0):
        return False
    sum_of_elements = sum_tuples(power_calc(a, power), power_calc(b, power))
    third_element = power_calc(c, power)
    if sum_of_elements == third_element:
        #print("Found a solution!")
        #print(element_to_string(a) + "^3 " + element_to_string(b) + "^3 = " + element_to_string(c) + "^3")
        #print("Both sides equal " + element_to_string(third_cube))
        return True
    else:
        return False

def increment_test_values(test_value, max_value, min_value):
    out = test_value
    for i in range(len(test_value)):
        if out[i] < max_value:
            out[i]  = out[i] + 1
            return out
        else:
            out[i] = min_value
    return out

def search_area(max_value, min_value, last_value, power):
    test_value = [min_value, min_value, min_value, min_value, min_value]
    solutions = []
    for i in range(((max_value + 1) - min_value) ** 5):
        if fermat_test((test_value[0], test_value[1]), (test_value[2], test_value[3]), (test_value[4], last_value), power):
            print(test_value + [last_value])
        test_value = increment_test_values(test_value, max_value, min_value)

for i in range(15):
    t = th.Thread(target=search_area, args=(15, 0, i, 6,))
    t.start()
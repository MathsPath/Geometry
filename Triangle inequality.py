a = float(input("Input length of A side: "))
b = float(input("Input length of B side: "))
c = float(input("Input length of C side: "))

def triangle_inequality(a_value, b_value, c_value):
    if a_value < b_value + c_value and b_value < a_value + c_value and c_value < a_value + b_value:
        return True
    else:
        return False

print(triangle_inequality(a_value=a, b_value=b, c_value=c))
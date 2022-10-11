a = int(input("a = "))
b = int(input("b = "))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print('НОД('+str(a)+';'+str(b)+') = ', gcd(a,b))
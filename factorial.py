#head recursion
def gen_factorial(n):
    if n == 1:
        return n
    else:
        return n * gen_factorial(n-1)
    
#tail recursion
def gen_factorial(n, value=1):
    if n == 1:
        return value
    else:
        return gen_factorial((n-1), (value * n))

def generate_factorialloop(n):
    value = 1
    while n > 1:
        value *= n
        n -= 1
    return value

def main():
    print(gen_factorial(10))
    print(generate_factorialloop(10))

main()
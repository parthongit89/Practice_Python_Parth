
n = int(input("Entger the number : "))
def factorial(n) :
    if (n==1 or n==0) :
        return 1
    return n * factorial(n-1)
print(f"the factorial of is  ", factorial(n))
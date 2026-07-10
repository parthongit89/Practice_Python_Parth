def p_t(n):
    if n == 0 : return "done"
    print("*" * n)
    p_t(n-1)
n = int(input("Enter the number: "))
print(p_t(n))
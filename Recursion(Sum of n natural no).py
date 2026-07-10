aa#  sum(5) = 5+4+3+2+1
# sum (7) = 7+6+5+4+3+2+1
# sum (9) = 9+8+7+6+5+4+3+2+1
# sum(n) = n +(n-1)+(n-2)........+1

# sm_r(n) = n + sm_r(n-1)
def sm_r(n):
    if n == 1:
        return 1
    return n + sm_r(n - 1)

n = int(input("Enter the number: "))
print(sm_r(n))
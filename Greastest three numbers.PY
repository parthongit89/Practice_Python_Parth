# Write a program using fuction to find the Greastest three numbers
def Greatest():
    li= []
    for Q in range(3):
        Q = int(input("Enter number :"))
        li.append(Q)
        a = (max(li))
    return  print(a)
Greatest()

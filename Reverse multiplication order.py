#  method  1

n = int(input("Enter a number: "))
for i in range(1,11) :
	print(f"{n} x {11-i} = {n*(11-i)}")

# method  2

n = int(input("Enter the number  : "))
l = []
for i in range(1,11) :
    mul =  i * n
    l.append(mul)
l.reverse()
for li in l :	
    print(li)








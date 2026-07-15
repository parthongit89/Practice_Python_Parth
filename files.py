# method 1
f = open("file.txt") 
content = f.read()
if ("Twinkle" in content) :
    print("The word exist in file ")
else : 
    print("The word in not exist in file ")

f.close()

# method 2
with open("file.txt", "r") as file :
    content = file.read()
    if ("Twinkle" in content) :
        print("The word exist in file ")
    else : 
        print("The word in not exist in file ")

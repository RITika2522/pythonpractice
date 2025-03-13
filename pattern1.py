for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

#pattern 2
for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()

#pattern 3
for i in range(5):
    for j in range(5-i):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
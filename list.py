#ways to create list
'''lvar1 = [101, "Amit",89.90]
lvar2 = []

lvar2[0] = 101

print(lvar2)            #gives error as indexerror overriding works only if list contain some value
'''


""" 
lvar1 = [101, "Amit", "pune", "3985624755", 89.90, "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

for i in range(0,len(lvar1),2):
    print(lvar1[i], end = " ")
 """
lvar2 = []
val = int(input("Enter the number of values to add: "))
for i in range(0,val):
    lvar2.append(input("Enter the value to add: "))

for i in range(0,len(lvar2)):
    print(lvar2[i], end = " ")


#insert,sort,reverse,remove,pop,clear,copy,append,extend,count,index,alit
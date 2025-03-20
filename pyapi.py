#insert api

""" alist=["amit",101,89.9]

alist.insert(2,"Pune")
alist.append("90.2%")
alist.insert(4,"amit@xyz.com")
alist.insert(8,"Div-c")
alist.insert(-1,"2645485475")
alist.append("Student")

print(alist) """

#extend api
#any iteratable data structure can be passed as an argument to this

""" alist=["Amit", 101, 89.90]
blist=list(("MCA", "Class 1st", "Div A"))
print(alist)
print(blist)
alist.extend(blist)
print("After extend alist: ", alist) """


#remove api
#remove will remove the given word from the list or iterative data structure from its first occurence
#expected program find the words charaters digit from the list and count how many times the word or digit or character is removed

""" from os import remove


alist = ["The", "name", "of", "The", "school", "is", "The", "MITWPU"]

#using recursion
def removeword(word, alist):
    if word in alist:
        alist.remove(word)
        removeword(word,alist)
    else:
        print(alist)

#without recursion
def removeword(word, alist):
    while word in alist:
        
        remove(word)
    print(alist) """

alist = ["amit", 101, "MCA", "Pune", 45522521]
print("Before pop() ", alist)

""" # #given index value will be removed
 alist.pop(4)  """

""" alist.pop(8)
#+ve index and index out of bound while poping
# IndexError: pop index out of range """

""" alist.pop(-1)
#negative indexing pop """

print("After pop() ", alist)
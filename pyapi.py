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



""" alist = ["amit", 101, "MCA", "Pune", 45522521]
print("Before pop() ", alist)

 # #given index value will be removed
#  alist.pop(4)  

# alist.pop(8)
#+ve index and index out of bound while poping
# IndexError: pop index out of range 

# alist.pop(-1)
#negative indexing pop 

print("After pop() ", alist) """


"""DELETE operation
operator not a function
deletes the list as well same as drop operation in sql


#delete with expression pointing a location
alist =["Amit", 101, "MITWPU", "PUNE", 101]

print(alist)

# del alist[4]
# del alist[-1]
#if the above order is reversed then it will give error of index out of bound

# del alist[2:]
#+ve index can be passed, negative index can be passed, slicing acan be done, shopping cart example
print(alist)"""


"""Clear API
same as truncat operation in sql clear the list but list exists

alist=["Amit", 101, "MITWPU", "PUNE", 101]
print(alist)

alist.clear()

print(alist)
"""

"""SORTING OF THE LIST
    sort is for homogeneous elements
    but reverse can be performed on heterogeneous elements


alist=[101,108,106,107,103,109,100,102]
# alist=["AMIT", "ZAID","BHUPESH","MIHIR","ARTI"]
# alist=[101,108,106,107,"AMIT", "ZAID","BHUPESH"]    #give error as it would not able to sort heterogeneous data

#if sort in reverse order 
#this can be done by setting up flags

print(alist)
alist.sort(reverse=True)        

alist.reverse()         #alist[::-1]
print(alist)
"""
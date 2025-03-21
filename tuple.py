#TUPLE elements are immutable(no changes allowed)
#TUPLE elements can be access but not overridden
#TUPLE allows duplicate elements
#TUPLE can be extended using + operator (two tuple can be added) but extend function is not supported
#TUPLE has count function therefore counter is need not to be created

tvar=(101, "ajay", 'MIT', "MCA", "Pune", 101, 89.9,101)

for var in tvar:
    print(var," ",tvar.count(var))
print(tvar[::-1])
print(tvar.count("ajay"))
# tvar2=(101,89.09,45)
# tvar=tvar+tvar2

""" 
#this will extend the tuple
tvar = tvar+tvar2
print(tvar) 
"""

temp=("Pune")           #if given without braces then also it is a string as it calls a constructor of the string when entered with braces therefore typw will be string and not tuple to make it tuple just add ',' to after it  

#temp = 100,200,300         #it is also treated as tuple
#temp = 100, 'MIT',90.8        #it will also be a tuple

# print(type(tvar))
# print(type(temp))

flag=True

print(tvar)


""" 
for val in tvar: 
    print(val, end=" ")

for i in range(0,len(tvar)):
    print(tvar[i], end=",") 
"""

# for var in tvar:
    
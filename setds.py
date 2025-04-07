#SET is a heterogeneous data structure
#unordered set of data
#can have repeated value 
#Why the string values get shuffled while printing in set and for values after 10 why the digits get shuffled

# sobj = (1,2,3,4,5,"Amit", "Ajay", "Rajesh", "Omkar" )
# sobj=(2,6,4,1,5,3)
# sobj=(4,5,1,2,3,90,30,20,8,9)
# sobj= ("amit",3,"Ajay",10,"rajesh",6,"omkar",5)
""" sobj = {"amit", 101, "ajay", 101, 89.9, "pune"}
print(type(sobj))
for val in sobj:
    print(val, end=" ") """


#add
    #will ignore the repeated value


#remove
    #will remove the value from the set
    #if the value is not present in the set then it will throw an error


""" sobj ={"amit", 101, "ajay", 101, 89.9, "pune"}  
print("Before remove set:",sobj)
sobj.remove("amit")
print("After remove set:",sobj)
sobj.discard(101)
print("After discard set:",sobj) """


set1 ={1,2,3,4}
alist=['A', 'B','C',1,2,3]

#set1.update(alist)

# strvar = "my name is XYZ"
# print(strvar.split())       #default value in split is space
# set1.update(strvar)

tupvar= ("ABCD",)
temp = tupvar[0]
set1.update(temp)
print("Set: ",set1, "Length: ", len(set1))

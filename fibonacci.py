n = 10
num1 =0
num2 =1
num3 =0

for i in range(2,n):
    print(num1)
    print(num2)
    num3 = num1+num2
    num1 = num2
    num2 = num3
    print(num3)
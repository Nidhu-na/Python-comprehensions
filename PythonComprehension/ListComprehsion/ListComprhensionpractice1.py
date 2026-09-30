nums=[10, 15, 20, 25, 30, 35, 40]

l1=[n for n in nums if n%10==0]
print("Div by 10 : ",l1)
l2=[n*n for n in l1]
print("Squares   : ",l2)

nums=[10, 15, 20, 25, 30, 35, 40]


l3=[n*n for n in nums if n%10==0]
print("Squares   : ",l3)
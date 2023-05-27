num=int(input("Enter the number:"))
divisor=[]
for x in range (1,num+1):
    if(num%x==0):
       (divisor.append(x))
print(divisor)
print("enter a number (numerator): ")
numn = int(input())
print("enter a number (deniminator): ")
numd = int(input())

if numn%numd==0:
   print("/n"  +(numn)+ "is divisible by ") +str(numd)
else:
   print("/n"  +(numn)+ "is not divisible by ") +str(numd)
   
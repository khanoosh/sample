"""
print("This is a calculator")
a=input("enter num a")
b=input("enter num b")
sum=a+b
diff=a-b
prod=a*b
div=a/b

print("the sum is " + str(sum) +'\n'+ "the difference is " + str(diff)+'\n'+ "the product is"+ str(prod)+ '\n'+"the quotient is "+ str(div))
"""

import sys
a=int(sys.argv[1])
b=int(sys.argv[2])

sum=a+b
diff=a-b
prod=a*b
div=a/b

print("the sum is " + str(sum) +'\n'+ "the difference is " + str(diff)+'\n'+ "the product is"+ str(prod)+ '\n'+"the quotient is "+ str(div))
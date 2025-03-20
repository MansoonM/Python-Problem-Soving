#-------------Using For loop-------------

num= int(input("Enter a number: "))
f=1; 
if num<0:
    print("Error You have entered number in Negative.")
elif num==0:
    print("Factorial of 0 is always 1.")
else:
    for i in range (1,num+1):
        f= f*i;
print("Factorial of given number is ",f);



#---------------Using Recursion Method----------------

def fact(a):
   if a==0:
      return 1;
   else:
      return ( (a)* fact(a-1) );

number= int(input("Enter a number: "));
result=fact(number)
print("Factorial of given number is ",result);


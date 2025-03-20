# a=0   a=1  a=1
# b=1   b=1  b=2              Fibonacci Sequence 0,1,1,2,3,5,8,13...
# c=1   c=2  c=3

a=int(input("Enter a number: "));
b=int(input("Enter a number: "));
num=int(input("Enter a number to obtain fibonacci sequence: "));

if num==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range (2,num):
      c=a+b
      a=b
      b=c
      print(c)


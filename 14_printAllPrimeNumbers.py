#given range, find prime number in an intervals  #1:22:01 WsCube Tech

lower=int(input("Enter the lower number "))
upper=int(input("Enter the upper number "))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                #print(num, " is not a prime number")
                break
        else:
            print(num," is a Prime Number")
                  
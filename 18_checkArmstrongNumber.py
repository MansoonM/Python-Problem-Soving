num=int(input("Enter a digit number: "));

sum=0
temp=num #store userInput to perform Operations

lengthOfNum=len(str(num)) #length of Number Use str for length



while temp>0:
    digit=temp%10; #last digit
    sum += digit**lengthOfNum  #operation with last digit
    temp //=10   #remove last element
    
if sum==num:
    print("This is an Armstrong Number.")
else:
     print("This is not an Armstrong Number.")

    # largest among three numbers using conditional statements

Num1=int(input("Enter a Number "));
Num2=int(input("Enter another Number "));
Num3=int(input("Enter last Number "));

if (Num1 > Num2) and (Num1 > Num3):
    print(Num1, " is largest.")
elif (Num2 > Num1) and (Num2 > Num3):
    print(Num2, " is largest.")
else:
    print(Num3, " is largest.")
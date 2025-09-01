'''Task 3: Maximum of Three Numbers (if-elif-else)
Take 3 numbers from the user.
Find and print the largest number using decision statements.'''
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number: "))
if a==b==c:
    print("all numbers are equal:",a,b,c)
elif(a>=b) and (a>=c):
    print("largest number:",a)
elif b>=c:
    print("largest number:",b)
else:
    print("largest number:",c)
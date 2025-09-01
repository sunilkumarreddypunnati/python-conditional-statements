'''Task 4: Student Grade
Take marks from the user.
Assign grade as follows:
90+ → A
75–89 → B
50–74 → C
Below 50 → Fail'''
marks=int(input("enter you mark:"))
if (marks>=90) and (marks<=100):
    print("you got A grade:",marks)
elif marks>=75 and marks<=89:
    print("you got B grade:",marks)
elif marks>=50 and marks<=74:
    print("you got C grade:",marks)
elif marks<50 and marks >=0:
    print("sorry you fail",marks)
else:
    print("invalid marks")
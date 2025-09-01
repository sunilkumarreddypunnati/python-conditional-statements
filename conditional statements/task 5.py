'''Task 5: ATM Withdrawal Check
Take account balance and withdrawal amount.
If withdrawal amount is less than or equal to balance 
→ print "Transaction Successful".
Else 
→ print "Insufficient Balance".'''
balance=int(input("please enter your balance:"))
requird=int(input("please enter required balence: "))
if requird<=balance:
    balance-=requird
    print("trasaction is successfull")
    print("balance amount:",balance)
else:
    print("insufficient balance")

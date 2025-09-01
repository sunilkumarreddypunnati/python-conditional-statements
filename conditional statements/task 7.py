'''Task 7: Discount on Shopping (if-elif-else)
Take shopping amount as input.
Apply discount:
More than 5000 → 20% discount
2000–5000 → 10% discount
Below 2000 → No discount'''
amount=int(input("enter amount spend on shopping:"))
if amount>5000:
    print("you get 20 percent discount")
    discount=amount*(20/100)
    #print("now you should pay :",amount-discount)
elif amount>=2000 and amount<=5000:
    print("you get 10 percent discount")
    discount=amount*(10/100)
    #print("now you should pay :",amount-discount)
else:
    print("no discount.please shopping more than 2000")
    discount =0
payable_amount = amount-discount
print(payable_amount)
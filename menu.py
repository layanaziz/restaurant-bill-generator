resturant={"Pasta":50, "pizza":60,"salad":40}
print(resturant)
order1=input("What is your order? ")
howmany1=int(input("How many do you want? "))
tip1=resturant[order1]*howmany1*0.10
vat1=(resturant[order1]*howmany1*0.15)
a=(resturant[order1]*howmany1)+(tip1)+(vat1)

yesNo=input("Anything else Sir?")
if yesNo=="no":
  print("The total for your order is: ",a)
else:
  order2=input("What is your order? ")
  howmany2=int(input("How many do you want? "))
  tip2=resturant[order2]*howmany2*0.10
  vat2=(resturant[order2]*howmany2*0.15)
  b=(resturant[order2]*howmany2)+(vat2)+(tip2)
  yesNo2=input("Anything else Sir?")

  if yesNo2=="no":
       print("The total for your order is: ",b+a)
  else:
    order3=input("What is your order? ")
    howmany3=int(input("How many do you want? "))
    tip3=resturant[order3]*howmany3*0.10
    vat3=(resturant[order3]*howmany3*0.15)
    c=(resturant[order3]*howmany3)+(vat3)+(tip3)
    print("The total for your order is: ",c+b+a)
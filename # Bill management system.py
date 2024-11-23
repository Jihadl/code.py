# Bill management system
menu = ["fish-690$","lacci-90$","cotpoti-60$","dairy milk-20%"]
print(menu)
menu1 = ["fish","lacci","cotpoti","dairy milk"]
price = [690,90,70,60,20]
menu2 = input("chooise your Fast: ")
quantity  =  int(input("Enter your quantity : "))
tips = int(input("Do you have any tips?: "))

if menu2 == menu1[0]:
    total = price[0]*quantity  + tips
    print("Your bill is",total)
elif menu2 == menu1[1]:
    total = price[1]*quantity  + tips
    print("Your bill is",total)
elif menu2 == menu1[2]:
    total = price[2]*quantity  + tips
    print("Your bill is",total)
elif menu2 == menu1[3]:
    total = price[3]*quantity  + tips
    print("Your bill is",total)
elif menu2 == menu1[4]:
    total = price[4]*quantity  + tips
    print("Your bill is",total) 
print("Thank you for your order")

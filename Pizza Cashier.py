print("========================================================")
print("Wellcome to MI Pizza Delivery")
print("MENU:")
print("Pizza Options:")
print("Meat Monsta | Personal :Rp.55,000 | Medium :Rp.65,000 | Large: Rp.75,000")
print("Super Supreme | Personal :Rp.60,000 | Medium :Rp 70,000 | Large: Rp.80,000")
print("Meat Lover | Personal :Rp.60,000 | Medium :Rp.70,000 | Large: Rp.80,000")
print("Tuna Melt | Personal :Rp.50,000 | Medium :Rp.60,000 | Large: Rp.70,000")
print("Crust Options:")
print("Pan Crust | Cheesy Bite Crust | Stuffed Crust")
print("Extra Cheese:Rp. 10,000")
print("==========================================================")

price=0
 
pizza_choices = input("choose your pizza: ").lower()
if pizza_choices == "meat lover" :
    print("You have chosen Meat lover Pizza")
    price += 40_000
    print("==========================================================")
    
elif pizza_choices == "meat monsta" :
    print("You have chosen Meat Monsta Pizza")
    price += 35_000

elif pizza_choices == "super supreme" :
    print("You have chosen Super Supreme Pizza")
    price += 40_000

elif pizza_choices == "tuna melt" :
    print("You have chosen Tuna Melt Pizza")
    price += 30_000
else:
    print("Thank's for coming!!!")    

crust = input("Enter crust type (pan crust/cheesy bite crust/stuffedcrust/):")
print("==========================================================")

print("Choose your Size Pizza?")
size =input("size:").lower()
if size == "personal":
    print("Your Choose the Personal size")
    price +=20_000
elif size == "medium":
    print("Your Choose the Medium Size")
    price +=30_000
elif size == "large":
    print("Your Choose the Large Size")
    price +=40_000
else:
    print("you choose the original size")    
print("==========================================================")


extra_cheese = input("Do you want extra cheese? (Yes/No):").lower()
if extra_cheese == "yes":
    print("You have to pay for the extra cheese for Rp.10.000")
    price += 10_000
else:
    print("Thanks for the order")
    exit()
print("==========================================================")

print("Thank you for choosing  MI Pizza Hut Deliveries!")
print(f"Your final bill is: Rp. {price}")





# Code By Krishna Kaushal
import math
total_amount_pizza = 0
total_amount_pasta = 0
total_garlic_breads = 0
total_soft_drinks = 0
pizza_price = 0
pasta_price = 0
total_extra_products = 0
total_pizza_num = 0
total_pasta_num = 0
total_garlic_num = 0
total_soft_num = 0
total_baklawa_num = 0
i = 0
print("\n******************** Welcome To Pizza Plaza ********************\n")
print("#################################################################\n")
print("1. 1 Large Pizza = $12")
print("2. 2 Large Pizzas = $22")
print("3. Enter Number of Large pizzas manually (one garlic bread free for every 3 pizzas)")
print("4. 1 Large Pasta = $8")
print("5. 2 Large Pasta = $15")
print("6. Enter Number of Large Pastas Manually (one 1.25 litre soft drink free for every 3 pastas)")
print("7. 3 pizzas AND 3 pastas (get a small box of baklawa in addition to garlic bread and soft drinks)")
print("8. Return to Main Menu\n")
print("#################################################################\n")
while i <= 2:
    try:
        num = int(input("Choose a Number: "))
        # pizza_num = 0
        # pizza_price = 0
        if num == 1:
            pizza_num = 1
            pizza_price = 12
            total_amount_pizza = total_amount_pizza + pizza_price
            # print(total_amount_pizza)
            # print("Total Number of Pizzas =", pizza_num)
            total_pizza_num = total_pizza_num + pizza_num
            print("Total Price is", "Rs."+str(pizza_price), "for", pizza_num, "pizza")
            # print("Total payment Ammount Recieved For pizzas Order =", total_amount_pizza)
        elif num == 2:
            pizza_num = 2
            pizza_price = 22
            total_amount_pizza = total_amount_pasta + pizza_price
            # print(total_amount_pizza)
            # print("Total Number of Pizzas =", pizza_num)
            total_pizza_num = total_pizza_num + pizza_num
            print("Total Price is", "Rs."+str(pizza_price), "for", pizza_num, "pizzas")    
            # print("Total payment Ammount Recieved For pizzas Order =", total_amount_pizza)
        elif num == 3:
            pizza_num = input("Enter Number of Pizzas You Want: ")
            pizza_price = int(pizza_num) * 10
            garlic_bread = int(pizza_num) / 3
            total_amount_pizza = int(total_amount_pizza) + int(pizza_price)
            total_garlic_breads = total_garlic_breads + garlic_bread
            # print("Total Number of Pizzas =", pizza_num)
            total_pizza_num = int(total_pizza_num) + int(pizza_num)
            total_garlic_num = total_garlic_num + garlic_bread
            print("Total Price is", "Rs."+str(pizza_price), "for", pizza_num, "pizzas")
            # print("Total payment Ammount Recieved For pizzas Order =", total_amount_pizza)
            print("Free Garlic Breads =", math.floor(garlic_bread))

        elif num == 4:
            pasta_num = 1
            pasta_price = 8
            total_amount_pasta = total_amount_pasta + pasta_price
            total_pasta_num = total_pasta_num + pasta_num
            # print("Total Number of Pastas =", pasta_num)
            print("Total Price is", "Rs."+str(pasta_price), "for", pasta_num, "pasta")
            # print("Total Amount of Payent Recieved For Pastas Order =", total_amount_pasta)
        elif num == 5:
            pasta_num = 2
            pasta_price = 15
            total_amount_pasta = total_amount_pasta + pasta_price
            total_pasta_num = total_pasta_num + pasta_num
            # print("Total Number of Pastas =", pasta_num)
            print("Total Price is", "Rs."+str(pasta_price), "for", pasta_num, "pastas")
            # print("Total Amount of Payent Recieved For Pastas Order =", total_amount_pasta)
        elif num == 6:
            pasta_num = input("Enter number of pastas you want: ")
            pasta_price = int(pasta_num) * 7
            soft_drink = int(pasta_num) / 3
            total_amount_pasta = int(total_amount_pasta) + int(pasta_price)
            total_soft_drinks = total_soft_drinks + soft_drink
            total_pasta_num = int(total_pasta_num) + int(pasta_num)
            total_soft_num = total_soft_num + soft_drink
            print("Total Number of Pastas =",pasta_num)
            print("Total Price is", "Rs."+str(pasta_price), "for", pasta_num, "pastas")
            # print("Total Amount of Payent Recieved For Pastas Order =", total_amount_pasta)
            print("Free 1.25 Litre Soft Drinks =", math.floor(soft_drink))
        elif num == 7:
            pizza_num = int(input("Enter the number of Pizzas: "))
            pasta_num = int(input("Enter the number of Pastas: "))
            if pizza_num > 2 and pasta_num > 2:
                pizza_price = pizza_num * 10
                pasta_price = pasta_num * 7
            total_price = pizza_price + pasta_price
            baklawa = pasta_num / 3
            garlic_bread = pizza_num / 3
            soft_drink = pasta_num / 3
            total_pizza_num = int(total_pizza_num) + int(pizza_num)
            total_pasta_num = int(total_pasta_num) + int(pasta_num)
            total_baklawa_num = int(total_baklawa_num) + int(baklawa)
            print("\nTotal Price is", "Rs."+str(pasta_price), "for", str(pasta_num), "pastas and Rs."+str(pizza_price), "for", str(pizza_num), "Pizzas")
            print("Free Baklawa =", math.floor(baklawa))
            print("Free Garlic Breads =", math.floor(garlic_bread))
            print("Free Soft Drinks =", math.floor(soft_drink))
        elif num == 8:
            continue
        x = input("\nDo You Wanna Continue? (y/n)")
        if x == "n":
            break
        else:
            continue
    except:
        print("Wrong Input")
    # print("Total payment Ammount Recieved For pizzas Order =", total_amount_pizza)
    # print("Total Amount of Payent Recieved For Pastas Order =", total_amount_pasta)
print("\n")

print("################################################################################")
print("total payment amounts received for pizzas order =", total_amount_pizza)
print("total payment amounts received for pastas order =", total_amount_pasta)
print("total amount of pizzas and pastas sold in that session:")
print("     Pizzas =", total_pizza_num)
print("     Pastas =", total_pasta_num)
print("     Garlic Breads =", math.floor(total_garlic_breads))
print("     Soft Drinks =", math.floor(total_soft_drinks))
print("     Baklawa =", math.floor(total_baklawa_num))
total_bill = int(total_amount_pizza) + int(total_amount_pasta)
print("\nTotal Bill = ", total_bill)
print("################################################################################")

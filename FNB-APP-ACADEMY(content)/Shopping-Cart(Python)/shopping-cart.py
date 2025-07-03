foods= []
prices = []
total = 0

while True:
    food = input("Enter food item to buy(or 'done' to finish): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter price for {food}: "))
        foods.append(food)
        prices.append(price)
       
print("Your Shopping Cart:")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price

print("\n")
print(f"Total price: R{total}")

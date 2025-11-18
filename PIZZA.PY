import random

pizzas = {
    "Margherita": {"Small": 200, "Medium": 300, "Large": 400},
    "Pepperoni": {"Small": 250, "Medium": 350, "Large": 450},
    "Veggie": {"Small": 220, "Medium": 320, "Large": 420}
}

toppings = {
    "Extra Cheese": 50,
    "Mushrooms": 40,
    "Olives": 30,
    "Paneer": 60
}

print("🍕 Welcome to Python Pizza Delivery System 🍕")

name = input("Enter your name: ")
order_list = []

while True:
    print("\nMenu:")
    for i, pizza in enumerate(pizzas.keys(), start=1):
        print(f"{i}. {pizza}")
    choice = int(input("Choose your pizza (number): "))
    pizza_name = list(pizzas.keys())[choice - 1]

    size = input("Choose size (Small/Medium/Large): ").capitalize()
    qty = int(input("Enter quantity: "))

    print("\nAvailable Toppings:")
    for i, t in enumerate(toppings.keys(), start=1):
        print(f"{i}. {t} - ₹{list(toppings.values())[i-1]}")
    topping_choice = input("Enter topping numbers separated by commas (or press Enter for none): ")

    selected_toppings = []
    topping_cost = 0
    if topping_choice:
        for i in topping_choice.split(","):
            top = list(toppings.keys())[int(i.strip()) - 1]
            selected_toppings.append(top)
            topping_cost += toppings[top]

    price = pizzas[pizza_name][size]
    total = (price + topping_cost) * qty

    order_list.append({
        "pizza": pizza_name,
        "size": size,
        "qty": qty,
        "toppings": selected_toppings,
        "total": total
    })

    more = input("Do you want to add more pizzas? (y/n): ")
    if more.lower() != 'y':
        break

print("\n----- Order Summary -----")
grand_total = 0
for o in order_list:
    print(f"{o['qty']}x {o['size']} {o['pizza']} with {', '.join(o['toppings']) if o['toppings'] else 'no extra toppings'} - ₹{o['total']}")
    grand_total += o['total']

delivery_time = random.randint(15, 45)
print(f"\nTotal Amount: ₹{grand_total}")
print(f"Estimated Delivery Time: {delivery_time} minutes")
print(f"Thank you {name}, your pizza is on the way! 🍕")

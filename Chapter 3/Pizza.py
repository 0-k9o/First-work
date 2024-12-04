pizzas = ['pepperoni', 'margherita', 'carbonara', 'Prosciutto']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
print("\nI really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('Calzone')
friend_pizzas.append('Sarda')
print("My favorite pizzas are:")
print(pizzas)

print("\nMy friend’s favorite pizzas are:")
print(friend_pizzas)
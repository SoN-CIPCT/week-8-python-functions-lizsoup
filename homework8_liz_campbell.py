# Sandwich ingredients list function
print("Method 1 with 4 parameters, but 1 parameter can collect unlimited arguments")
def sandwich_order(bread, condiment, cheese, *toppings):
    print(f"\nYour sandwich order is one sandwich with {bread} bread, {condiment}, {cheese} and the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

sandwich_order('rye', 'mustard', 'provolone', 'turkey', 'ham', 'swiss')
sandwich_order('white', 'mayonnaise', 'swiss', 'ham')
sandwich_order('whole wheat', 'mayo', "no cheese", 'bacon', 'lettuce', 'tomato')

# Version 2 with single parameter
print("\n\nMethod 2 with single parameter:")
def sandwich_order(*toppings):
    print(f"\nYour sandwich order is one sandwich with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

sandwich_order('rye', 'mustard', 'provolone', 'turkey', 'ham', 'swiss')
sandwich_order('white', 'mayonnaise', 'swiss', 'ham')
sandwich_order('whole wheat', 'mayo', "no cheese", 'bacon', 'lettuce', 'tomato')
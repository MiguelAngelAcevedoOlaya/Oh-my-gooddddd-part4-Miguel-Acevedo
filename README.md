# RETO 4

## PUNTO 1

``` mermaid

classDiagram
    class Shape {
        + vertices: list(Point)
        + edges: list(Line)
        + inner_angles: list(float)
        + is_regular: bool
        + compute_area(self)
        + compute_perimeter(self)
        + compute_inner_angles(self)
    }

    class Point {
        + x: int
        + y: int
        + compute_distance(self, Point)
    }

    class Line {
        + start_point: Point
        + end_point: Point
        + length: float
    }

    class Triangle {
    }

    class Isosceles{
    }

    class Equilateral{
    }

    class Scalene{
    }

    class TriRectangle{
    }

    class Rectangle{
    }

    class Square{
    }

    Shape *-- Line 
    Shape *-- Point
    Triangle <|-- Shape
    Isosceles <|-- Triangle
    Equilateral <|-- Triangle
    Scalene <|-- Triangle
    TriRectangle <|-- Triangle
    Rectangle <|-- Shape
    Square <|-- Rectangle
```

```
class Point:
    # Definition of the Point class
    definition: str = "Abstract geometric entity that represents a location in space."

    # Constructor method for the Point class
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    # Method to move the point to a new location
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    # Method to reset the point to the origin
    def reset(self):
        self.x = 0
        self.y = 0
    
    # Method to calcule the distance of two points
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

class Line:
    # Constructor method to initialize the Line object with start and end points
    def __init__(self, start, end):
        self.start = start  # Start point of the line
        self.end = end      # End point of the line
        self.length = start.compute_distance(end)


class Square:
    def __init__(self, regular: bool, vertices: list, edges: list, inner_angles: list):
        self.regular = regular
        self.vertices = vertices
        self.edges = edges  # Calculate the length of the points
        self.inner_angles = inner_angles
        self.point = Point() # Call class point
        self.line = Line() # Call class line
    
    def compute_area(self):
        pass
    
    def compute_perimeter(self):
        pass
    
    def compute_inner_angles(self):
        pass


```

## Punto 2

```
class Menuitem: 
    def __init__(self, name, price=0):
        # Initializes a menu item with a name and a default price.
        self.name = name
        self.price = price

    def calculate_price(self):
        # Method to calculate the price of the item.
        return self.price

class Fastfood(Menuitem):
    def __init__(self, name, fastfood):
        # Initializes a Fastfood object with a name, type of fast food, and sets the price based on the item name.
        super().__init__(name)
        self.fastfood = fastfood
        # Sets the price based on the item name.
        if name == "hamburguer":
            self.price = 15.99
        elif name == "pizza":
            self.price = 9.99
        elif name == "hotdog":
            self.price = 7.99
        elif name == "salchipapa":
            self.price = 10.99
        else:
            self.price = 0

class Desserts(Menuitem):
    def __init__(self, name, dessert):
        # Initializes a Desserts object with a name, type of dessert, and sets the price based on the item name.
        super().__init__(name)
        self.dessert = dessert
        # Sets the price based on the item name.
        if name == "cake":
            self.price = 6.99
        elif name == "icecream":
            self.price = 1.99
        elif name == "sundae":
            self.price = 6.99
        else:
            self.price = 0

class Drinks(Menuitem):
    def __init__(self, name, drink):
        # Initializes a Drinks object with a name, type of drink, and sets the price based on the item name.
        super().__init__(name)
        self.drink = drink
        # Sets the price based on the item name.
        if name == "soda":
            self.price = 4.99
        elif name == "juice":
            self.price = 3.99
        elif name == "smoothie":
            self.price = 8.99
        elif name == "water":
            self.price = 1.99
        else:
            self.price = 0

class Proteins(Menuitem):
    def __init__(self, name, protein):
        # Initializes a Proteins object with a name, type of protein, and sets the price based on the item name.
        super().__init__(name)
        self.protein = protein
        # Sets the price based on the item name.
        if name == "chicken":
            self.price = 13.99
        elif name == "fish":
            self.price = 14.99
        elif name == "meat":
            self.price = 13.99
        else:
            self.price = 0

class Order:
    menu = [
        Fastfood("hamburguer", "Fastfood"),
        Fastfood("pizza", "Fastfood"),
        Fastfood("hotdog", "Fastfood"),
        Fastfood("salchipapa", "Fastfood"),
        Desserts("cake", "Dessert"),
        Desserts("icecream", "Dessert"),
        Desserts("sundae", "Dessert"),
        Drinks("soda", "Drink"),
        Drinks("juice", "Drink"),
        Drinks("smoothie", "Drink"),
        Drinks("water", "Drink"),
        Proteins("chicken", "Protein"),
        Proteins("fish", "Protein"),
        Proteins("meat", "Protein"),
    ]

    def __init__(self):
        # Initializes an order with an empty list to store ordered items.
        self.menuitems = []

    def add_item(self, menuitem):
        # Adds an item to the order.
        self.menuitems.append(menuitem)

    def take_order(self):
        # Calculates the total price of the order.
        total_price = sum(item.price for item in self.menuitems)
        return total_price

    def print_menu(self):
        # Prints the menu options.
        print("Menu:")
        for item in self.menu:
            print("OPTION:  " +str(item.name)+ " = $" +str(item.price))
        print("IF YOUR ORDER IS MORE THAT 50 DOLLARS, YOU GET AN 2% DISCOUNT IN THE TOTAL BILLn")
        print("\n")

    def print_receipt(self):
        # Prints the order receipt, including discounts if applicable.
        print("This is your order Receipt:")
        for item in self.menuitems:
            print("-" +str(item.name)+ ": $" +str(item.price))
        total_price = self.take_order()
        if total_price > 60:
          total_price = total_price * 0.98
        print("Total: " +str(total_price))

# Example usage
order = Order()

# Prints the menu before taking orders
order.print_menu()


# Prompt user to order Fast Food
fast_food = input("Do you want to order Fast Food?: ")
if fast_food.lower() == "yes":
    fast_food_quantity = int(input("How many? "))
    for _ in range(fast_food_quantity):
        order_food = input("What do you want to order: ")
        order.add_item(Fastfood(order_food.lower(), "Fastfood"))
else:
    print("Ok, I'm going to continue")

# Prompt user to order Drinks
drinks = input("Do you want to order Drinks?: ")
if drinks.lower() == "yes":
    drinks_quantity = int(input("How many? "))
    for _ in range(drinks_quantity):
        order_drink = input("What do you want to order: ")
        order.add_item(Drinks(order_drink.lower(), "Drink"))
else:
    print("Ok, I'm going to continue")

# Prompt user to order Desserts
desserts = input("Do you want to order Desserts?: ")
if desserts.lower() == "yes":
    desserts_quantity = int(input("How many? "))
    for _ in range(desserts_quantity):
        order_dessert = input("What do you want to order: ")
        order.add_item(Desserts(order_dessert.lower(), "Dessert"))
else:
    print("Ok, I'm going to continue")
  
# Prompt user to order Proteins
proteins = input("Do you want to order Proteins?: ")
if proteins.lower() == "yes":
    proteins_quantity = int(input("How many? "))
    for _ in range(proteins_quantity):
        order_protein = input("What do you want to order: ")
        order.add_item(Proteins(order_protein.lower(), "Protein"))
else:
    print("Ok, I'm going to continue")
    print("\n")

# Print the receipt after taking all orders
order.print_receipt()
```

# RETO 4

## PUNTO 1


This Python code defines several classes representing geometric shapes and entities.

The Point class represents a point in 2D space and includes methods for moving the point and calculating the distance between two points.

The Line class represents a line segment connecting two points and calculates its length.

The Shape class serves as a superclass for geometric shapes. It includes methods for computing the area, perimeter, and inner angles of a shape. This class is not intended to be instantiated directly but serves as a base for subclasses.

The Triangle, Rectangle, Square, Isoceles, Equilateral, Scalene, and Trirectangle classes represent specific types of shapes and inherit from the Shape class. Each subclass implements methods specific to its type, such as checking if the shape meets certain criteria (e.g., being an equilateral triangle or a square) and computing its area, perimeter, and inner angles accordingly.

Overall, these classes provide a modular and extensible way to work with geometric shapes in Python, allowing for easy addition of new shapes and functionality.

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

``` python
import math

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
        distance = (((self.x - point.x)**2) + ((self.y - point.y)**2))**(0.5)
        return distance

class Line:
    # Constructor method to initialize the Line object with start and end points
    def __init__(self, start, end):
        self.start = start  # Start point of the line
        self.end = end      # End point of the line
        self.length = start.compute_distance(end)
        

class Shape: # Super class
    def __init__(self, regular: bool, vertices: list, edges: list, inner_angles: list):
        self.regular = regular # The form is regular?
        self.vertices = vertices # Vertices of the form
        self.edges = edges  # Calculate the length of the points
        self.inner_angles = inner_angles # Angles
    
    def compute_area(self): # Funtion to calcule the area
        pass
    
    def compute_perimeter(self): # Funtion to calculate the perimeter
        pass
    
    def compute_inner_angles(self): # Funtion to calculate angles
        pass

class Triangle(Shape): # Class
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)
        self.compute_perimeter() # Call perimeter 
    
    def compute_perimeter(self):
        if len(self.edges) == 3: # Len of vertices need to be three
            perimeter = self.edges[0] + self.edges[1] + self.edges[2]
            self.perimeter = perimeter
            return perimeter # Return the perimeter
        pass

    def compute_area(self):
        if len(self.edges) == 3:
            s_heron = self.perimeter / 2 # I use the heron formula to calculate the area because it´s funtion for all triangles
            area = (s_heron*(s_heron-self.edges[0])*(s_heron-self.edges[1])*(s_heron-self.edges[2]))**0.5
            return area
        else:
            pass
    
    def compute_inner_angles(self):
        if len(self.edges) == 3: # We use arcoseno to calculate the angles of the traingle, this funtion in all triangles
            angle_a = math.degrees(math.acos((self.edges[1]**2 + self.edges[2]**2 - self.edges[0]**2) / (2 * self.edges[1] * self.edges[2])))
            angle_b = math.degrees(math.acos((self.edges[2]**2 + self.edges[0]**2 - self.edges[1]**2) / (2 * self.edges[0] * self.edges[2])))
            angle_c = math.degrees(math.acos((self.edges[0]**2 + self.edges[1]**2 - self.edges[2]**2) / (2 * self.edges[0] * self.edges[1])))
            self.inner_angles = [angle_a, angle_b, angle_c]
            return self.inner_angles
        else: pass

class Rectangle(Shape): # Class 
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)
        self.is_rectangle()
    
    def is_rectangle(self): # Try to see if the points that the user enter make a rectangle
        if len(self.edges) == 4:
            sorted_vertices = sorted(self.vertices, key=lambda point: point.x) # Order the points
            if sorted_vertices[0].x == sorted_vertices[1].x:
                if sorted_vertices[2].x == sorted_vertices[3].x:
                    if sorted_vertices[0].y == sorted_vertices[2].y:
                        if sorted_vertices[1].y == sorted_vertices[3].y: # If they are a rectangle
                            width = self.vertices[2].x - self.vertices[0].x # Calculate the width
                            height = self.vertices[1].y - self.vertices[0].y # Calculate the height
                            self.width = width
                            self.height = height
                            return True
                        else: 
                            return False # In all other cases the form is not a rectangle, and base of that we don´t need to do the other
                    else: 
                        return False
                else:
                    return False
            else: 
                return False
        else:
            return False
            
    def compute_perimeter(self):
        if len(self.edges) == 4:
            perimeter = (2*self.width + 2*self.height) # Calculate perimeter in base of with and height
            return perimeter
        else:
            pass

    def compute_area(self):
        if len(self.edges) == 4:
            area = self.height * self.width # Caclulate the area of a form with 4 lines
            return area
        else:
            pass
    
    def compute_inner_angles(self):
        if len(self.edges) == 4:
            self.inner_angles = [90, 90, 90, 90] # If is a rectangle, you don´t need to calculate angles, there are 90 
            return self.inner_angles
        else: pass

class Square(Rectangle): # Class Herence
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)
    
    def is_square(self):
        super().is_rectangle() # Prove if is a rectangle but why?
        if self.height == self.width: # To call this things and see if they are equal, in case that not, it´s not a square
            return True # Is square
        else:
            return False # Is´nt an square
        
    def compute_perimeter(self):
        return super().compute_perimeter() # Call perimeter from rectangle

    
    def compute_area(self):
        return super().compute_area() # Call area from rectangle
    
    def compute_inner_angles(self):
        return super().compute_inner_angles() # Call inner angles from rectangle
        
class Isoceles(Triangle): # Class Herence
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)
        
    def is_isoceles(self): # Define if is a isoceles, 2 lines need to be equal
        if self.edges[0] == self.edges[1] or self.edges[0] == self.edges[2] or self.edges[1] == self.edges[2]:
            return True
        else: return False
    
    def compute_perimeter(self):
        return super().compute_perimeter() # Call perimeter in traingle
    
    def compute_area(self):
            return super().compute_area() # Call area in trinagle
    
    def compute_inner_angles(self): # Call inner angles in triangle
        return super().compute_inner_angles()

class Equilateral(Triangle): # Class herence
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)
        
    def is_equilateral(self): # We need to see if is a equilateral, it is if all the lines are equal
        if self.edges[0] == self.edges[1] and self.edges[1] == self.edges[2]:
            return True
        else: return False
    
    def compute_perimeter(self):
        return super().compute_perimeter() # Call perimeter from triangle

    
    def compute_area(self):
        return super().compute_area() # Call area from triangle
    
    def compute_inner_angles(self):
        return super().compute_inner_angles() # Call inner angles from triangle

class Scalene(Triangle): # Class herence
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)
        
    def is_scalene(self): # We need to si if is scalen, the three lines are diferente
        if self.edges[0] != self.edges[1] and self.edges[0] != self.edges[2] and self.edges[1] != self.edges[2]:
            return True
        else: return False
    
    def compute_perimeter(self): # Call perimeter from triangle
        return super().compute_perimeter()
    
    def compute_area(self):
        return super().compute_area() # Call area from tringle

    
    def compute_inner_angles(self):
        return super().compute_inner_angles() # Call inner angles from triangle

class Trirectangle(Triangle): #Class herence
    def __init__(self, regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(regular, vertices, edges, inner_angles)

    def is_trirectangle(self): # We need to si if a rectnagle triangle, we considere a few calculate mistake that happens in python
        super().compute_inner_angles()
        for i in self.inner_angles:
            if abs(i - 90) < 0.1:
                return True
        else: return False
            
    def compute_perimeter(self):
        return super().compute_perimeter() # call perimeter from triangle
    
    def compute_area(self): # call area from triangle
        return super().compute_area()
    
    def compute_inner_angles(self): # call inner angles from triangle
        return super().compute_inner_angles()
if __name__ == "__main__":
    # Ask the user whether they want to input 3 or 4 points
    figure = int(input("You want to enter 3 or 4 points: "))
    flag = True

    # Validate the user input
    while flag == True:
        if figure == 3 or figure == 4:
            break
        else:
            figure = int(input("You want to enter 3 or 4 points: "))

    # Process based on the number of points entered by the user
    if figure == 3:
        # Obtain the coordinates of three points from the user
        p1 = Point(int(input("Enter the x coordinate of the p1: ")), int(input("Enter the y coordinate of the p1: ")))
        p2 = Point(int(input("Enter the x coordinate of the p2: ")), int(input("Enter the y coordinate of the p2: ")))
        p3 = Point(int(input("Enter the x coordinate of the p3: ")), int(input("Enter the y coordinate of the p3: ")))

        # Create lines using the provided points
        line1 = Line(p1, p2)
        line2 = Line(p2, p3)
        line3 = Line(p3, p1)

        # Create instances of different types of triangles
        triangulo = Isoceles(True, [p1, p2, p3], [line1.length, line2.length, line3.length], [0, 0, 0])
        triangulo_1 = Equilateral(True, [p1, p2, p3], [line1.length, line2.length, line3.length], [0, 0, 0])
        triangulo_2 = Scalene(True, [p1, p2, p3], [line1.length, line2.length, line3.length], [0, 0, 0])
        triangulo_3 = Trirectangle(True, [p1, p2, p3], [line1.length, line2.length, line3.length], [0, 0, 0])
        print(triangulo_3.is_trirectangle())

        # Determine the type of triangle and perform calculations accordingly
        if triangulo.is_isoceles() == True:
            if triangulo_3.is_trirectangle() == True:
                print("The triangle is an isoceles and a rectangle triangle")
                per_trin = triangulo.compute_perimeter()
                print("The perimeter of the triangle is: " + str(per_trin))
                area_trin = triangulo.compute_area()
                print("The area of the triangle is: " + str(area_trin))
                angles_trin = triangulo.compute_inner_angles()
                print("The inner angles of the triangle is: " + str(angles_trin))
            else:
                print("The triangle is an isoceles")
                per_trin = triangulo.compute_perimeter()
                print("The perimeter of the triangle is: " + str(per_trin))
                area_trin = triangulo.compute_area()
                print("The area of the triangle is: " + str(area_trin))
                angles_trin = triangulo.compute_inner_angles()
                print("The inner angles of the triangle is: " + str(angles_trin))

        elif triangulo_1.is_equilateral() == True:
            print("The triangle is an Equilateral")
            per_trin = triangulo_1.compute_perimeter()
            print("The perimeter of the triangle is: " + str(per_trin))
            area_trin = triangulo_1.compute_area()
            print("The area of the triangle is: " + str(area_trin))
            angles_trin = triangulo_1.compute_inner_angles()
            print("The inner angles of the triangle is: " + str(angles_trin))

        elif triangulo_2.is_scalene() == True:
            if triangulo_3.is_trirectangle() == True:
                print("The triangle is an Scalene and a rectangle triangle")
                per_trin = triangulo_2.compute_perimeter()
                print("The perimeter of the triangle is: " + str(per_trin))
                area_trin = triangulo_2.compute_area()
                print("The area of the triangle is: " + str(area_trin))
                angles_trin = triangulo_2.compute_inner_angles()
                print("The inner angles of the triangle is: " + str(angles_trin))
            else: 
                print("The triangle is an Scalene")
                per_trin = triangulo_2.compute_perimeter()
                print("The perimeter of the triangle is: " + str(per_trin))
                area_trin = triangulo_2.compute_area()
                print("The area of the triangle is: " + str(area_trin))
                angles_trin = triangulo_2.compute_inner_angles()
                print("The inner angles of the triangle is: " + str(angles_trin))

    if figure == 4:
        # Obtain the coordinates of four points from the user
        p1 = Point(int(input("Enter the x coordinate of the p1: ")), int(input("Enter the y coordinate of the p1: ")))
        p2 = Point(int(input("Enter the x coordinate of the p2: ")), int(input("Enter the y coordinate of the p2: ")))
        p3 = Point(int(input("Enter the x coordinate of the p3: ")), int(input("Enter the y coordinate of the p3: ")))
        p4 = Point(int(input("Enter the x coordinate of the p4: ")), int(input("Enter the y coordinate of the p4: ")))

        # Sort the points based on their x-coordinate
        listi = [p1, p2, p3, p4]
        listi = sorted(listi, key=lambda p: (p.x, p.y))

        # Create lines using the provided points
        line1 = Line(listi[0], listi[1])
        line2 = Line(listi[0], listi[2])
        line3 = Line(listi[1], listi[3])
        line4 = Line(listi[2], listi[3])
        # Create instances of Rectangle and Square
        rectangulo = Rectangle(True, [listi[0], listi[1], listi[2], listi[3]], [line1.length, line2.length, line3.length, line4.length], [0, 0, 0, 0])
        cuadrado = Square(True, [listi[0], listi[1], listi[2], listi[3]], [line1.length, line2.length, line3.length, line4.length], [0, 0, 0, 0])

        # Check if the figure is a square or a rectangle
        if cuadrado.is_square() == True: # If it's a square
            print("The form is a square")
            per_cua = cuadrado.compute_perimeter() # Compute the perimeter
            print("The perimeter of the square is: " +str(per_cua))
            area_cua = cuadrado.compute_area() # Compute the area
            print("The area of the square is: " +str(area_cua))
            angles_cua = cuadrado.compute_inner_angles() # Compute the inner angles
            print("The inner angles of the square is: " +str(angles_cua))

        elif rectangulo.is_rectangle() == True: # If it's a rectangle
            print("The form is a Rectangle")
            per_rect = rectangulo.compute_perimeter() # Compute the perimeter
            print("The perimeter of the rectangle is: " +str(per_rect))
            area_rect = rectangulo.compute_area() # Compute the area
            print("The area of the rectangle is: " +str(area_rect))
            angles_rect = rectangulo.compute_inner_angles() # Compute the inner angles
            print("The inner angles of the rectangle is: " +str(angles_rect))

```

## Punto 2

This code represents a simple restaurant ordering and payment system.

First, it defines classes for menu items, including their names and prices, as well as classes for payment methods such as cash and card. Each menu item can have its price set and retrieved, and payments can be made either with cash or card.

The Order class manages the customer's order, allowing them to select items from the menu, calculate the total price, print the receipt with any applicable discounts, and handle the payment process. Discounts are applied if the total price exceeds $60 or if the payment method is cash.

In the main part of the code, an instance of the Order class is created, and the user is prompted to select items from the menu. After completing the order, the user can choose to pay with either cash or a card. If paying with cash, an 8% discount is applied, and if paying with a card, the payment process is handled.

Overall, this code provides a framework for managing restaurant orders, calculating prices, applying discounts, and processing payments, enhancing the customer experience and facilitating efficient order management.

``` python
class Menuitem: 
    def __init__(self, name, price=0):
        # Initializes a menu item with a name and a default price.
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def calculate_price(self):
        # Method to calculate the price of the item.
        return self._price

class Pay_method:
    def __init__(self, amount):
        # Constructor to initialize the amount attribute.
        self.amount = amount
    
    def pagar(self, cantidad):
        # Method placeholder for making payments.
        pass

class Card(Pay_method):
    def __init__(self,tipe, number, cvc):
        # Constructor for Card class.
        super().__init__(self.amount)  # Calling the superclass constructor
        self.tipe = tipe  # Type of card
        self.number = number  # Card number
        self.cvc = cvc  # Card verification code
    
    def pagar(self):
        # Method to process card payment.
        pago = print("Your pay" +str(self.amount)+ "with card number: " +str(self.number)+ " was made sucessfull")
        return pago

class Credit(Card):
    def __init__(self, tipe, number, cvc):
        # Constructor for Credit card class.
        super().__init__(self, tipe, number, cvc)
    
    def pagar(self):
        # Method to process credit card payment.
        return super().pagar()

class Debit(Card):
    def __init__(self, tipe, number, cvc):
        # Constructor for Debit card class.
        super().__init__(self, tipe, number, cvc)
        
    def pagar(self):
        # Method to process debit card payment.
        return super().pagar() 

class Cash(Pay_method):
    def __init__(self, cash, correct = False, vueltas = 0):
        # Constructor for Cash class.
        self.cash = cash  # Amount of cash
        self.correct = correct  # Flag indicating if payment is correct
        self.vueltas = vueltas  # Change to be returned
        
    def cambio(self):
        # Method to calculate change for cash payment.
        if self.cash < self.amount:
            print("Your money is not enough")
            self.correct = False
            return self.correct
        elif self.cash == self.amount:
            self.vueltas = 0
            return self.correct
        elif self.amount < self.cash:
            self.vueltas = self.cash -self.amount
            return self.correct
        
    def pagar(self):
        # Method to process cash payment.
        if self.vueltas == 0:
            pago = ("You pay: " +str(self.cash)+ " sucessfull")
        elif self.vueltas > 0:
            pago = ("You pay: " +str(self.cash)+ " sucessfull and this is your change: " +str(self.vueltas))
        return pago
    

class Fastfood(Menuitem):
    def __init__(self, name, fastfood):
        # Initializes a Fastfood object with a name, type of fast food, and sets the price based on the item name.
        super().__init__(name)
        self.fastfood = fastfood
        # Sets the price based on the item name.
        if name == "hamburguer":
            self.set_price(15.99)
        elif name == "pizza":
            self.set_price(9.99)
        elif name == "hotdog":
            self.set_price(7.99)
        elif name == "salchipapa":
            self.set_price(10.99)
        else:
            self.set_price(0)

class Desserts(Menuitem):
    def __init__(self, name, dessert):
        # Initializes a Desserts object with a name, type of dessert, and sets the price based on the item name.
        super().__init__(name)
        self.dessert = dessert
        # Sets the price based on the item name.
        if name == "cake":
            self.set_price(6.99)
        elif name == "icecream":
            self.set_price(1.99)
        elif name == "sundae":
            self.set_price(6.99)
        else:
            self.set_price(0)

class Drinks(Menuitem):
    def __init__(self, name, drink):
        # Initializes a Drinks object with a name, type of drink, and sets the price based on the item name.
        super().__init__(name)
        self.drink = drink
        # Sets the price based on the item name.
        if name == "soda":
            self.set_price(4.99)
        elif name == "juice":
            self.set_price(3.99)
        elif name == "smoothie":
            self.set_price(8.99)
        elif name == "water":
            self.set_price(1.99)
        else:
            self.set_price(0)

class Proteins(Menuitem):
    def __init__(self, name, protein):
        # Initializes a Proteins object with a name, type of protein, and sets the price based on the item name.
        super().__init__(name)
        self.protein = protein
        # Sets the price based on the item name.
        if name == "chicken":
            self.set_price(13.99)
        elif name == "fish":
            self.set_price(14.99)
        elif name == "meat":
            self.set_price(13.99)
        else:
            self.set_price(0)

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
        total_price = sum(item.get_price() for item in self.menuitems)
        return total_price

    def print_menu(self):
        # Prints the menu options.
        print("Menu:")
        for item in self.menu:
            print("OPTION:  " +str(item.get_name())+ " = $" +str(item.get_price()))
        print("IF YOUR ORDER IS MORE THAT 50 DOLLARS, YOU GET AN 2% DISCOUNT IN THE TOTAL BILL. \nALSO IF YOU PAY IN EFFECTIVE, YOU GET AN 8% DISCOUNT")
        print("\n")

    def print_receipt(self):
        # Prints the order receipt, including discounts if applicable.
        print("This is your order Receipt:")
        for item in self.menuitems:
            print("-" +str(item._name)+ ": $" +str(item._price))
        total_price = self.take_order()
        if total_price > 60:
          total_price = total_price * 0.98
        print("Total: " +str(total_price))
        return total_price

if __name__ == "__main__":
    # Create an instance of the Order class to manage the customer's order.
    order = Order()

    # Display the menu options for the user to see.
    order.print_menu()

    # Prompt the user to order Fast Food items.
    fast_food = input("Do you want to order Fast Food?: ")
    if fast_food.lower() == "yes":
        # Ask the user for the quantity of fast food items they want to order.
        fast_food_quantity = int(input("How many? "))
        # Iterate over the quantity specified and add each fast food item to the order.
        for _ in range(fast_food_quantity):
            order_food = input("What do you want to order: ")
            order.add_item(Fastfood(order_food.lower(), "Fastfood"))
    else:
        print("Ok, I'm going to continue")

    # Prompt the user to order Drinks.
    drinks = input("Do you want to order Drinks?: ")
    if drinks.lower() == "yes":
        # Ask the user for the quantity of drinks they want to order.
        drinks_quantity = int(input("How many? "))
        # Iterate over the quantity specified and add each drink to the order.
        for _ in range(drinks_quantity):
            order_drink = input("What do you want to order: ")
            order.add_item(Drinks(order_drink.lower(), "Drink"))
    else:
        print("Ok, I'm going to continue")

    # Prompt the user to order Desserts.
    desserts = input("Do you want to order Desserts?: ")
    if desserts.lower() == "yes":
        # Ask the user for the quantity of desserts they want to order.
        desserts_quantity = int(input("How many? "))
        # Iterate over the quantity specified and add each dessert to the order.
        for _ in range(desserts_quantity):
            order_dessert = input("What do you want to order: ")
            order.add_item(Desserts(order_dessert.lower(), "Dessert"))
    else:
        print("Ok, I'm going to continue")
    
    # Prompt the user to order Proteins.
    proteins = input("Do you want to order Proteins?: ")
    if proteins.lower() == "yes":
        # Ask the user for the quantity of proteins they want to order.
        proteins_quantity = int(input("How many? "))
        # Iterate over the quantity specified and add each protein to the order.
        for _ in range(proteins_quantity):
            order_protein = input("What do you want to order: ")
            order.add_item(Proteins(order_protein.lower(), "Protein"))
    else:
        print("Ok, I'm going to continue")
        print("\n")

    # Print the receipt summarizing the order and total price.
    total_price = order.print_receipt()
    
    # Create an instance of the Pay_method class to handle the payment process.
    method = Pay_method(amount = total_price)

    print("\n")
    # Ask the user whether they want to pay with cash or card.
    pagando = input("Do you want to pay with cash or card? ")
    bandera = True
    while bandera:
        if pagando.lower() == "cash" or pagando.lower() == "efectivo":
            print("You get a 8% discount")
            # Apply an 8% discount for cash payment.
            total_price = total_price * 0.92
            # Prompt the user to enter the cash amount and handle the payment process.
            cash = Cash(cash=int(input("Enter the money with you are going to pay")), amount= total_price)
            if not cash.cambio():
                continue
            else:
                print(cash.pagar())
                bandera = False
                break
        elif pagando.lower() == "card" or pagando.lower() == "tarjeta":
            # Prompt the user to enter card details and handle the card payment process.
            tipe = input("Enter card type (debit/credit): ")
            number = input("Enter card number: ")
            cvc = input("Enter card cvc: ")
            amount = total_price
            card = Card(tipe, amount, number, cvc)
            print(card.pagar())
            bandera = False
            break

```

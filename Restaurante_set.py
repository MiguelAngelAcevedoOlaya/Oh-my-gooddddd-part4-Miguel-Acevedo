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


# Base class for Sneaker
class Sneaker:
    def __init__(self, name, brand, price, size, color, stock_quantity, release_year):
        self.name = name
        self.brand = brand
        self.price = price
        self.size = size
        self.color = color
        self.stock_quantity = stock_quantity
        self.release_year = release_year
    
    def display_info(self):
        return f"Name: {self.name}, Brand: {self.brand}, Price: ${self.price}, Size: {self.size}, Color: {self.color}, Stock: {self.stock_quantity}, Release Year: {self.release_year}"

# RunningSneaker class, inherits from Sneaker
class RunningSneaker(Sneaker):
    def __init__(self, name, brand, price, size, color, stock_quantity, release_year, cushioning, weight):
        super().__init__(name, brand, price, size, color, stock_quantity, release_year)
        self.cushioning = cushioning
        self.weight = weight
    
    def display_info(self):
        info = super().display_info()
        return f"{info}, Cushioning: {self.cushioning}, Weight: {self.weight}g"

# LifestyleSneaker class, inherits from Sneaker
class LifestyleSneaker(Sneaker):
    def __init__(self, name, brand, price, size, color, stock_quantity, release_year, design_type, material):
        super().__init__(name, brand, price, size, color, stock_quantity, release_year)
        self.design_type = design_type
        self.material = material
    
    def display_info(self):
        info = super().display_info()
        return f"{info}, Design Type: {self.design_type}, Material: {self.material}"

# Store class that manages the inventory
class Store:
    def __init__(self):
        self.inventory = {
            'Running': [],
            'Lifestyle': []
        }
    
    def add_sneaker(self, sneaker, category):
        if category in self.inventory:
            self.inventory[category].append(sneaker)
    
    def display_inventory(self, category):
        if category in self.inventory:
            print(f"--- {category} Sneakers ---")
            for sneaker in self.inventory[category]:
                print(sneaker.display_info())
        else:
            print("Category not found!")
    
    def search_by_size(self, size):
        found = False
        for category, sneakers in self.inventory.items():
            for sneaker in sneakers:
                if sneaker.size == size:
                    print(sneaker.display_info())
                    found = True
        if not found:
            print(f"No sneakers found in size {size}.")

# Create store object
store = Store()

# Function to add sneakers to the store
def add_sneaker_to_store():
    category = input("Enter the sneaker category (Running/Lifestyle): ").strip().capitalize()
    name = input("Enter the name of the sneaker: ").strip()
    brand = input("Enter the brand of the sneaker: ").strip()
    price = float(input("Enter the price of the sneaker: "))
    size = int(input("Enter the size of the sneaker: "))
    color = input("Enter the color of the sneaker: ").strip()
    stock_quantity = int(input("Enter the stock quantity of the sneaker: "))
    release_year = int(input("Enter the release year of the sneaker: "))
    
    if category == "Running":
        cushioning = input("Enter the cushioning type: ").strip()
        weight = int(input("Enter the weight of the sneaker (in grams): "))
        sneaker = RunningSneaker(name, brand, price, size, color, stock_quantity, release_year, cushioning, weight)
        store.add_sneaker(sneaker, "Running")
    elif category == "Lifestyle":
        design_type = input("Enter the design type: ").strip()
        material = input("Enter the material of the sneaker: ").strip()
        sneaker = LifestyleSneaker(name, brand, price, size, color, stock_quantity, release_year, design_type, material)
        store.add_sneaker(sneaker, "Lifestyle")
    else:
        print("Invalid category. Sneaker not added.")

# Function to display the menu
def display_menu():
    while True:
        print("\n--- Sneaker Retail Store ---")
        print("1. Add Sneaker")
        print("2. Display Running Sneakers")
        print("3. Display Lifestyle Sneakers")
        print("4. Search for Sneakers by Size")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_sneaker_to_store()
        elif choice == "2":
            store.display_inventory("Running")
        elif choice == "3":
            store.display_inventory("Lifestyle")
        elif choice == "4":
            size = int(input("Enter the size to search: "))
            store.search_by_size(size)
        elif choice == "5":
            print("Exiting the store. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

# Add 5 more sneakers to the store
store.add_sneaker(RunningSneaker("Nike Air Max", "Nike", 150, 11, "Red", 50, 2022, "Medium", 280), "Running")
store.add_sneaker(RunningSneaker("Adidas Supernova", "Adidas", 130, 10, "Black", 30, 2023, "Soft", 270), "Running")
store.add_sneaker(LifestyleSneaker("Puma Suede", "Puma", 90, 8, "Blue", 100, 2021, "Casual", "Suede"), "Lifestyle")
store.add_sneaker(LifestyleSneaker("Reebok Classic", "Reebok", 80, 9, "White", 80, 2020, "Retro", "Leather"), "Lifestyle")
store.add_sneaker(RunningSneaker("Under Armour HOVR", "Under Armour", 170, 12, "Gray", 25, 2023, "High", 310), "Running")

# Run the store menu
display_menu()

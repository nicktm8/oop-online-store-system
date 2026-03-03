# Importovanje klasa

import product as pr
import employee as em
import user as us
import random

# Lista proizvoda (name, price, quantity, description)

products = [
    pr.Product("Macbook Air M3", 145000, 9, "Tanak i lagan laptop sa moćnim M3 čipom."),
    pr.Product("Samsung Galaxy S25 Ultra", 150000, 10, "Flegšip model sa integrisanom S Pen olovkom i AI funkcijama."),
    pr.Product("Samsung Galaxy Tab S11", 100000, 20, "Premium Android tablet sa balansom između cene i performansi."),
    pr.Product("Dell Gaming Monitor (27 inča)", 25000, 30, "Monitor visokih performansi sa IPS panelom i brzim osvežavanjem (165Hz+)."),
    pr.Product("Logitech MX Master 3S", 8000, 40, "Profesionalni bežični miš poznat po ergonomiji i tišim klikovima.")
    
]

# Lista zaposlenih (name, email, salary, address)

employees = [
    em.Employee("Adam Adamic", "adamAgmail.com", 100000, "Topolska 18, 21000 Novi Sad"),
    em.Employee("Bojana Bojanic", "bocka123@gmail.com", 120000, "Kralja Nikole 99, 11000 Beograd")
]

# Lista korisnika (name, username, email, phone, address)

users = [
    us.User("Jeremy Hammond", "jer1hmd@gmail.com", 12345678, "742 Evergreen Terrace, Springfield, OR 97403"),
    us.User("Richard May", "maymay@gmail.com", 324321543, "1060 W Addison St, Chicago, IL 60613"),
    us.User("James Clarkson", "clarksonJ@mgmail.com", 1697542843, "221B Baker St, London NW1 6XE, UK")
]

# Demonstracija enkapsulacije


# Ispis liste products, implementiranje check_quantity metode i demonstracija enkapsulacije (get_price, set_price)

print("\nList of products:")

for product in products:
    old_price = product.get_price()
    new_price = old_price * 1.10   # Uvecanje cene (Old Price) za 10%

    product.set_price(new_price)

    print(f"\nName: {product.name}")
    print(f"Old Price: {old_price:,.2f} RSD")
    print(f"New Price: {new_price:,.2f} RSD")
    print(f"Quantity: {product.quantity}")
    print(f"Description: {product.get_description()}")
    print(f"Adequate inventory (10+ items): {product.check_quantity()}")

print("-" * 50)

# Ispis liste employees i users, polimorfizam

print("\n--- Display of employees and users ---\n")

persons = employees + users   # lista tipa Person

for person in persons:
    
    print(person.display_info())

# Dodavanje proizvoda korisnicima u shopping_history i implementiranje metoda add_product i total_spend
print("\n--------Shopping history--------\n")

for user in users:
    print(f"User: {user.name}")
    
    num_products = random.randint(1, 3)

    for _ in range(num_products):
        user.add_product(random.choice(products))
               
    for product in user.shopping_history:
        print(f"{product.name} - {product.get_price():,.2f} RSD")

    # Ukupna Potrošnja
    
    print(f"Total spent: {user.total_spent():,.2f} RSD\n")

print("-" * 50)

# Implementiranje increase_salary metode i enkapsulacija (get_salary, set_salary)

for employee in employees:
    old_salary = employee.get_salary()

    employee.increase_salary(10)

    new_salary = employee.get_salary()

    print(employee.name)
    print(f"Old salary: {old_salary:,.2f} RSD")
    print(f"Increased salary (+10%): {new_salary:,.2f} RSD\n")


print("-" * 50)


from models.person import Person

class User(Person):
    
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, address)
        self.phone = phone
        self.shopping_history = []
        
    # Setter i getter za phone    
        
    def set_phone(self, phone):
        if phone == "":
            raise ValueError("Phone cannot be empty")
        if type(phone) != int:
            raise TypeError("Phone must be a number")
        
        self.phone = phone
             
    def get_phone(self):
        return self.phone
        
    def total_spent(self):
        total = 0 
        
        for p in self.shopping_history:
            total += p.get_price()
            
        return total
    
    def add_product(self, product):
        self.shopping_history.append(product)
        
    # Polimorfizam 
        
    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Email: {self.get_email()}\n"
            f"Address: {self.get_address()}\n"
            f"Phone: {self.get_phone()}\n"
        )    

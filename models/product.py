
class Product:
    
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self._description = description
        
    # Setter i getter za price    
        
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        self.__price = price
        
    def get_price(self):
        return self.__price
    
    # Setter i getter za description
    
    def set_description(self, description):
        if type(description) != str:
            raise TypeError("Description must be a string")
        if description == "":
            raise ValueError("Description cannot be empty")
        
        self._description = description
         
    def get_description(self):
        return self._description
    
    # Check_quantity funkcija
        
    def check_quantity(self):
        return self.quantity >= 10

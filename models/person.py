from abc import ABC, abstractmethod 

class Person(ABC):
    
    def __init__(self, name, email, address):
        self.name = name
        self._email = email
        self._address = address
    
    # Setter i getter za email
    
    def set_email(self, email):
            self._email = email
     
    def get_email(self):
        return self._email
    
    # Setter i getter za address
    
    def set_address(self, address):
        if type(address) != str:
            raise TypeError("Address must be a string")
        if address == "":
            raise ValueError("Address cannot be empty")

        self._address = address
        
    def get_address(self):
        return self._address

    # Validacija email-a
    
    def check_email(self):
        if '@' not in self._email:
            return False
        
        user, domain = self._email.split("@")
        
        if len(user) == 0 or len(domain) == 0:
            return False
        if "." not in domain:
            return False
        
        return True
    
    @abstractmethod
    def display_info(self): 
       pass

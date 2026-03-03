from person import Person

class Employee(Person):
    
    def __init__(self, name, email, salary, address):
        super().__init__(name, email, address)
        self.__salary = salary
        
    # Setter i getter za salary    
        
    def set_salary(self, salary):
       
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    # increase_salary funkcija
    
    def increase_salary(self, percentage):
        self.__salary *= 1 + percentage / 100
    
    # Polimorfizam
           
    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Email: {self.get_email()}\n"
            f"Valid email: {self.check_email()}\n"
            f"Address: {self.get_address()}\n"
            f"Salary: {self.get_salary():,.2f} RSD\n"
        )    

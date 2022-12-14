class Employee:

    raise_amount = 1.05

    def __init__(self, first_name, last_name, job_title, salary, email):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary
        self.email = email 

    def raise_amount (self, salary):
        self.salary += self.raise_amount 
        print(f"Congratulations {self.first_name} {self.last_name}, you have received a raise, and now your salary is {self.salary}")

class Sales(Employee):
    def __init__ (self, phone_number):
        super().__init__(first_name, last_name, job_title, salary, email)
        self.phone_number = phone_number
        # create a phone number attribute on instatiation using the super method

    def send_email (self, email, message):
        self.email = email
        self.message = message
        print(f"Dear {self}, thank you for your interest in the product. My email is ..... and my phone number is ....")

class Development(Employee):
    def code(self, code):
        print (f"Dear Mike O'Neil, thank you for your request. My email is {self.email} and my phone number is {self.phone}.")

   

# salesperson = Sales('Blake', 'Waters', 'sales_rep', 500000, "bwaters@email.com", 555_555_5555)

salesperson = Sales ("mike O'Neil") ("mikeyoh@email.com") ("Dear Mike O'Neil, thank you... My email is lsadkjfl;as and my phone number is....")
salesperson = Sales raise_amount (50000)
dev1 = Employee ('Cecelia', 'Cathwright', 'Back End Dev', 1000000, "ceca@email.com")
dev1 = Development (100000)
# dev.code() # "Cecelia Cathwright is writing code"

print(dev1)



        
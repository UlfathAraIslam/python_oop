class Employee:
    def __init__(self,name,hourly_wage):
        self.name = name
        self.hourly_wage = hourly_wage
yuki = Employee("Yuki",1200)
kenta = Employee("Kenta",1500)
print(f"Yuki: {yuki.name} {yuki.hourly_wage}, Kenta: {kenta.name},{kenta.hourly_wage}")
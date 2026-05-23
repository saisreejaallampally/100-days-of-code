#code 1
student={}
for i in range(2):
    name=input("Enter name:")
    age=input("Enter age:")
    marks=input("Enter marks:")
    city=input("Enter city:")
    student["name"]=name
    student["age"]=age
    student["marks"]=marks
    student["city"]=city
print(student)
 
#code 2
products={}
for i in range(3):
    product_name=input("Enter the product name:")
    quantity=int(input("Enter the quantity:"))
    products[product_name]=quantity
print(products)
for key in products:
    print(key)
for value in products.values():
    print(value)

#code 3
employees={}
for i in range(3):
    employee_name=input("Enter the name:")
    salary=int(input("Enter the salary:"))
    employees[employee_name]=salary
print(employees)
for key,value in employees.items():
    if value>30000:
        print(key)






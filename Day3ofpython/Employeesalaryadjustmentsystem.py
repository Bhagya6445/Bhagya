list = []
num_employees = int(input("Enter the number of employees :"))
employees = []
for i in range(num_employees):
    name  = input(f"Enter the Employee name: ")
    salary = float(input(f"Enter the Employee salary: "))
    rating = int(input(f"Enter the Employee rating between 1&5: "))
    list.append({"name": name,"salary": salary,"rating": rating})
    print(list)
adjust_salary = lambda salary ,rating:salary *0.10 if salary >=4 else salary *1.05 if rating ==3 else salary *0.97    
updated_salary = adjust_salary(salary,rating)
print(f"updated salary for {name}: {updated_salary}")
employees.append({"name": name,"salary": updated_salary+salary,"rating": rating})
print(employees)

persons = int(input("Enter the number of persons: "))
customers = []
for i in range(persons):
    name = input(f"Enter the person name: ")
    age = int(input(f"Enter the person age: "))
    total_purchase = float(input(f"Enter  the total amount spent by the customer: "))
    customers.append({"name" : name, "age" : age, "total_purchase" : total_purchase})
    print(customers)
apply_discount = lambda c:{
    "name": c["name"],"age": c["age"],"total_purchase": c["total_purchase"] *(1.0 if c["age"] <=25 else 0.05)}
eligible_customers = filter(lambda c: c["age"] <= 40,customers)
discounted_customers = list(map(apply_discount,eligible_customers))
print("Customers with discount applied:")
for customer in discounted_customers:
    print(customer)

                           
          
#List & Dictionary: Stores customer details.
# input() & int()/float(): Takes user input.
#Loop (for): Repeats for multiple customers.
#Lambda Functions (lambda): Anonymous function to apply discount.
#filter(): Selects customers eligible for a discount.
#map(): Modifies eligible customers by applying the discount.

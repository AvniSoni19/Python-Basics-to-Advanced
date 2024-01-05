stocks=[('Reliance',1000),('Tata',2000),('Adani',2500)]
for stock,price in stocks:
    print(stock) 
for stock,price in stocks:    
    print(price)

employee_info=[('abc',200),('xyz',300),('pqr',500)]
  
def salary_largest(n):
    largest=0
    emp_name=''
    for i,j in n:
        if j>largest:
            largest=j
            emp_name=i
    print(f"{largest} thousand rupees to our employee {emp_name}")
    

salary_largest(employee_info)

list1=[['Shweta',20000],['Mayank',30000],['Shubham',15000],['Riya',35000],['Tarun',20000]]

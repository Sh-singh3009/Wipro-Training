from oopconcepts.employeedetails import EmployeeDetails

#driver
emp_no = int(input('Enter employee no: '))
emp_name = input('Enter employee name: ')
basic_pay = float(input('Enter basic salary: '))

employee = EmployeeDetails(e_no=emp_no, e_name=emp_name, bsc_pay=basic_pay)
print('Emp no: ', employee.e_no)
print('Emp name: ', employee.e_name)
print('Basic Pay: ', employee.bsc_pay)
print('Salary : ', employee.calculate_netsal())
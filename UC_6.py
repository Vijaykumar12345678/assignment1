import random

def main():
    wage_per_hour = 20
    full_day_hours = 8
    half_day_hours = 4
    daily_wage = 0
    monthly_wage = 0
    total_no_of_days = int(input("Enter the number of days you were supposed to work (between 1-20): "))

    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======\n")
    
    total_hours = total_no_of_days * full_day_hours
    counter = 0

    for i in range(1, total_no_of_days + 1):
        emp_check = random.randint(0, 2)  # Generates 0, 1, or 2

        if emp_check == 0:
            print(f"Employee is Present on day and is working full time: {i}")
            daily_wage = wage_per_hour * full_day_hours
            print(f"The daily wage of Employee is: {daily_wage}\n")
            counter += 1
        elif emp_check == 1:
            print(f"Employee is Present but working part time on day: {i}")
            daily_wage = wage_per_hour * half_day_hours
            print(f"The daily wage of Employee is: {daily_wage}\n")
        elif emp_check == 2:
            print(f"Employee is Absent on day: {i}")
            daily_wage = 0
            print(f"The daily wage of Employee is: {daily_wage}\n")

        monthly_wage += daily_wage

    print("\n")
    print(f"The monthly wage of employee is: {monthly_wage}")

if __name__ == "__main__":
    main()

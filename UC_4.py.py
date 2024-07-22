import random

def main():
    wage_per_hour = 20
    full_day_hours = 8
    half_day_hours = 4
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======\n")

    emp_check = random.randint(0, 2)  # Generates 0, 1, or 2

    if emp_check == 0:
        print("Employee is Present")
        print(f"The daily wage of Employee is: {wage_per_hour * full_day_hours}\n")
    elif emp_check == 1:
        print("Employee is Present but working part time")
        print(f"The daily wage of Employee is: {wage_per_hour * half_day_hours}\n")
    elif emp_check == 2:
        print("Employee is Absent")
        print("The daily wage of Employee is: 0\n")

if __name__ == "__main__":
    main()

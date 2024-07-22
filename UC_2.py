import random

def main():
    wage_per_hour = 20
    full_day_hours = 8
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======\n")

    emp_check = random.randint(0, 1)  # Generates 0 or 1
    if emp_check == 0:
        print("Employee is Present")
        print(f"The daily wage of Employee is: {wage_per_hour * full_day_hours}\n")
    else:
        print("Employee is Absent")
        print("The daily wage of Employee is: 0\n")

if __name__ == "__main__":
    main()

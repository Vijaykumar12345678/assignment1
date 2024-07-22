import random

def main():
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
    
    emp_check = random.randint(0, 1)  # Generates 0 or 1
    if emp_check == 0:
        print("Employee is Present")
    else:
        print("Employee is Absent")

if __name__ == "__main__":
    main()

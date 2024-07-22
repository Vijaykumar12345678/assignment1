import random

class EmployeeWageComputation:
    def __init__(self, company_name, wage_per_hour, total_no_of_days):
        self.wage_per_hour = wage_per_hour
        self.full_day_hours = 8
        self.half_day_hours = 4
        self.daily_wage = 0
        self.monthly_wage = 0
        self.counter1 = 0.0
        self.total_hour_present = 0
        self.total_hour_part_time = 0
        self.total_hour_absent = 0
        self.total_hours = 0
        self.emp_check = 0
        self.total_no_of_days = total_no_of_days
        self.company_name = company_name

    def attendance_check(self):
        self.emp_check = random.randint(0, 2)
        if self.emp_check == 0:
            print(f"{self.company_name}: Employee is Present and is working full time")
            self.total_hour_present += 8
            self.counter1 += 1.0
        elif self.emp_check == 1:
            print(f"{self.company_name}: Employee is Present but working part time")
            self.total_hour_part_time += 4
            self.counter1 += 0.5
        else:
            print(f"{self.company_name}: Employee is Absent")
            self.total_hour_absent += 0
            self.counter1 += 0.0

    def calculate_daily_wage(self):
        if self.emp_check == 0:
            self.daily_wage = self.wage_per_hour * self.full_day_hours
            print(f"{self.company_name}: The daily wage of Employee is: {self.daily_wage}")
        elif self.emp_check == 1:
            self.daily_wage = self.wage_per_hour * self.half_day_hours
            print(f"{self.company_name}: The daily wage of Employee is: {self.daily_wage}")
        else:
            self.daily_wage = 0
            print(f"{self.company_name}: The daily wage of Employee is: {self.daily_wage}")

    def calculate_monthly_wage(self):
        self.monthly_wage += self.daily_wage
        self.total_hours = self.total_hour_present + self.total_hour_part_time

    def monthly_wage_condition(self):
        if self.counter1 >= 20 or self.total_hours >= 100:
            print(f"{self.company_name}: Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"{self.company_name}: Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"{self.company_name}: Total working hour while employee is Absent: {self.total_hour_absent}")
            print(f"{self.company_name}: The monthly wage is: {self.monthly_wage}")
        else:
            print(f"{self.company_name}: Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"{self.company_name}: Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"{self.company_name}: The total hours employee worked is: {self.total_hours}")
            print(f"{self.company_name}: The monthly wage is: {self.monthly_wage}")

    def combine_method(self):
        total_no_of_days = int(input(f"Enter the number of days you were supposed to work (between 1-20) for {self.company_name}: "))
        for i in range(1, total_no_of_days + 1):
            print(f"DAY NO: {i}")
            self.attendance_check()
            self.calculate_daily_wage()
            self.calculate_monthly_wage()
        self.monthly_wage_condition()

def main():
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
    print("")
    tata_motors = EmployeeWageComputation("Tata Motors", 20, 5)
    bridgelabz = EmployeeWageComputation("Bridelabz", 16, 6)
    sam_solutions = EmployeeWageComputation("Sam Solutions", 25, 3)
    user_choice = 'Y'
    while user_choice.upper() == 'Y':
        choice = int(input("Enter your choice 1:Tata Motors 2:Bridelabz 3:Sam Solutions: "))
        if choice == 1:
            print(f"COMPANY NAME: {tata_motors.company_name}")
            tata_motors.combine_method()
            print("\n")
        elif choice == 2:
            print(f"COMPANY NAME: {bridgelabz.company_name}")
            bridgelabz.combine_method()
            print("\n")
        elif choice == 3:
            print(f"COMPANY NAME: {sam_solutions.company_name}")
            sam_solutions.combine_method()
            print("\n")
        else:
            print("Not a valid choice")
        user_choice = input("Do you wish to check any other company details: if yes press 'Y' or else 'N': ")
    print("Thank you for using the service")

if __name__ == "__main__":
    main()

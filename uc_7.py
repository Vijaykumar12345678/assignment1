import random

class EmployeeWageComputation:
    def __init__(self):
        self.wage_per_hour = 20
        self.full_day_hours = 8
        self.half_day_hours = 4
        self.daily_wage = 0
        self.monthly_wage = 0
        self.counter1 = 0
        self.total_hour_present = 0
        self.total_hour_part_time = 0
        self.total_hour_absent = 0
        self.total_hours = 0
        self.emp_check = 0

    def attendance_check(self):
        self.emp_check = random.randint(0, 2)  # Generates 0, 1, or 2
        if self.emp_check == 0:
            print("Employee is Present and is working full time")
            self.total_hour_present += self.full_day_hours
        elif self.emp_check == 1:
            print("Employee is Present but working part time")
            self.total_hour_part_time += self.half_day_hours
        elif self.emp_check == 2:
            print("Employee is Absent")
            self.total_hour_absent += 0

    def calculate_daily_wage(self):
        if self.emp_check == 0:
            self.daily_wage = self.wage_per_hour * self.full_day_hours
            print(f"The daily wage of Employee is: {self.daily_wage}\n")
        elif self.emp_check == 1:
            self.daily_wage = self.wage_per_hour * self.half_day_hours
            print(f"The daily wage of Employee is: {self.daily_wage}\n")
        else:
            self.daily_wage = 0
            print(f"The daily wage of Employee is: {self.daily_wage}\n")

    def calculate_monthly_wage(self):
        self.monthly_wage += self.daily_wage
        self.total_hours = self.total_hour_present + self.total_hour_part_time

    def monthly_wage_condition(self):
        if self.counter1 >= 20 or self.total_hours >= 100:
            print(f"Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"Total working hour while employee is Absent: {self.total_hour_absent}")
            print(f"The monthly wage is: {self.monthly_wage}")
        else:
            print(f"Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"The total hours employee worked is: {self.total_hours}")
            print(f"The monthly wage is: {self.monthly_wage}")

def main():
    total_no_of_days = int(input("Enter the number of days you were supposed to work (between 1-20): "))
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======\n")
    
    e1 = EmployeeWageComputation()

    for i in range(1, total_no_of_days + 1):
        print(f"The day is: {i}")
        e1.attendance_check()
        e1.calculate_daily_wage()
        e1.calculate_monthly_wage()

    e1.monthly_wage_condition()

if __name__ == "__main__":
    main()


import json
import os


# Function to load data from a JSON file
def load_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: JSON data must contain a list of employees.")
            return []

        # Validate required keys
        required_keys = ["id", "name", "department", "salary", "age"]

        valid_data = []

        for employee in data:
            if not isinstance(employee, dict):
                print("Warning: Invalid employee record skipped.")
                continue

            if all(key in employee for key in required_keys):
                valid_data.append(employee)
            else:
                print("Warning: Employee record missing required keys.")

        return valid_data

    except FileNotFoundError:
        print("Error: JSON file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON file format.")
        return []
    except OSError as error:
        print("File error:", error)
        return []


# Function to search for an employee by name
def search_employee(data, name):
    results = [
        employee for employee in data
        if name.lower() in employee["name"].lower()
    ]

    if results:
        print("\nSearch Results:")
        for employee in results:
            print(employee)
    else:
        print("No matching employee found.")


# Function to filter employees by department
def filter_by_department(data, department):
    results = [
        employee for employee in data
        if employee["department"].lower() == department.lower()
    ]

    if results:
        print("\nFiltered Employees:")
        for employee in results:
            print(employee)
    else:
        print("No employees found in this department.")


# Function to calculate summary information
def show_summary(data):
    if not data:
        print("No employee data available.")
        return

    total_employees = len(data)
    total_salary = sum(employee["salary"] for employee in data)
    average_salary = total_salary / total_employees
    highest_salary = max(data, key=lambda emp: emp["salary"])

    print("\nEmployee Summary")
    print("-------------------------")
    print("Total Employees:", total_employees)
    print("Total Salary:", total_salary)
    print("Average Salary:", round(average_salary, 2))
    print("Highest Paid Employee:", highest_salary["name"])
    print("Highest Salary:", highest_salary["salary"])


# Function to save processed data to a JSON file
def save_data(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully.")
    except OSError as error:
        print("Error saving data:", error)


# Main program
def main():
    filename = "employees.json"
    data = load_data(filename)

    if not data:
        print("No valid employee records loaded.")
        return

    while True:
        print("\n===== JSON Data Processor =====")
        print("1. Search Employee")
        print("2. Filter by Department")
        print("3. Show Summary")
        print("4. Display All Employees")
        print("5. Save Data to JSON")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter employee name to search: ").strip()
            if name:
                search_employee(data, name)
            else:
                print("Please enter a name.")

        elif choice == "2":
            department = input("Enter department name: ").strip()
            if department:
                filter_by_department(data, department)
            else:
                print("Please enter a department.")

        elif choice == "3":
            show_summary(data)

        elif choice == "4":
            print("\nAll Employee Records:")
            for employee in data:
                print(employee)

        elif choice == "5":
            save_data("processed_employees.json", data)

        elif choice == "6":
            print("Thank you for using JSON Data Processor!")
            break

        else:
            print("Invalid choice. Please select from 1 to 6.")


if __name__ == "__main__":
    main()

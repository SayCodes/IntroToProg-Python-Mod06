# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sayali Bhosale,2/18/2024,Assignment 06: Functions
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Data Constants
FILE_NAME: str = "Enrollments.json"

# Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file = None
menu_choice: str = ''
student_data: dict = {}
students: list = []
json_data: str = ''


class FileProcessor:
    """Handles file read and write operations."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a JSON file into a list."""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages("File not found.", e)
        except JSONDecodeError as e:
            IO.output_error_messages("File not in valid json format.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list to a JSON file."""
        try:
            with open(file_name, 'w') as file_obj:
                json.dump(student_data, file_obj)
        except IOError as e:
            IO.output_error_messages("Error writing to file.", e)


class IO:
    """Handles input/output operations."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages."""
        if error:
            print(f"Error: {message} {error}")
        else:
            print(f"Error: {message}")

    @staticmethod
    def output_menu(menu: str):
        """Outputs the menu."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets user input for menu choice."""
        return input("Enter your choice: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Outputs student data."""
        for student in student_data:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")

    @staticmethod
    def input_student_data(student_data: list):
        """Gets user input for student data."""
        try:
            first_name = input("Enter student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should only contain letters.")
            last_name = input("Enter student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should only contain letters.")
            course_name = input("Enter course name: ")
            student_data.append({"FirstName": first_name, "LastName": last_name, "CourseName": course_name})
            print("Student registered successfully.")
        except ValueError as e:
            IO.output_error_messages(str(e))


# Read data from file
FileProcessor.read_data_from_file(FILE_NAME, students)

# Main loop
while menu_choice != "4":
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)

    elif menu_choice == "2":
        IO.output_student_courses(students)

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        print("Data saved successfully to file.")

    elif menu_choice == "4":
        print("Program Ended\n")

    else:
        IO.output_error_messages("Please select option 1, 2, 3 or 4.")

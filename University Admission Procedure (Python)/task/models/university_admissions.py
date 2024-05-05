import logging

from models.student import Student
from utils.set_logging import init_debug_and_info_handlers

# Create a logger
logger = logging.getLogger(__name__)
init_debug_and_info_handlers(logger)


class UniversityAdmissions:

    def __init__(self):
        self.number_of_accepted_students: int = 0
        self.number_of_rejected_students: int = 0
        self.number_of_applicants: int = 0
        self.accepted_students: list[Student] = []
        self.rejected_students: list[Student] = []
        self.initial_students_list: list[Student] = self.receive_applicants()

    def receive_applicants(self):
        # create a list to store the students
        students: list[Student] = []
        # create a variable to store the number of students
        self.number_of_applicants: int = int(input())
        # create a variable for number of students to be accepted
        self.number_of_accepted_students: int = int(input())
        # create a loop to get all the students
        for _ in range(self.number_of_applicants):
            # Get the user input as a string
            user_input: str = input()
            # Split the string into a list of substrings based on space
            first_name, last_name, gpa = user_input.split(" ")
            # Convert gpa to float
            gpa: float = float(gpa)
            # Create a Student instance
            student: Student = Student(first_name, last_name, gpa)
            logger.debug(f"{Student.__repr__(student)}")
            # Append the student object to the students list
            students.append(student)
            logger.debug(f"Student {student.first_name} {student.last_name} has been added to the list.")
        # return the students list
        return students

    def sort_applicants(self):
        # sort the students list based on the gpa and then by full name
        self.initial_students_list.sort(key=lambda x: (-x.gpa, x.first_name, x.last_name))
        logger.debug(f"Students list has been sorted based on GPA.")
        logger.debug(f"Students list: {self.initial_students_list}")

    def admit_students(self):
        # Sort the students list based on the gpa and then by full name
        self.sort_applicants()
        # Admit the top students based on the number of accepted students
        logger.debug(f"Admitting {self.number_of_accepted_students} students.")
        self.accepted_students = self.initial_students_list[:self.number_of_accepted_students]
        # Reject the remaining students
        self.rejected_students = self.initial_students_list[self.number_of_accepted_students:]
        logger.debug(f"Accepted students: {self.accepted_students}")
        logger.debug(f"Rejected students: {self.rejected_students}")

    def display_admitted_students(self):
        # Print the list of admitted students
        logger.info("Successful applicants:")
        for student in self.accepted_students:
            logger.info(f"{student.first_name} {student.last_name}")

    def check_admission(self, student):
        if student.get_average_score() >= 60:
            logger.info("Congratulations, you are accepted!")
            return True
        else:
            logger.info("We regret to inform you that we will not be able to offer you admission.")
            return False

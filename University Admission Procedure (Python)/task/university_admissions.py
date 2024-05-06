import logging
from collections import defaultdict

from student import Student
from util.set_logging import init_debug_and_info_handlers

# Create a logger
logger = logging.getLogger(__name__)
init_debug_and_info_handlers(logger)


class UniversityAdmissions:

    def __init__(self):
        self.number_of_accepted_students_per_dept: int = 0
        self.number_of_rejected_students: int = 0
        self.number_of_applicants: int = 0
        self.departments = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
        self.initial_students_list: list[Student] = self.receive_applicants()
        self.accepted_students: defaultdict[str, list] = self.select_best_candidates(self.initial_students_list,
                                                                                     self.number_of_accepted_students_per_dept)
        self.rejected_students: list[Student] = []

    def receive_applicants(self):
        # create a list to store the student.py
        students: list[Student] = []
        # create a variable for number of student.py to be accepted
        self.number_of_accepted_students_per_dept: int = int(input())
        # create a loop to get all the student.py
        with open('./applicants.txt', 'r') as file:
            for line in file:
                data = line.strip().split(" ", 5)
                # Split the string into a list of substrings based on space
                first_name, last_name, gpa, first_choice, second_choice, third_choice = data
                # Convert gpa to float
                gpa: float = float(gpa)
                # Create a Student instance
                student: Student = Student(first_name, last_name, gpa, first_choice, second_choice, third_choice)
                logger.debug(f"{Student.__repr__(student)}")
                # Append the student object to the student.py list
                students.append(student)
                logger.debug(f"Student {student.first_name} {student.last_name} has been added to the list.")
        # return the student.py list
        return students

    def sort_applicants(self, filtered_applicants: list[Student]):
        logger.debug("Sorting applicants based on GPA and name...")
        sorted_applicants = sorted(filtered_applicants, key=lambda x: (-x.gpa, x.first_name + x.last_name))
        logger.debug("Applicants sorted.")
        return sorted_applicants

    def select_best_candidates(self, applicants: list[Student], n: int):
        logger.debug("Selecting best candidates for each department...")
        departments = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
        admitted_students = defaultdict(list)
        remaining_applicants = applicants.copy()

        for priority in range(3):
            logger.debug(f"Considering priority level {priority + 1}...")
            for department in departments:
                logger.debug(f"Processing department: {department}")
                filtered_applicants = [applicant for applicant in remaining_applicants if
                                       applicant.priorities[priority] == department]
                logger.debug(f"Number of applicants for {department}: {len(filtered_applicants)}")
                sorted_applicants = self.sort_applicants(filtered_applicants)
                # Select the top candidates from the sorted applicants
                selected_applicants = sorted_applicants[:max(0, n - len(admitted_students[department]))]
                logger.debug(f"Number of selected applicants for {department}: {len(selected_applicants)}")
                admitted_students[department].extend(selected_applicants)
                remaining_applicants = [applicant for applicant in remaining_applicants if
                                        applicant not in selected_applicants]
                logger.debug(f"Number of remaining applicants: {len(remaining_applicants)}")

        logger.debug("Best candidates selected for each department.")
        self.re_sort_accepted_students(admitted_students)
        logger.debug(f"Admitted students: {admitted_students}")
        return admitted_students

    def re_sort_accepted_students(self, admitted_students: defaultdict[str, list]):
        for department in self.departments:
            admitted_students[department] = self.sort_applicants(admitted_students[department])
            logger.debug(f"Re-Sorted admitted students for {department}:")

    def print_admitted_students(self):
        logger.debug("Printing admitted students for each department...")

        for department in self.departments:
            logger.info(department)
            for student in self.accepted_students[department]:
                logger.info(f"{student.first_name} {student.last_name} {student.gpa}")
            logger.info("")
        logger.debug("Admitted students printed.")

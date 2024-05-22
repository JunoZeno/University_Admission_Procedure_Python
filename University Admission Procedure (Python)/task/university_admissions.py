import logging
from collections import defaultdict

from student import Student
from util.set_logging import init_debug_and_info_handlers

# Create a logger
logger = logging.getLogger(__name__)
init_debug_and_info_handlers(logger)


class UniversityAdmissions:

    def __init__(self):
        """
        This is the constructor method for the UniversityAdmissions class.

        It initializes the following attributes:
        - number_of_accepted_students_per_dept: The number of students to be accepted per department. Initialized to 0.
        - number_of_rejected_students: The number of students that were rejected. Initialized to 0.
        - number_of_applicants: The total number of applicants. Initialized to 0.
        - departments: A list of the departments in the university.
        - test_score_student_index: A dictionary mapping each department to the index of the test score relevant to it.
        - initial_students_list: A list of Student objects representing the initial applicants. It is populated by calling the receive_applicants method.
        - accepted_students: A defaultdict mapping each department to a list of the students accepted to it. It is populated by calling the select_best_candidates method.
        - rejected_students: A list of Student objects representing the students that were rejected. Initialized as an empty list.
        """
        self.number_of_accepted_students_per_dept: int = 0
        self.number_of_rejected_students: int = 0
        self.number_of_applicants: int = 0
        self.departments = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
        self.initial_students_list: list[Student] = self.receive_applicants()
        self.accepted_students: defaultdict[str, list] = self.select_best_candidates(self.initial_students_list,
                                                                                     self.number_of_accepted_students_per_dept)
        self.rejected_students: list[Student] = []

    def receive_applicants(self):
        """
        This method is responsible for receiving the applicants from a file and creating a list of Student objects.

        It first reads the number of students to be accepted per department from the user input.
        Then, it reads the 'applicants.txt' file line by line, where each line represents a student's data.
        The data includes the student's first name, last name, test scores in physics, chemistry, mathematics, and computer science,
        and their first, second, and third choices of department.

        Each line is split into a list of strings, and the test scores are converted to integers.
        A Student object is created with these data and appended to the students list.

        The method returns the list of Student objects.

        :return: A list of Student objects representing the applicants.
        :rtype: list[Student]
        """
        # create a list to store the student.py
        students: list[Student] = []
        # create a variable for number of student.py to be accepted
        self.number_of_accepted_students_per_dept: int = int(input())
        # create a loop to get all the student.py
        with open('./applicants.txt', 'r') as file:
            for line in file:
                data: list[str] = line.strip().split(" ", 9)
                # Split the string into a list of substrings based on space
                first_name, last_name, phs_test, chem_test, math_test, cs_test, first_choice, second_choice, third_choice = data
                # convert the test scores to integer
                phs_test = int(phs_test)
                chem_test = int(chem_test)
                math_test = int(math_test)
                cs_test = int(cs_test)
                # Create a Student instance
                student: Student = Student(first_name, last_name, phs_test,
                                           chem_test, math_test, cs_test,
                                           first_choice, second_choice, third_choice)
                logger.debug(f"{Student.__repr__(student)}")
                # Append the student object to the student.py list
                students.append(student)
                logger.debug(f"Student {student.first_name} {student.last_name} has been added to the list.")
        # return the student.py list
        return students

    def sort_applicants(self, filtered_applicants: list[Student], department: str):
        """
        This method sorts the applicants based on their test scores and names.

        It first logs a debug message indicating the start of the sorting process.
        Then, it sorts the applicants in descending order of their test scores relevant to the department.
        If two applicants have the same test score, they are sorted in ascending order of their names.
        The sorted list of applicants is then returned.

        :param filtered_applicants: A list of Student objects representing the applicants to be sorted.
        :type filtered_applicants: list[Student]
        :param department: The department for which the applicants are being sorted.
        :type department: str
        :return: A list of Student objects representing the sorted applicants.
        :rtype: list[Student]
        """
        logger.debug("Sorting applicants based on test scores and name...")
        sorted_applicants = sorted(filtered_applicants,
                                   key=lambda x: (-x.req_test_scores_per_subject[department], x.first_name + x.last_name))
        logger.debug("Applicants sorted.")
        return sorted_applicants

    def select_best_candidates(self, applicants: list[Student], n: int):
        """
        This method selects the best candidates for each department based on their test scores and priorities.

        It first creates a copy of the applicants list and a defaultdict to store the admitted students.
        Then, it iterates over the three priority levels and the departments.
        For each department, it filters the applicants whose current priority is the department and sorts them.
        The top candidates are selected from the sorted applicants based on the number of remaining spots in the department.
        These candidates are added to the admitted students and removed from the remaining applicants.

        After all the departments and priority levels have been processed, the admitted students are re-sorted.
        The method returns the defaultdict mapping each department to a list of the students admitted to it.

        :param applicants: A list of Student objects representing the initial applicants.
        :type applicants: list[Student]
        :param n: The number of students to be accepted per department.
        :type n: int
        :return: A defaultdict mapping each department to a list of the students admitted to it.
        :rtype: defaultdict[str, list]
        """
        logger.debug("Selecting best candidates for each department...")

        admitted_students = defaultdict(list)
        remaining_applicants = applicants.copy()

        for priority in range(3):
            logger.debug(f"Considering priority level {priority + 1}...")
            for department in self.departments:
                logger.debug(f"Processing department: {department}")
                filtered_applicants = [applicant for applicant in remaining_applicants if
                                       applicant.priorities[priority] == department]
                logger.debug(f"Number of applicants for {department}: {len(filtered_applicants)}")
                sorted_applicants = self.sort_applicants(filtered_applicants, department)
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
        """
        This method re-sorts the admitted students for each department based on their GPA and name.

        It iterates over the departments and for each department, it sorts the admitted students by calling the sort_applicants method.
        The sorted list of students is then assigned back to the department in the admitted_students defaultdict.

        :param admitted_students: A defaultdict mapping each department to a list of the students admitted to it.
        :type admitted_students: defaultdict[str, list]
        """
        for department in self.departments:
            admitted_students[department] = self.sort_applicants(admitted_students[department], department)
            logger.debug(f"Re-Sorted admitted students for {department}:")

    def print_admitted_students(self):
        """
        This method prints the admitted students for each department.

        It first logs a debug message indicating the start of the printing process.
        Then, it iterates over the departments. For each department, it logs the department name and the details of each student admitted to it.
        The details include the student's first name, last name, and the test score relevant to the department.
        After printing the students for a department, it logs an empty line for readability.
        Finally, it logs a debug message indicating the end of the printing process.
        """
        logger.debug("Printing admitted students for each department...")

        for department in self.departments:
            logger.info(department)
            for student in self.accepted_students[department]:
                logger.info(f"{student.first_name} {student.last_name} {student.req_test_scores_per_subject[department]}")
            logger.info("")
        logger.debug("Admitted students printed.")

    def send_admitted_students_list_to_files(self):
        """
        This method sends the list of admitted students for each department to separate files.
        :return:
        """
        logger.debug("Creating file for admitted students for each department...")

        for department in self.departments:
            department_file_name = department.lower() + ".txt"
            with open(f'./{department_file_name}', 'w') as file:
                for student in self.accepted_students[department]:
                    file.write(f"{student.first_name} {student.last_name} {student.req_test_scores_per_subject[department]}\n")
        logger.debug("Admitted students added to files.")

import logging

from util.set_logging import init_debug_and_info_handlers

# Create a logger
logger = logging.getLogger(__name__)
init_debug_and_info_handlers(logger)


class Student:
    """
    This class represents a Student applying for university admission.

    Attributes:
    - amount_scores_required: The number of test scores required for admission. Set to 3.
    - first_name: The first name of the student.
    - last_name: The last name of the student.
    - test_scores: A list of the student's test scores in Physics, Chemistry, Mathematics, and Computer Science.
    - priorities: A list of the student's department preferences in order of priority.
    - scores: A list of the student's scores. Initialized as an empty list.
    """

    amount_scores_required = 3

    def __init__(self, first_name, last_name, physics_test, chem_test, math_test, cs_test,
                 first_choice, second_choice, third_choice):
        """
        This is the constructor method for the Student class.

        It initializes the following attributes:
        - first_name: The first name of the student.
        - last_name: The last name of the student.
        - test_scores: A list of the student's test scores in Physics, Chemistry, Mathematics, and Computer Science.
        - priorities: A list of the student's department preferences in order of priority.
        - scores: A list of the student's scores. Initialized as an empty list.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.test_scores: list[int] = [physics_test, chem_test, math_test, cs_test]
        self.req_test_scores_per_subject: dict[str, float] = {  # Added for easier access to test scores per subject
            'Biotech': self.get_average_score([physics_test, chem_test]),
            'Chemistry': chem_test,
            'Engineering': self.get_average_score([math_test, cs_test]),
            'Mathematics': math_test,
            'Physics': self.get_average_score([physics_test, math_test])
        }
        self.priorities = [first_choice, second_choice, third_choice]
        self.scores: list[float] = []

    def get_average_score(self, scores: list[int]) -> float:
        """
        This method calculates and returns the average of the student's scores.

        :return: The average of the student's scores.
        :rtype: float
        """
        # Make sure this returns one decimal place
        return round(sum(scores) / len(scores), 1)

    def __repr__(self):
        """
        This method returns a string representation of the Student object.

        :return: A string representation of the Student object.
        :rtype: str
        """
        return (f"Student(first_name='{self.first_name}', last_name='{self.last_name}', gpa={self.test_scores},"
                f" priorities={self.priorities})")

    def __str__(self):
        """
        This method returns a string representation of the Student object, including the student's first name and average score.

        :return: A string representation of the Student object, including the student's first name and average score.
        :rtype: str
        """
        return f"{self.first_name} {self.get_average_score()}"

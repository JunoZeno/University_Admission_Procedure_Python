import logging
import sys

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # Change between INFO and DEBUG

# Create a stream handler for info messages
info_handler = logging.StreamHandler(sys.stdout)
info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter('%(message)s')
info_handler.setFormatter(info_formatter)

# Create a stream handler for debug messages
debug_handler = logging.StreamHandler(sys.stdout)
debug_handler.setLevel(logging.DEBUG)
debug_formatter = logging.Formatter('DEBUG - %(filename)s:%(lineno)d - %(message)s')
debug_handler.setFormatter(debug_formatter)

# Set the info handler to only handle INFO messages
info_handler.addFilter(lambda record: record.levelno == logging.INFO)

# Set the debug handler to only handle DEBUG messages
debug_handler.addFilter(lambda record: record.levelno == logging.DEBUG)

# Remove existing handlers from the logger preventing duplicate logs
for handler in logger.handlers[:]:
    logger.removeHandler(handler)

# Add the handlers to the logger
logger.addHandler(info_handler)
logger.addHandler(debug_handler)


class Student:
    amount_scores_required = 3

    def __init__(self, name=None):
        self.name = name
        self.scores = []

    def add_scores(self):
        for _ in range(Student.amount_scores_required):
            score = int(input())
            self.scores.append(score)
        logger.debug(f'self.scores')

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name} {self.get_average_score()}"


class UniversityAdmissions:
    def check_admission(self, student):
        if student.get_average_score() >= 60:
            logger.info("Congratulations, you are accepted!")
            return True
        else:
            logger.info("We regret to inform you that we will not be able to offer you admission.")
            return False


if __name__ == "__main__":
    student = Student()
    student.add_scores()
    logger.info(student.get_average_score())
    university = UniversityAdmissions()
    university.check_admission(student)

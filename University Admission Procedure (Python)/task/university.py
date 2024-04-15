import logging

from models.student import Student
from models.university_admissions import UniversityAdmissions
from utils import set_logging

# Create a logger
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    set_logging.init_debug_and_info_handlers(logger)
    student = Student()
    student.add_scores()
    logger.info(student.get_average_score())
    university = UniversityAdmissions()
    university.check_admission(student)

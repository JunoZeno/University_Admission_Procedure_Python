import logging

from utils import set_logging

from models.university_admissions import UniversityAdmissions

# Create a logger
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    set_logging.init_debug_and_info_handlers(logger)
    # student = Student()
    # student.add_scores()
    # logger.info(student.get_average_score())
    # university.check_admission(student)

    university = UniversityAdmissions()
    university.admit_students()
    university.display_admitted_students()

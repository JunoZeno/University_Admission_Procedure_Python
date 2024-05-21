import logging

from util import set_logging

from university_admissions import UniversityAdmissions

# Create a logger
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    set_logging.init_debug_and_info_handlers(logger)
    university = UniversityAdmissions()
    university.print_admitted_students()

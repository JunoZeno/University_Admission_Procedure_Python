import logging

from utils.set_logging import init_debug_and_info_handlers

# Create a logger
logger = logging.getLogger(__name__)
init_debug_and_info_handlers(logger)


class UniversityAdmissions:
    def check_admission(self, student):
        if student.get_average_score() >= 60:
            logger.info("Congratulations, you are accepted!")
            return True
        else:
            logger.info("We regret to inform you that we will not be able to offer you admission.")
            return False

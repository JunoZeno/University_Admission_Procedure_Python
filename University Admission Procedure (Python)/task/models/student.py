import logging

from utils.set_logging import init_debug_and_info_handlers

# Create a logger
logger = logging.getLogger(__name__)
init_debug_and_info_handlers(logger)


class Student:
    amount_scores_required = 3

    def __init__(self, first_name, last_name, gpa):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.gpa: float = gpa
        self.scores: list[float] = []

    def add_scores(self):
        for _ in range(Student.amount_scores_required):
            score = int(input())
            self.scores.append(score)
        logger.debug(f'{self.first_name} scores are {self.scores}')

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.gpa}"

    def __str__(self):
        return f"{self.first_name} {self.get_average_score()}"

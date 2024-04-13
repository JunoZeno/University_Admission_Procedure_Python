# write your code here

class Student:
    amount_scores_required = 3

    def __init__(self, name=None):
        self.name = name
        self.scores = []

    def add_scores(self):
        for _ in range(Student.amount_scores_required):
            score = int(input())
            self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name} {self.get_average_score()}"


class UniversityAdmissions:
    def check_admission(self, student):
        if student.get_average_score():
            print("Congratulations, you are accepted!")
            return True
        return False


if __name__ == "__main__":
    student = Student()
    student.add_scores()
    print(student.get_average_score())
    university = UniversityAdmissions()
    university.check_admission(student)
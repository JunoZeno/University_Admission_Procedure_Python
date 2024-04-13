from hstest import StageTest, CheckResult, WrongAnswer, TestCase

input_1 = ["70", "90", "60"]
input_2 = ["50", "53", "78"]
input_3 = ["100", "84", "10"]
input_4 = ["50", "50", "50"]


class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [
            TestCase(stdin=input_1, attach=input_1),
            TestCase(stdin=input_2, attach=input_2),
            TestCase(stdin=input_3, attach=input_3),
            TestCase(stdin=input_4, attach=input_4)
        ]

    @staticmethod
    def get_mean(*numbers):
        numbers = [int(number) for number in numbers]
        return sum(numbers) / len(numbers)

    def check(self, reply: str, attach: list):
        output = reply.lower().strip().split('\n')
        output = [line for line in output if line.strip()]
        if len(output) != 2:
            raise WrongAnswer("The output should contain 2 lines. \n"
                              "However, {0} lines were found in your output.".format(len(output)))
        correct_mean = round(self.get_mean(*attach), 2)
        try:
            output_mean = round(float(output[0].strip()), 2)
        except ValueError:
            raise WrongAnswer("The first line of your output is supposed to contain nothing but a number.\n")

        if output_mean != correct_mean:
            raise WrongAnswer("The mean score in your output is {0}.\n"
                              "However, the answer {1} was expected.".format(output_mean, correct_mean))

        if "congratulations" not in output[1] or "you are accepted" not in output[1]:
            raise WrongAnswer("The second line of your output does not seem to contain the line \n"
                              "\"Congratulations, you are accepted!\"")

        return CheckResult.correct()


if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()

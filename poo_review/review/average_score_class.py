class ScoreList:

    def __init__(self, scores):
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)


scores1 = ScoreList(scores=[75, 88, 90, 67])
print(f"A média do aluno1, que está registrada no scores 1 é:",
      f"{scores1.average()}")

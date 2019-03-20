class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    # Returns the latest score.
    def latest(self):
        return self.scores[-1]

    # Return the best score.
    def personal_best(self):
        return max(self.scores)

    # Return a list of three best scores.
    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]

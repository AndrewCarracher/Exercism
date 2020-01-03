class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def scores(self):
        return self.scores

    def latest(self):
        latest_score = self.scores[-1]
        return latest_score        

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]
        

    def personal_best(self):
        return max(self.scores)
        

    def report(self):
        latest_score = self.latest()
        best_score = self.personal_best()
        if best_score - latest_score <= 0:
            response = f"Your latest score was {latest_score}. That's your personal best!"
        else:
            difference = best_score - latest_score 
            response = f"Your latest score was {latest_score}. That's {difference} short of your personal best!"

        return response
        

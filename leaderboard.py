class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"{self.name}: {self.score}"

class Leaderboard:
    def __init__(self):
        self.players = {}

    def add_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)

    def update_score(self, name, points):
        if name in self.players:
            self.players[name].score += points
        else:
            self.add_player(name)
            self.players[name].score += points

    def get_top_players(self, n=10):
        sorted_players = sorted(self.players.values(), key=lambda p: p.score, reverse=True)
        return sorted_players[:n]

    def get_all_players(self):
        return list(self.players.values())

# For mini-games, perhaps a simple question class
class Question:
    def __init__(self, question, answer, points=10):
        self.question = question
        self.answer = answer
        self.points = points

class Game:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def play_game(self, player_name, leaderboard):
        score = 0
        for q in self.questions:
            user_answer = input(f"{q.question} ")
            if user_answer.lower() == q.answer.lower():
                score += q.points
                print("Correct!")
            else:
                print(f"Wrong! Correct answer: {q.answer}")
        leaderboard.update_score(player_name, score)
        print(f"{player_name} scored {score} points in {self.name}")